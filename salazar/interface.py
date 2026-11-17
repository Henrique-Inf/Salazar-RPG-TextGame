"""Funções de entrada e saída no terminal."""


def titulo(texto):
    print()
    print("~" * 46)
    print(texto.center(46))
    print("~" * 46)


def perguntar(texto, padrao=None):
    sufixo = f" [{padrao}]" if padrao else ""
    resposta = input(f"{texto}{sufixo}: ").strip()
    return resposta or (padrao or "")


def escolher(texto, opcoes, descricoes=None):
    """Mostra um menu numerado e devolve a opção escolhida."""
    print(f"\n{texto}")
    for i, opcao in enumerate(opcoes, 1):
        extra = f" — {descricoes[opcao]}" if descricoes and opcao in descricoes else ""
        print(f"  {i}. {opcao}{extra}")
    while True:
        resposta = input("> ").strip()
        if resposta.isdigit() and 1 <= int(resposta) <= len(opcoes):
            return opcoes[int(resposta) - 1]
        print(f"Digite um número de 1 a {len(opcoes)}.")


def confirmar(texto):
    while True:
        resposta = input(f"{texto} (s/n): ").strip().lower()
        if resposta in ("s", "sim"):
            return True
        if resposta in ("n", "nao", "não"):
            return False


def pausar():
    input("\n(pressione Enter para continuar)")
