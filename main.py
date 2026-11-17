"""Salazar — um RPG de texto no mundo de D&D 5e.

Para jogar:  python main.py
"""

from salazar.criacao import criar_personagem
from salazar.interface import titulo, escolher, pausar
from salazar.personagem import Personagem, listar_saves


def prologo(heroi):
    titulo("PRÓLOGO")
    print(
        f"A chuva cai sobre a estrada de terra quando {heroi.nome} avista as luzes\n"
        "de uma taverna à beira da floresta. Lá dentro, o calor da lareira e o\n"
        "cheiro de ensopado contrastam com os olhares desconfiados dos aldeões.\n"
        "\n"
        "Um velho de capuz ergue os olhos da caneca e diz baixinho:\n"
        f"— Você tem cara de quem procura problemas, {heroi.raca.lower()}.\n"
        "  E por aqui... problemas não faltam."
    )
    print("\n[ A aventura continua na próxima versão! ]")


def novo_jogo():
    heroi = criar_personagem()
    arquivo = heroi.salvar()
    print(f"\nJogo salvo em {arquivo.name}.")
    pausar()
    prologo(heroi)


def carregar_jogo():
    saves = listar_saves()
    if not saves:
        print("\nNenhum jogo salvo encontrado.")
        return
    nomes = [s.stem for s in saves]
    escolhido = escolher("Qual jogo carregar?", nomes)
    heroi = Personagem.carregar(saves[nomes.index(escolhido)])
    print()
    print(heroi.ficha())
    pausar()
    prologo(heroi)


def main():
    titulo("S A L A Z A R")
    print("Um RPG de texto no mundo de D&D 5e".center(46))
    while True:
        opcao = escolher("Menu principal", ["Novo jogo", "Carregar jogo", "Sair"])
        if opcao == "Novo jogo":
            novo_jogo()
        elif opcao == "Carregar jogo":
            carregar_jogo()
        else:
            print("\nAté a próxima aventura!")
            break


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nAté a próxima aventura!")
