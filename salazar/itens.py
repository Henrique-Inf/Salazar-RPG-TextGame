"""Itens do jogo.

Cada item tem um nome e uma descrição (mostrada ao examinar no inventário).
O equipamento inicial da classe não fica aqui: ele é gerado a partir de
`CLASSES[classe]["equipamento"]` em dados.py (ids "kit:0", "kit:1"...).
"""

ITENS = {
    "tesoura": {
        "nome": "Tesoura de poda",
        "descricao": "Lâmina longa e enferrujada, cabo de madeira gasto. Serve para podar rosas… ou para forçar uma fresta.",
    },
    "chaves": {
        "nome": "Molho de chaves",
        "descricao": "Várias chaves de ferro presas a um aro. Uma etiqueta de couro diz: 'Ir. Margarida — celas e depósito'.",
    },
    "chave_enferrujada": {
        "nome": "Chave enferrujada",
        "descricao": "Pequena, pesada e coberta de ferrugem. Tem o tamanho certo para um cadeado velho.",
    },
    "livro_registros": {
        "nome": "Livro de registros",
        "descricao": "Capa de couro rachada. As páginas listam nomes e datas, linha após linha. Na última, há um nome riscado tantas vezes que o papel rasgou: impossível ler.",
    },
    "petala": {
        "nome": "Pétala fresca",
        "descricao": "Branca e macia, como se tivesse sido colhida agora há pouco. Cheira a algo doce demais.",
    },
    "veu": {
        "nome": "Véu de freira",
        "descricao": "Tecido preto, bem dobrado e com cheiro de incenso velho. Há um nome bordado na barra, desbotado demais para ler.",
    },
    "moedas": {
        "nome": "Moedas antigas",
        "descricao": "Um punhado de moedas de cobre cobertas de limo, tiradas do fundo da fonte. A cunhagem é de um reino que você não reconhece.",
    },
}
