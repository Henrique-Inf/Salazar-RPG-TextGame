"""Exploração: o jogador escolhe ações num menu para andar e examinar as coisas.

A tela é redesenhada a cada passo: cabeçalho com o estado do herói, a descrição
da sala, o resultado da última ação (se houve) e o menu.
"""

from .mundo import SALAS, saidas_disponiveis
from .interface import limpar, titulo, escolher
from .inventario import itens_no_chao, nome_item, obter_item, pegar, usar, texto_detalhe

LARGURA = 46
VOLTAR = "Voltar"
EXAMINAR = "Examinar…"
PEGAR = "Pegar…"
USAR = "Usar item…"
INVENTARIO = "Inventário"
PEGAR_TUDO = "Pegar tudo"
MAPA = "Mapa"
FICHA = "Ficha do personagem"
SALVAR = "Salvar jogo"
MENU = "Salvar e voltar ao menu"


def rotulo_direcao(direcao):
    if direcao in ("subir", "descer"):
        return f"{direcao.capitalize()} a escada"
    if direcao == "fora":
        return "Sair do convento"
    if direcao == "dentro":
        return "Voltar para dentro do convento"
    return f"Ir para o {direcao}"


def tela(heroi, mensagem=None):
    """Limpa a tela e desenha o cabeçalho, a sala e a mensagem da última ação."""
    limpar()
    sala = SALAS[heroi.local]
    print(f"{heroi.nome} · {heroi.raca} {heroi.classe} · PV {heroi.pv_atual}/{heroi.pv_maximo}")
    print("─" * LARGURA)
    print(f"{sala['nome']}  ({sala['andar']})")
    print()
    print(sala["descricao"])
    if mensagem:
        print()
        print("─" * LARGURA)
        print(mensagem)
    print()


def texto_mapa(heroi):
    linhas = ["Lugares que você já conhece:"]
    for andar in ("Subterrâneo", "Térreo", "Exterior"):
        salas = [s for s in heroi.visitados if SALAS[s]["andar"] == andar]
        if not salas:
            continue
        linhas.append(f"  {andar}:")
        for s in salas:
            marca = "  ◄ você está aqui" if s == heroi.local else ""
            linhas.append(f"    - {SALAS[s]['nome']}{marca}")
    return "\n".join(linhas)


def examinar(heroi):
    """Pergunta o que examinar e devolve o texto (ou None se o jogador voltar)."""
    detalhes = SALAS[heroi.local].get("detalhes", {})
    if not detalhes:
        return "Não há nada de especial para examinar aqui."
    tela(heroi)
    opcoes = [coisa.capitalize() for coisa in detalhes] + [VOLTAR]
    escolha = escolher("Examinar o quê?", opcoes, separar_antes=(VOLTAR,))
    if escolha == VOLTAR:
        return None
    return texto_detalhe(heroi, detalhes[escolha.lower()])


def menu_pegar(heroi, chao):
    """Escolhe o que pegar do chão. Devolve a mensagem (ou None se o jogador voltar)."""
    tela(heroi)
    nomes = {nome_item(heroi, i): i for i in chao}
    opcoes = list(nomes) + ([PEGAR_TUDO] if len(nomes) > 1 else []) + [VOLTAR]
    escolha = escolher("Pegar o quê?", opcoes, separar_antes=(VOLTAR,))
    if escolha == VOLTAR:
        return None
    ids = list(nomes.values()) if escolha == PEGAR_TUDO else [nomes[escolha]]
    pegos = [pegar(heroi, i) for i in ids]
    return "Você pegou: " + ", ".join(pegos) + "."


def menu_inventario(heroi):
    """Mostra os itens que você carrega; escolher um mostra a descrição."""
    if not heroi.inventario:
        return "Você não está carregando nada."
    tela(heroi)
    nomes = {nome_item(heroi, i): i for i in heroi.inventario}
    escolha = escolher(f"Inventário ({len(nomes)} itens)", list(nomes) + [VOLTAR], separar_antes=(VOLTAR,))
    if escolha == VOLTAR:
        return None
    return f"{escolha}\n{obter_item(heroi, nomes[escolha])['descricao']}"


def menu_usar(heroi):
    """Escolhe um item do inventário para usar neste lugar."""
    tela(heroi)
    nomes = {nome_item(heroi, i): i for i in heroi.inventario}
    escolha = escolher("Usar qual item?", list(nomes) + [VOLTAR], separar_antes=(VOLTAR,))
    if escolha == VOLTAR:
        return None
    return usar(heroi, nomes[escolha])


def mover(heroi, destino):
    heroi.local = destino
    if destino not in heroi.visitados:
        heroi.visitados.append(destino)


def despertar(heroi):
    limpar()
    titulo("PRÓLOGO")
    print(
        "Escuridão. Depois, frio.\n"
        "\n"
        f"{heroi.nome} abre os olhos devagar. A cabeça lateja, a boca está seca,\n"
        "e a memória é um poço vazio: nenhum rosto, nenhum lugar, nenhuma\n"
        "lembrança de como chegou até aqui. Só o próprio nome, e a certeza de\n"
        "que não deveria estar onde está."
    )


def explorar(heroi, salvar):
    """Laço principal de exploração. `salvar` é uma função que grava o jogo."""
    if heroi.local not in heroi.visitados:
        heroi.visitados.append(heroi.local)
    mensagem = None

    while True:
        sala = SALAS[heroi.local]

        # Um item de menu para cada saída. Se você já conhece o destino, ele aparece ao lado.
        destinos, descricoes = {}, {}
        for direcao, destino in saidas_disponiveis(sala, heroi.flags).items():
            rotulo = rotulo_direcao(direcao)
            destinos[rotulo] = destino
            if destino in heroi.visitados:
                descricoes[rotulo] = SALAS[destino]["nome"]

        tela(heroi, mensagem)
        mensagem = None
        chao = itens_no_chao(heroi)
        opcoes = list(destinos) + [EXAMINAR]
        if chao:
            opcoes.append(PEGAR)
        if heroi.inventario:
            opcoes.append(USAR)
        opcoes += [INVENTARIO, MAPA, FICHA, SALVAR, MENU]
        escolha = escolher("O que você faz?", opcoes, descricoes, separar_antes=(EXAMINAR, INVENTARIO))

        if escolha in destinos:
            mover(heroi, destinos[escolha])
        elif escolha == EXAMINAR:
            mensagem = examinar(heroi)
        elif escolha == PEGAR:
            mensagem = menu_pegar(heroi, chao)
        elif escolha == USAR:
            mensagem = menu_usar(heroi)
        elif escolha == INVENTARIO:
            mensagem = menu_inventario(heroi)
        elif escolha == MAPA:
            mensagem = texto_mapa(heroi)
        elif escolha == FICHA:
            mensagem = heroi.ficha()
        elif escolha == SALVAR:
            mensagem = f"Jogo salvo em {salvar(heroi).name}."
        elif escolha == MENU:
            salvar(heroi)
            return
