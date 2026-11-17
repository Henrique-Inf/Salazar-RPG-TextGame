# Salazar — RPG de Texto

Um RPG de texto em Python ambientado num mundo de fantasia medieval com as regras de **D&D 5ª edição**.
Você controla **Salazar**, um herói totalmente personalizável: escolha o nome, a raça, a classe, os atributos e o alinhamento.

## Como jogar

Precisa apenas do [Python 3.9+](https://www.python.org/downloads/) (nenhuma biblioteca extra).

```bash
git clone https://github.com/Henrique-Inf/Salazar-RPG-TextGame.git
cd Salazar-RPG-TextGame
python main.py
```

## O que já existe

- Criação de personagem completa
  - 9 raças: Anão, Elfo, Halfling, Humano, Draconato, Gnomo, Meio-Elfo, Meio-Orc e Tiefling
  - 12 classes: Bárbaro, Bardo, Bruxo, Clérigo, Druida, Feiticeiro, Guerreiro, Ladino, Mago, Monge, Paladino e Patrulheiro
  - 3 formas de definir atributos: conjunto padrão, rolagem 4d6 e compra de pontos
  - Alinhamento
- Ficha calculada automaticamente: PV, CA, iniciativa, modificadores e salvaguardas
- Salvar e carregar o jogo (arquivos em `saves/`), incluindo onde você está
- Exploração do **Convento da Nossa Senhora do Rosto Florido**: 21 salas em dois andares (subterrâneo e térreo)

## Comandos de exploração

| Comando | O que faz |
|---|---|
| `norte`, `sul`, `leste`, `oeste` (ou `n`, `s`, `l`, `o`) | andar |
| `nordeste`, `noroeste`, `sudeste`, `sudoeste` (ou `ne`, `no`, `se`, `so`) | diagonais |
| `subir`, `descer` | usar escadas |
| `olhar` | descrever o lugar de novo |
| `examinar <coisa>` | olhar algo de perto (ex.: `examinar porta`) |
| `mapa` | lugares que você já visitou |
| `ficha` | ver sua ficha |
| `salvar` | salvar o jogo |
| `ajuda` | lista de comandos |
| `menu` | salvar e voltar ao menu |

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
salazar/
  mundo.py              # o convento: salas, saídas e descrições
  exploracao.py         # comandos de exploração e prólogo
  dados.py              # raças, classes e tabelas de regras
  dados_rolagem.py      # rolagem de dados
  personagem.py         # ficha do personagem, cálculos, salvar/carregar
  criacao.py            # criação de personagem passo a passo
  interface.py          # menus e entradas no terminal
tests/                  # testes automáticos (python -m unittest)
docs/                   # planta do convento
```

## Licença das regras

Este jogo usa conteúdo do System Reference Document 5.1 ("SRD 5.1") da Wizards of the Coast LLC,
disponível em https://dnd.wizards.com/resources/systems-reference-document e licenciado sob a
Creative Commons Attribution 4.0 International License (https://creativecommons.org/licenses/by/4.0/legalcode).
