"""A sala de testes: um lugar à parte onde as novidades são experimentadas.

Ela usa exatamente o mesmo formato das salas do convento (veja o comentário no
topo de mundo.py), então tudo o que funciona aqui funciona no jogo de verdade.
Quando uma ideia estiver boa, é só copiar o que for preciso para o mapa oficial.

Particularidades desta sala:
  reposicao – os itens do chão nunca acabam: se você já está com um item no
              inventário ele some da lista, e se você o perde, ele volta.
"""

from .itens import ITENS

SALA_LAB_ID = "lab"

SALAS_LAB = {
    SALA_LAB_ID: {
        "nome": "Sala de testes",
        "andar": "Laboratório",
        "descricao": (
            "Uma sala branca, sem janelas e sem portas, com bancadas de madeira ao\n"
            "longo das paredes. É aqui que as novas ideias do jogo são testadas antes\n"
            "de irem para o convento. Nada do que você fizer aqui é salvo.\n"
            "\n"
            "Todos os itens do jogo estão espalhados pelo chão. Use as ferramentas\n"
            "de teste para dar itens, mexer nos eventos, curar, mudar de nível ou ir\n"
            "para qualquer sala do convento."
        ),
        "saidas": {},
        "reposicao": True,
        # Todos os itens ficam à mostra, menos a chave do baú de teste, que sai de lá.
        "itens": [i for i in ITENS if i != "chave_enferrujada"]
        + [{"id": "chave_enferrujada", "flag": "lab_bau"}],
        "kit_flag": "lab_bau",
        "usos": {
            "chaves": {
                "texto": (
                    "A chave gira e o baú de teste se abre. Dentro estão o equipamento\n"
                    "inicial da sua classe e uma chave enferrujada."
                ),
                "flag": "lab_bau",
                "ja": "O baú de teste já está aberto.",
            },
        },
        "detalhes": {
            "bancadas": "Cada bancada guarda um tipo de teste. Por enquanto, só itens e inventário. Em breve: combate.",
            "baú de teste": {
                "texto": "Um baú trancado. Serve para testar um item que só aparece depois de um evento. Tente usar o molho de chaves.",
                "depois": [{"flag": "lab_bau", "texto": "O baú está aberto e vazio."}],
            },
            "quadro": "Uma lista do que já dá para testar: itens, inventário, eventos, níveis e teletransporte.",
        },
    },
}
