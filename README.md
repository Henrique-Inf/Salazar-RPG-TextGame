# Salazar — RPG de Texto

Um RPG de texto em Python ambientado num mundo de fantasia medieval com as regras de **D&D 5ª edição**.
Você controla **Salazar**, um herói totalmente personalizável: escolha o nome, a raça, a classe, os atributos e o alinhamento.

## Como jogar

Precisa do [Python 3.9+](https://www.python.org/downloads/).

```bash
git clone https://github.com/Henrique-Inf/Salazar-RPG-TextGame.git
cd Salazar-RPG-TextGame
pip install -r requirements.txt
python main.py
```

Os menus são navegados com **↑ ↓** e **Enter** (biblioteca [questionary](https://github.com/tmbo/questionary)).
Sem ela, ou fora de um terminal de verdade, o jogo usa listas numeradas e continua funcionando.

## O que já existe

- Criação de personagem completa
  - 9 raças: Anão, Elfo, Halfling, Humano, Draconato, Gnomo, Meio-Elfo, Meio-Orc e Tiefling
  - 12 classes: Bárbaro, Bardo, Bruxo, Clérigo, Druida, Feiticeiro, Guerreiro, Ladino, Mago, Monge, Paladino e Patrulheiro
  - 3 formas de definir atributos: conjunto padrão, rolagem 4d6 e compra de pontos
  - Alinhamento
- Ficha calculada automaticamente: PV, CA, iniciativa, modificadores e salvaguardas
- Salvar e carregar o jogo (arquivos em `saves/`), incluindo onde você está
- Exploração do **Convento da Nossa Senhora do Rosto Florido**: 21 salas em dois andares (subterrâneo e térreo)

## Como explorar

A tela é limpa a cada passo: no topo fica o seu personagem (nome, raça, classe e PV), depois a descrição da sala, o resultado da última ação e o menu. Você escolhe uma ação:

- **Ir para o norte / sul / leste / oeste…**: as saídas da sala (e as escadas, com *Subir* e *Descer*). Salas que você já visitou mostram o nome ao lado.
- **Examinar…**: abre uma lista com as coisas da sala que dá para olhar de perto
- **Mapa**: lugares que você já visitou
- **Ficha do personagem**
- **Salvar jogo** / **Salvar e voltar ao menu**

## O mapa

![Planta do convento](docs/mapa-convento.png)

Os textos de todas as salas ficam em `salazar/mundo.py`: para mudar uma descrição, é só editar lá.
Depois de mexer no mapa, rode `python -m unittest` para conferir se toda saída tem volta e se todas as salas são alcançáveis.

## Próximos passos

- [x] Exploração: locais, movimento e descrições
- [ ] Combate por turnos com rolagens de ataque e dano
- [ ] Inventário e itens
- [ ] Experiência e subida de nível
- [ ] Missões, diálogos e escolhas

## Estrutura

```
main.py                 # menu principal
requirements.txt        # dependências (questionary)
salazar/
  mundo.py              # o convento: salas, saídas e descrições
  exploracao.py         # menu de exploração e prólogo
  dados.py              # raças, classes e tabelas de regras
  dados_rolagem.py      # rolagem de dados
  personagem.py         # ficha do personagem, cálculos, salvar/carregar
  criacao.py            # criação de personagem passo a passo
  interface.py          # menus navegáveis (setas) e entradas no terminal
tests/                  # testes automáticos (python -m unittest)
docs/                   # planta do convento
```

## Licença das regras

Este jogo usa conteúdo do System Reference Document 5.1 ("SRD 5.1") da Wizards of the Coast LLC,
disponível em https://dnd.wizards.com/resources/systems-reference-document e licenciado sob a
Creative Commons Attribution 4.0 International License (https://creativecommons.org/licenses/by/4.0/legalcode).
