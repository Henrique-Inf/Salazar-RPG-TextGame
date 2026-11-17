"""Criação de personagem passo a passo."""

from .dados import (
    ATRIBUTOS, NOMES_ATRIBUTOS, RACAS, CLASSES, ALINHAMENTOS,
    CONJUNTO_PADRAO, CUSTO_PONTOS, PONTOS_TOTAIS,
)
from .dados_rolagem import rolar_atributo
from .interface import titulo, perguntar, escolher, confirmar
from .personagem import Personagem, com_sinal


def distribuir_valores(valores, classe):
    """Deixa o jogador colocar cada valor em um atributo."""
    principais = CLASSES[classe]["principal"]
    nomes = [NOMES_ATRIBUTOS[p] for p in principais]
    print(f"\nDica: para {classe}, os atributos mais importantes são {', '.join(nomes)}.")

    restantes = sorted(valores, reverse=True)
    atributos = {}
    for valor in list(restantes):
        livres = [a for a in ATRIBUTOS if a not in atributos]
        if len(livres) == 1:
            atributos[livres[0]] = valor
            print(f"{valor} vai para {NOMES_ATRIBUTOS[livres[0]]}.")
            break
        opcoes = [NOMES_ATRIBUTOS[a] for a in livres]
        nome = escolher(f"Em qual atributo colocar o {valor}?", opcoes)
        atributos[livres[opcoes.index(nome)]] = valor
    return atributos


def compra_de_pontos():
    """Compra de pontos: todos começam em 8 e você gasta 27 pontos."""
    print("\nTodos os atributos começam em 8. Você tem 27 pontos para gastar (máximo 15).")
    atributos = {a: 8 for a in ATRIBUTOS}
    while True:
        gastos = sum(CUSTO_PONTOS[v] for v in atributos.values())
        restantes = PONTOS_TOTAIS - gastos
        rotulos = {f"{NOMES_ATRIBUTOS[a]:<13} {atributos[a]:>2}": a for a in ATRIBUTOS}
        opcoes = list(rotulos) + ["Concluir"]
        escolha = escolher(f"Pontos restantes: {restantes}", opcoes, separar_antes=("Concluir",))

        if escolha == "Concluir":
            if restantes and not confirmar(f"Ainda sobram {restantes} pontos. Concluir mesmo assim?"):
                continue
            return atributos

        a = rotulos[escolha]
        valor = atributos[a]
        acoes, descricoes = [], {}
        if valor < 15:
            custo = CUSTO_PONTOS[valor + 1] - CUSTO_PONTOS[valor]
            acoes.append("Aumentar")
            descricoes["Aumentar"] = f"custa {custo} ponto{'s' if custo > 1 else ''}"
        if valor > 8:
            acoes.append("Diminuir")
        acoes.append("Voltar")
        acao = escolher(f"{NOMES_ATRIBUTOS[a]}: {valor}", acoes, descricoes)

        if acao == "Aumentar":
            if gastos + CUSTO_PONTOS[valor + 1] - CUSTO_PONTOS[valor] > PONTOS_TOTAIS:
                print("Pontos insuficientes.")
            else:
                atributos[a] = valor + 1
        elif acao == "Diminuir":
            atributos[a] = valor - 1


def gerar_atributos(classe):
    metodos = [
        "Conjunto padrão (15, 14, 13, 12, 10, 8)",
        "Rolar 4d6 e descartar o menor",
        "Compra de pontos (27 pontos)",
    ]
    metodo = escolher("Como você quer definir os atributos?", metodos)

    if metodo == metodos[0]:
        return distribuir_valores(CONJUNTO_PADRAO, classe)

    if metodo == metodos[1]:
        while True:
            print("\nRolando os dados...")
            valores = []
            for _ in range(6):
                total, dados = rolar_atributo()
                print(f"  {dados} → {total}")
                valores.append(total)
            if confirmar(f"Valores: {sorted(valores, reverse=True)}. Ficar com eles?"):
                return distribuir_valores(valores, classe)

    return compra_de_pontos()


def escolher_bonus_extras(raca):
    """Para raças que escolhem atributos extras (ex.: Meio-Elfo)."""
    quantidade = RACAS[raca].get("escolhas_extras", 0)
    if not quantidade:
        return {}
    print(f"\n{raca}s ganham +1 em {quantidade} atributos à sua escolha.")
    disponiveis = [a for a in ATRIBUTOS if a not in RACAS[raca]["bonus"]]
    escolhidos = {}
    for _ in range(quantidade):
        opcoes = [NOMES_ATRIBUTOS[a] for a in disponiveis if a not in escolhidos]
        nome = escolher("Qual atributo recebe +1?", opcoes)
        escolhidos[next(a for a in disponiveis if NOMES_ATRIBUTOS[a] == nome)] = 1
    return escolhidos


def criar_personagem():
    titulo("CRIAÇÃO DE PERSONAGEM")
    print("Toda lenda começa com um nome.")
    nome = perguntar("Nome do herói", padrao="Salazar")

    raca = escolher(
        f"Qual é a raça de {nome}?",
        list(RACAS),
        {r: d["descricao"] for r, d in RACAS.items()},
    )
    bonus = ", ".join(f"{NOMES_ATRIBUTOS[a]} {com_sinal(v)}" for a, v in RACAS[raca]["bonus"].items())
    print(f"Bônus de {raca}: {bonus}")

    classe = escolher(
        f"Qual é a classe de {nome}?",
        list(CLASSES),
        {c: d["descricao"] for c, d in CLASSES.items()},
    )

    atributos_base = gerar_atributos(classe)
    bonus_escolhidos = escolher_bonus_extras(raca)
    alinhamento = escolher("Qual é o alinhamento?", ALINHAMENTOS)

    personagem = Personagem(
        nome=nome,
        raca=raca,
        classe=classe,
        alinhamento=alinhamento,
        atributos_base=atributos_base,
        bonus_escolhidos=bonus_escolhidos,
    )
    print()
    print(personagem.ficha())
    if not confirmar("Seguir com este personagem?"):
        return criar_personagem()
    return personagem
