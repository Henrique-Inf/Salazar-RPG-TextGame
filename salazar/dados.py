"""Dados de regras do D&D 5e (conteúdo do SRD 5.1) usados pelo jogo."""

ATRIBUTOS = ["FOR", "DES", "CON", "INT", "SAB", "CAR"]

NOMES_ATRIBUTOS = {
    "FOR": "Força",
    "DES": "Destreza",
    "CON": "Constituição",
    "INT": "Inteligência",
    "SAB": "Sabedoria",
    "CAR": "Carisma",
}

# Bônus de atributo, deslocamento (em metros) e traços resumidos de cada raça.
RACAS = {
    "Anão": {
        "bonus": {"CON": 2, "SAB": 1},
        "deslocamento": 7.5,
        "pv_extra_por_nivel": 1,
        "tracos": ["Visão no escuro", "Resiliência anã", "Robustez anã (+1 PV por nível)"],
        "descricao": "Robusto e teimoso, forjado nas montanhas.",
    },
    "Elfo": {
        "bonus": {"DES": 2, "INT": 1},
        "deslocamento": 9,
        "tracos": ["Visão no escuro", "Ancestralidade feérica", "Transe", "Truque de mago"],
        "descricao": "Gracioso e longevo, ligado à magia antiga.",
    },
    "Halfling": {
        "bonus": {"DES": 2, "CAR": 1},
        "deslocamento": 7.5,
        "tracos": ["Sortudo", "Bravura", "Agilidade halfling", "Furtividade natural"],
        "descricao": "Pequeno, sortudo e surpreendentemente corajoso.",
    },
    "Humano": {
        "bonus": {a: 1 for a in ATRIBUTOS},
        "deslocamento": 9,
        "tracos": ["Versatilidade (+1 em todos os atributos)"],
        "descricao": "Ambicioso e adaptável, está em todo lugar.",
    },
    "Draconato": {
        "bonus": {"FOR": 2, "CAR": 1},
        "deslocamento": 9,
        "tracos": ["Ancestralidade dracônica", "Arma de sopro", "Resistência a dano"],
        "descricao": "Descendente de dragões, orgulhoso e imponente.",
    },
    "Gnomo": {
        "bonus": {"INT": 2, "CON": 1},
        "deslocamento": 7.5,
        "tracos": ["Visão no escuro", "Esperteza gnômica", "Conhecimento de artífice"],
        "descricao": "Curioso e inventivo, cheio de energia.",
    },
    "Meio-Elfo": {
        "bonus": {"CAR": 2},
        "escolhas_extras": 2,  # +1 em dois atributos à escolha (exceto CAR)
        "deslocamento": 9,
        "tracos": ["Visão no escuro", "Ancestralidade feérica", "Versatilidade em perícias"],
        "descricao": "Entre dois mundos, carismático e versátil.",
    },
    "Meio-Orc": {
        "bonus": {"FOR": 2, "CON": 1},
        "deslocamento": 9,
        "tracos": ["Visão no escuro", "Ameaçador", "Resistência implacável", "Ataques selvagens"],
        "descricao": "Forte e feroz, difícil de derrubar.",
    },
    "Tiefling": {
        "bonus": {"CAR": 2, "INT": 1},
        "deslocamento": 9,
        "tracos": ["Visão no escuro", "Resistência infernal", "Legado infernal"],
        "descricao": "Marcado por um pacto infernal antigo.",
    },
}

# dado_vida: lados do dado de vida.
# ca: (base, soma DES?, limite de DES, atributo extra, bônus de escudo)
CLASSES = {
    "Bárbaro": {
        "dado_vida": 12,
        "principal": ["FOR"],
        "salvaguardas": ["FOR", "CON"],
        "ca": (10, True, None, "CON", 0),
        "equipamento": ["Machado grande", "2 machadinhas", "Pacote de aventureiro"],
        "descricao": "Guerreiro movido pela fúria primal.",
    },
    "Bardo": {
        "dado_vida": 8,
        "principal": ["CAR"],
        "salvaguardas": ["DES", "CAR"],
        "ca": (11, True, None, None, 0),
        "equipamento": ["Rapieira", "Alaúde", "Armadura de couro", "Adaga"],
        "descricao": "Artista cuja música tece magia.",
    },
    "Bruxo": {
        "dado_vida": 8,
        "principal": ["CAR"],
        "salvaguardas": ["SAB", "CAR"],
        "ca": (11, True, None, None, 0),
        "equipamento": ["Besta leve", "Foco arcano", "Armadura de couro", "2 adagas"],
        "descricao": "Recebe poder de um pacto com um patrono.",
    },
    "Clérigo": {
        "dado_vida": 8,
        "principal": ["SAB"],
        "salvaguardas": ["SAB", "CAR"],
        "ca": (14, True, 2, None, 2),
        "equipamento": ["Maça", "Brunea", "Escudo", "Símbolo sagrado"],
        "descricao": "Campeão divino que canaliza a fé.",
    },
    "Druida": {
        "dado_vida": 8,
        "principal": ["SAB"],
        "salvaguardas": ["INT", "SAB"],
        "ca": (11, True, None, None, 2),
        "equipamento": ["Cimitarra", "Escudo de madeira", "Armadura de couro", "Foco druídico"],
        "descricao": "Guardião da natureza que muda de forma.",
    },
    "Feiticeiro": {
        "dado_vida": 6,
        "principal": ["CAR"],
        "salvaguardas": ["CON", "CAR"],
        "ca": (10, True, None, None, 0),
        "equipamento": ["Besta leve", "Foco arcano", "2 adagas"],
        "descricao": "A magia corre no seu sangue.",
    },
    "Guerreiro": {
        "dado_vida": 10,
        "principal": ["FOR", "DES"],
        "salvaguardas": ["FOR", "CON"],
        "ca": (16, False, None, None, 2),
        "equipamento": ["Cota de malha", "Espada longa", "Escudo", "Besta leve"],
        "descricao": "Mestre das armas e do combate.",
    },
    "Ladino": {
        "dado_vida": 8,
        "principal": ["DES"],
        "salvaguardas": ["DES", "INT"],
        "ca": (11, True, None, None, 0),
        "equipamento": ["Rapieira", "Arco curto", "Armadura de couro", "Ferramentas de ladrão"],
        "descricao": "Furtivo e preciso, golpeia nas sombras.",
    },
    "Mago": {
        "dado_vida": 6,
        "principal": ["INT"],
        "salvaguardas": ["INT", "SAB"],
        "ca": (10, True, None, None, 0),
        "equipamento": ["Bordão", "Grimório", "Foco arcano"],
        "descricao": "Estudioso das artes arcanas.",
    },
    "Monge": {
        "dado_vida": 8,
        "principal": ["DES", "SAB"],
        "salvaguardas": ["FOR", "DES"],
        "ca": (10, True, None, "SAB", 0),
        "equipamento": ["Espada curta", "10 dardos"],
        "descricao": "Lutador disciplinado que domina o ki.",
    },
    "Paladino": {
        "dado_vida": 10,
        "principal": ["FOR", "CAR"],
        "salvaguardas": ["SAB", "CAR"],
        "ca": (16, False, None, None, 2),
        "equipamento": ["Cota de malha", "Espada longa", "Escudo", "Símbolo sagrado"],
        "descricao": "Guerreiro sagrado preso a um juramento.",
    },
    "Patrulheiro": {
        "dado_vida": 10,
        "principal": ["DES", "SAB"],
        "salvaguardas": ["FOR", "DES"],
        "ca": (11, True, None, None, 0),
        "equipamento": ["Arco longo", "2 espadas curtas", "Armadura de couro"],
        "descricao": "Caçador e rastreador das terras selvagens.",
    },
}

ALINHAMENTOS = [
    "Leal e Bom", "Neutro e Bom", "Caótico e Bom",
    "Leal e Neutro", "Neutro", "Caótico e Neutro",
    "Leal e Mau", "Neutro e Mau", "Caótico e Mau",
]

CONJUNTO_PADRAO = [15, 14, 13, 12, 10, 8]

# Custo de compra de pontos (27 pontos, valores de 8 a 15).
CUSTO_PONTOS = {8: 0, 9: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 7, 15: 9}
PONTOS_TOTAIS = 27
