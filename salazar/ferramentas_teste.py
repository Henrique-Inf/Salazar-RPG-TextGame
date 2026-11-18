"""Ferramentas da sala de testes.

Para testar uma novidade (um combate, um NPC, um item novo...), escreva uma
função `minha_ferramenta(heroi)` que devolve um texto (ou None) e registre-a
no dicionário FERRAMENTAS no final deste arquivo. Ela aparece sozinha no menu
"Ferramentas de teste…" da sala de testes.
"""

from .dados import CLASSES, CONJUNTO_PADRAO, RACAS
from .exploracao import explorar, tela
from .interface import limpar, titulo, escolher
from .inventario import nome_item
from .itens import ITENS
from .laboratorio import SALA_LAB_ID, SALAS_LAB
from .mundo import SALAS, obter_sala, todas_as_flags
from .personagem import Personagem

VOLTAR = "Voltar"
ANDARES = ["Laboratório", "Subterrâneo", "Térreo", "Exterior"]


def personagem_de_teste(raca, classe):
    """Cria um personagem pronto, com os melhores valores nos atributos da classe."""
    principais = CLASSES[classe]["principal"]
    ordem = list(dict.fromkeys(principais + ["CON", "DES", "SAB", "INT", "CAR", "FOR"]))
    atributos = dict(zip(ordem, sorted(CONJUNTO_PADRAO, reverse=True)))

    # raças que escolhem atributos extras (Meio-Elfo): usa os melhores que puder
    extras = {}
    for a in ordem:
        if len(extras) >= RACAS[raca].get("escolhas_extras", 0):
            break
        if a not in RACAS[raca]["bonus"]:
            extras[a] = 1

    heroi = Personagem(
        nome="Testador",
        raca=raca,
        classe=classe,
        alinhamento="Neutro",
        atributos_base=atributos,
        bonus_escolhidos=extras,
        local=SALA_LAB_ID,
    )
    heroi.visitados.append(SALA_LAB_ID)
    heroi.modo_teste = True
    return heroi


# --- as ferramentas ---------------------------------------------------------

def dar_item(heroi):
    tela(heroi)
    kit = [f"kit:{i}" for i in range(len(CLASSES[heroi.classe]["equipamento"]))]
    nomes = {nome_item(heroi, i): i for i in list(ITENS) + kit if i not in heroi.inventario}
    if not nomes:
        return "Você já tem todos os itens do jogo."
    opcoes = list(nomes) + ["Dar todos", VOLTAR]
    escolha = escolher("Dar qual item?", opcoes, separar_antes=("Dar todos",))
    if escolha == VOLTAR:
        return None
    ids = list(nomes.values()) if escolha == "Dar todos" else [nomes[escolha]]
    heroi.inventario.extend(ids)
    return "Você recebeu: " + ", ".join(nome_item(heroi, i) for i in ids) + "."


def esvaziar_inventario(heroi):
    heroi.inventario.clear()
    heroi.pegos.clear()
    return "Inventário esvaziado."


def curar(heroi):
    heroi.pv_atual = heroi.pv_maximo
    return f"PV restaurados: {heroi.pv_atual}/{heroi.pv_maximo}."


def mudar_nivel(heroi):
    tela(heroi)
    opcoes = [f"Nível {n}" for n in range(1, 21)]
    escolha = escolher("Qual nível?", opcoes + [VOLTAR], separar_antes=(VOLTAR,))
    if escolha == VOLTAR:
        return None
    heroi.nivel = int(escolha.split()[1])
    heroi.pv_atual = heroi.pv_maximo
    return f"Agora você é nível {heroi.nivel}: PV {heroi.pv_maximo}, bônus de proficiência +{heroi.bonus_proficiencia}."


def eventos(heroi):
    """Liga e desliga os eventos do jogo (útil para testar partes do quebra-cabeça)."""
    flags = todas_as_flags()
    aviso = "[x] já aconteceu, [ ] ainda não. Escolha um para ligar ou desligar."
    while True:
        tela(heroi, aviso)
        rotulos = {f"[{'x' if f in heroi.flags else ' '}] {f}": f for f in flags}
        escolha = escolher("Eventos", list(rotulos) + [VOLTAR], separar_antes=(VOLTAR,))
        if escolha == VOLTAR:
            return None
        flag = rotulos[escolha]
        if flag in heroi.flags:
            heroi.flags.remove(flag)
        else:
            heroi.flags.append(flag)


def ir_para(heroi):
    """Teletransporta para qualquer sala do jogo (escolhendo o andar primeiro)."""
    tela(heroi)
    andar = escolher("Ir para qual andar?", ANDARES + [VOLTAR], separar_antes=(VOLTAR,))
    if andar == VOLTAR:
        return None
    salas = {s["nome"]: sid for sid, s in {**SALAS_LAB, **SALAS}.items() if s["andar"] == andar}
    tela(heroi)
    nome = escolher(f"Qual sala? ({andar})", list(salas) + [VOLTAR], separar_antes=(VOLTAR,))
    if nome == VOLTAR:
        return None
    heroi.local = salas[nome]
    if heroi.local not in heroi.visitados:
        heroi.visitados.append(heroi.local)
    return f"Você foi para: {nome}."


def reiniciar(heroi):
    heroi.inventario.clear()
    heroi.pegos.clear()
    heroi.flags.clear()
    heroi.visitados[:] = [SALA_LAB_ID]
    heroi.local = SALA_LAB_ID
    heroi.pv_atual = heroi.pv_maximo
    return "Tudo reiniciado: inventário, eventos e lugares visitados."


FERRAMENTAS = {
    "Dar item…": dar_item,
    "Esvaziar inventário": esvaziar_inventario,
    "Curar totalmente": curar,
    "Mudar nível…": mudar_nivel,
    "Eventos…": eventos,
    "Ir para…": ir_para,
    "Reiniciar tudo": reiniciar,
}


def menu_ferramentas(heroi):
    tela(heroi)
    escolha = escolher("Ferramentas de teste", list(FERRAMENTAS) + [VOLTAR], separar_antes=(VOLTAR,))
    if escolha == VOLTAR:
        return None
    return FERRAMENTAS[escolha](heroi)


def sala_de_testes():
    """Entrada pelo menu principal: escolhe raça e classe e vai para a sala de testes."""
    limpar()
    titulo("SALA DE TESTES")
    print("Um lugar para experimentar as novidades do jogo.")
    print("Nada aqui é salvo, e os seus jogos salvos não são tocados.")
    raca = escolher("Raça do personagem de teste", list(RACAS))
    classe = escolher("Classe do personagem de teste", list(CLASSES))
    explorar(personagem_de_teste(raca, classe), None, ferramentas=menu_ferramentas)
