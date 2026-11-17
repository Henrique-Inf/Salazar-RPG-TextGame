"""Exploração: o jogador digita comandos para andar e examinar as coisas."""

import unicodedata

from .mundo import SALAS
from .interface import titulo

DIRECOES = {
    "n": "norte", "norte": "norte",
    "s": "sul", "sul": "sul",
    "l": "leste", "leste": "leste", "e": "leste",
    "o": "oeste", "oeste": "oeste", "w": "oeste",
    "ne": "nordeste", "nordeste": "nordeste",
    "no": "noroeste", "noroeste": "noroeste",
    "se": "sudeste", "sudeste": "sudeste",
    "so": "sudoeste", "sudoeste": "sudoeste",
    "sobe": "subir", "subir": "subir", "cima": "subir",
    "desce": "descer", "descer": "descer", "baixo": "descer",
}

AJUDA = """
Comandos:
  norte, sul, leste, oeste    andar (ou só n, s, l, o)
  nordeste, noroeste...       diagonais (ne, no, se, so)
  subir, descer               usar escadas
  olhar                       descrever o lugar de novo
  examinar <coisa>            olhar algo de perto (ex.: examinar porta)
  mapa                        lugares que você já visitou
  ficha                       ver sua ficha de personagem
  salvar                      salvar o jogo
  ajuda                       mostrar esta lista
  menu                        voltar ao menu principal
""".rstrip()

PALAVRAS_IGNORADAS = {"ir", "va", "vai", "para", "pra", "o", "a", "os", "as", "de", "do", "da", "no", "na"}


def normalizar(texto):
    """Minúsculas e sem acentos, para aceitar 'examinar baús' e 'examinar baus'."""
    texto = unicodedata.normalize("NFD", texto.lower().strip())
    return "".join(c for c in texto if unicodedata.category(c) != "Mn")


def mostrar_sala(heroi, completa=True):
    sala = SALAS[heroi.local]
    print()
    print(f"== {sala['nome']} ==  ({sala['andar']})")
    if completa:
        print(sala["descricao"])
    saidas = ", ".join(sala["saidas"])
    print(f"Saídas: {saidas}")


def mostrar_mapa(heroi):
    print("\nLugares que você já conhece:")
    for andar in ("Subterrâneo", "Térreo"):
        salas = [SALAS[s] for s in heroi.visitados if SALAS[s]["andar"] == andar]
        if not salas:
            continue
        print(f"  {andar}:")
        for s in salas:
            marca = "  <- você está aqui" if s is SALAS[heroi.local] else ""
            print(f"    - {s['nome']}{marca}")


def examinar(heroi, alvo):
    detalhes = SALAS[heroi.local].get("detalhes", {})
    alvo = normalizar(alvo)
    for chave, texto in detalhes.items():
        chave_n = normalizar(chave)
        # aceita singular/plural simples: "flor" acha "flores", "cama" acha "camas"
        if alvo and (alvo == chave_n or chave_n.startswith(alvo) or alvo.startswith(chave_n)):
            print(f"\n{texto}")
            return
    if alvo:
        print("\nVocê não vê nada de especial nisso.")
    else:
        coisas = ", ".join(detalhes) or "nada em especial"
        print(f"\nExaminar o quê? Aqui você vê: {coisas}.")


def mover(heroi, direcao):
    sala = SALAS[heroi.local]
    destino = sala["saidas"].get(direcao)
    if not destino:
        print("\nNão dá para ir por aí.")
        return
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
    print("\n(Digite 'ajuda' para ver os comandos.)")


def explorar(heroi, salvar):
    """Laço principal de exploração. `salvar` é uma função que grava o jogo."""
    if heroi.local not in heroi.visitados:
        heroi.visitados.append(heroi.local)
    mostrar_sala(heroi)

    while True:
        try:
            entrada = input("\n> ")
        except EOFError:
            return
        palavras = [p for p in normalizar(entrada).split() if p]
        if not palavras:
            continue

        comando, resto = palavras[0], palavras[1:]

        if comando in ("ir", "andar", "va", "vai") and resto:
            resto = [p for p in resto if p not in PALAVRAS_IGNORADAS] or resto
            comando, resto = resto[0], resto[1:]

        if comando in DIRECOES:
            mover(heroi, DIRECOES[comando])
        elif comando in ("olhar", "ol", "olha", "look"):
            mostrar_sala(heroi)
        elif comando in ("examinar", "ex", "x", "ver", "investigar"):
            alvo = " ".join(p for p in resto if p not in PALAVRAS_IGNORADAS)
            examinar(heroi, alvo)
        elif comando == "mapa":
            mostrar_mapa(heroi)
        elif comando == "ficha":
            print()
            print(heroi.ficha())
        elif comando == "salvar":
            arquivo = salvar(heroi)
            print(f"\nJogo salvo em {arquivo.name}.")
        elif comando in ("ajuda", "help", "?"):
            print(AJUDA)
        elif comando in ("menu", "sair"):
            arquivo = salvar(heroi)
            print(f"\nJogo salvo em {arquivo.name}. Voltando ao menu...")
            return
        else:
            print("\nNão entendi. Digite 'ajuda' para ver os comandos.")
