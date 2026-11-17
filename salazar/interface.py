"""Funções de entrada e saída no terminal.

Os menus usam a biblioteca `questionary` (setas + Enter). Se ela não estiver
instalada, ou se o jogo não estiver rodando num terminal de verdade, os menus
viram listas numeradas, e o jogo continua funcionando.
"""

import os
import sys

try:
    import questionary
    from questionary import Choice, Separator, Style
except ImportError:  # pragma: no cover
    questionary = None

ESTILO = None
if questionary:
    ESTILO = Style([
        ("qmark", "fg:#d4a017 bold"),
        ("question", "bold"),
        ("pointer", "fg:#d4a017 bold"),
        ("highlighted", "fg:#d4a017 bold"),
        ("selected", "fg:#d4a017"),
        ("instruction", "fg:#888888 italic"),
        ("separator", "fg:#666666"),
        ("answer", "fg:#d4a017 bold"),
    ])


def menus_navegaveis():
    return questionary is not None and sys.stdin.isatty() and sys.stdout.isatty()


def aviso_biblioteca():
    if questionary is None:
        print("(Dica: rode 'pip install -r requirements.txt' para navegar nos menus com as setas.)")


def _resposta(valor):
    """questionary devolve None quando o jogador aperta Ctrl+C."""
    if valor is None:
        raise KeyboardInterrupt
    return valor


def limpar():
    """Limpa a tela (só num terminal de verdade, para não atrapalhar redirecionamentos)."""
    if sys.stdout.isatty():
        os.system("cls" if os.name == "nt" else "clear")


def titulo(texto):
    print()
    print("~" * 46)
    print(texto.center(46))
    print("~" * 46)


def perguntar(texto, padrao=None):
    if menus_navegaveis():
        resposta = _resposta(questionary.text(texto, default=padrao or "", qmark="›", style=ESTILO).ask())
        return resposta.strip() or (padrao or "")
    sufixo = f" [{padrao}]" if padrao else ""
    resposta = input(f"{texto}{sufixo}: ").strip()
    return resposta or (padrao or "")


def escolher(texto, opcoes, descricoes=None, separar_antes=()):
    """Mostra um menu e devolve a opção escolhida.

    opcoes:        lista de textos (o que é devolvido)
    descricoes:    dict opção → texto extra mostrado ao lado
    separar_antes: opções que ganham uma linha separadora antes delas
    """
    descricoes = descricoes or {}

    if menus_navegaveis():
        escolhas = []
        for opcao in opcoes:
            if opcao in separar_antes:
                escolhas.append(Separator("  ─────────"))
            rotulo = f"{opcao} — {descricoes[opcao]}" if opcao in descricoes else opcao
            escolhas.append(Choice(title=rotulo, value=opcao))
        return _resposta(questionary.select(
            texto,
            choices=escolhas,
            qmark="›",
            instruction=" ",
            style=ESTILO,
        ).ask())

    print(f"\n{texto}")
    for i, opcao in enumerate(opcoes, 1):
        extra = f" — {descricoes[opcao]}" if opcao in descricoes else ""
        print(f"  {i}. {opcao}{extra}")
    while True:
        resposta = input("> ").strip()
        if resposta.isdigit() and 1 <= int(resposta) <= len(opcoes):
            return opcoes[int(resposta) - 1]
        print(f"Digite um número de 1 a {len(opcoes)}.")


def confirmar(texto):
    if menus_navegaveis():
        return _resposta(questionary.select(
            texto, choices=["Sim", "Não"], qmark="›", instruction=" ", style=ESTILO
        ).ask()) == "Sim"
    while True:
        resposta = input(f"{texto} (s/n): ").strip().lower()
        if resposta in ("s", "sim"):
            return True
        if resposta in ("n", "nao", "não"):
            return False


def pausar():
    input("\n(pressione Enter para continuar)")
