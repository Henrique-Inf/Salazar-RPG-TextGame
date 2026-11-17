"""Exploração: o jogador escolhe ações num menu para andar e examinar as coisas."""

from .mundo import SALAS
from .interface import titulo, escolher

VOLTAR = "Voltar"
EXAMINAR = "Examinar…"
OLHAR = "Olhar ao redor"
MAPA = "Mapa"
FICHA = "Ficha do personagem"
SALVAR = "Salvar jogo"
MENU = "Salvar e voltar ao menu"


def rotulo_direcao(direcao):
    if direcao in ("subir", "descer"):
        return f"{direcao.capitalize()} a escada"
    return f"Ir para o {direcao}"


def mostrar_sala(heroi, completa=True):
    sala = SALAS[heroi.local]
    print()
    print(f"== {sala['nome']} ==  ({sala['andar']})")
    if completa:
        print(sala["descricao"])


def mostrar_mapa(heroi):
    print("\nLugares que você já conhece:")
    for andar in ("Subterrâneo", "Térreo"):
        salas = [s for s in heroi.visitados if SALAS[s]["andar"] == andar]
        if not salas:
            continue
        print(f"  {andar}:")
        for s in salas:
            marca = "  ◄ você está aqui" if s == heroi.local else ""
            print(f"    - {SALAS[s]['nome']}{marca}")


def examinar(heroi):
    detalhes = SALAS[heroi.local].get("detalhes", {})
    if not detalhes:
        print("\nNão há nada de especial para examinar aqui.")
        return
    opcoes = [coisa.capitalize() for coisa in detalhes] + [VOLTAR]
    escolha = escolher("Examinar o quê?", opcoes, separar_antes=(VOLTAR,))
    if escolha != VOLTAR:
        print(f"\n{detalhes[escolha.lower()]}")


def mover(heroi, destino):
    heroi.local = destino
    primeira_vez = destino not in heroi.visitados
    if primeira_vez:
        heroi.visitados.append(destino)
    mostrar_sala(heroi, completa=primeira_vez)


def despertar(heroi):
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
    mostrar_sala(heroi)

    while True:
        sala = SALAS[heroi.local]

        # Um item de menu para cada saída. Se você já conhece o destino, ele aparece ao lado.
        destinos, descricoes = {}, {}
        for direcao, destino in sala["saidas"].items():
            rotulo = rotulo_direcao(direcao)
            destinos[rotulo] = destino
            if destino in heroi.visitados:
                descricoes[rotulo] = SALAS[destino]["nome"]

        opcoes = list(destinos) + [EXAMINAR, OLHAR, MAPA, FICHA, SALVAR, MENU]
        print()
        escolha = escolher("O que você faz?", opcoes, descricoes, separar_antes=(EXAMINAR, MAPA))

        if escolha in destinos:
            mover(heroi, destinos[escolha])
        elif escolha == EXAMINAR:
            examinar(heroi)
        elif escolha == OLHAR:
            mostrar_sala(heroi)
        elif escolha == MAPA:
            mostrar_mapa(heroi)
        elif escolha == FICHA:
            print()
            print(heroi.ficha())
        elif escolha == SALVAR:
            arquivo = salvar(heroi)
            print(f"\nJogo salvo em {arquivo.name}.")
        elif escolha == MENU:
            arquivo = salvar(heroi)
            print(f"\nJogo salvo em {arquivo.name}. Voltando ao menu...")
            return
