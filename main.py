"""Salazar — um RPG de texto no mundo de D&D 5e.

Para jogar:  python main.py
"""

from salazar.criacao import criar_personagem
from salazar.exploracao import despertar, explorar
from salazar.interface import limpar, titulo, escolher, pausar, aviso_biblioteca
from salazar.personagem import Personagem, listar_saves


def salvar(heroi):
    return heroi.salvar()


def novo_jogo():
    heroi = criar_personagem()
    arquivo = salvar(heroi)
    print(f"\nJogo salvo em {arquivo.name}.")
    pausar()
    despertar(heroi)
    pausar()
    explorar(heroi, salvar)


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
    explorar(heroi, salvar)


def main():
    while True:
        limpar()
        titulo("S A L A Z A R")
        print("Um RPG de texto no mundo de D&D 5e".center(46))
        aviso_biblioteca()
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
