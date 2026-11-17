"""O mapa do jogo: o Convento da Nossa Senhora do Rosto Florido.

Cada sala tem:
  nome       – o título que aparece ao entrar
  andar      – "Subterrâneo" ou "Térreo"
  descricao  – o texto que aparece ao entrar pela primeira vez (ou com o comando "olhar")
  saidas     – direção → id da sala de destino
  detalhes   – coisas que podem ser examinadas com "examinar <coisa>"

Para mudar um texto do jogo, basta editar aqui. A planta original está em docs/mapa-convento.png.
O norte é o topo da folha do mapa.
"""

SALA_INICIAL = "sub_cela"

SALAS = {
    # ------------------------------------------------------------------
    # SUBTERRÂNEO
    # ------------------------------------------------------------------
    "sub_cela": {
        "nome": "Uma cela escura",
        "andar": "Subterrâneo",
        "descricao": (
            "Você está deitado sobre um catre de palha úmida. As paredes de pedra\n"
            "suam frio e o ar cheira a mofo e cera velha. A cela é maior que as\n"
            "outras, com duas camas estreitas encostadas na parede. A porta de\n"
            "grades, ao norte, está entreaberta, rangendo de leve com uma corrente\n"
            "de ar que vem de algum lugar."
        ),
        "saidas": {"norte": "sub_celas1"},
        "detalhes": {
            "catre": "A palha está amassada no formato de um corpo. O seu. Há quanto tempo você está aqui?",
            "camas": "A outra cama está vazia e coberta de poeira. Ninguém dorme nela há muito tempo.",
            "porta": "A fechadura está quebrada por dentro, como se alguém tivesse forçado a saída… ou a entrada.",
            "paredes": "Riscos na pedra contam dias. Muitos dias. Você não lembra de ter feito nenhum deles.",
        },
    },
    "sub_celas1": {
        "nome": "Corredor das celas",
        "andar": "Subterrâneo",
        "descricao": (
            "Um corredor estreito se estende para o norte, ladeado por portinhas\n"
            "de celas dos dois lados. Todas estão vazias. Algumas portas pendem\n"
            "das dobradiças. O silêncio é tão grande que você ouve a própria\n"
            "respiração."
        ),
        "saidas": {"sul": "sub_cela", "norte": "sub_celas2"},
        "detalhes": {
            "celas": "Catres, baldes, correntes presas à parede. Pertences nenhum. Quem ficava aqui não levou nada… ou não pôde levar.",
            "portas": "As trancas ficam do lado de fora. Estas celas foram feitas para prender, não para proteger.",
        },
    },
    "sub_celas2": {
        "nome": "Bloco de celas oeste",
        "andar": "Subterrâneo",
        "descricao": (
            "Um bloco maior de celas, organizado em torno de um corredor central.\n"
            "Mais portas, mais escuridão. Em algumas celas, flores secas foram\n"
            "deixadas sobre os catres, como oferendas. Ao nordeste, o corredor\n"
            "se abre para uma pequena antessala."
        ),
        "saidas": {"sul": "sub_celas1", "nordeste": "sub_antessala"},
        "detalhes": {
            "flores": "Pétalas murchas, quase pó. Alguém as colocou aqui com cuidado.",
            "celas": "Iguais às outras. Vazias, frias, esquecidas.",
        },
    },
    "sub_celas4": {
        "nome": "Bloco de celas leste",
        "andar": "Subterrâneo",
        "descricao": (
            "Outro bloco de celas, idêntico ao primeiro. Uma tocha apagada\n"
            "ainda está presa ao suporte na parede. O chão tem marcas de\n"
            "arrasto que seguem para o noroeste."
        ),
        "saidas": {"noroeste": "sub_antessala"},
        "detalhes": {
            "tocha": "Fria. O pano na ponta ainda cheira a óleo. Não faz tanto tempo assim que foi usada.",
            "marcas": "Sulcos no pó, como de algo pesado sendo puxado. Ou de alguém.",
        },
    },
    "sub_sala3": {
        "nome": "Sala redonda",
        "andar": "Subterrâneo",
        "descricao": (
            "Uma sala circular, base de uma das torres do convento. No centro, uma\n"
            "mesa de pedra com uma vela derretida até o fim. O teto some na\n"
            "escuridão lá em cima."
        ),
        "saidas": {"leste": "sub_antessala"},
        "detalhes": {
            "mesa": "Pedra lisa e fria. Há manchas de cera de muitas velas, uma por cima da outra.",
            "vela": "Queimou até o fim. Ninguém voltou para trocar.",
        },
    },
    "sub_antessala": {
        "nome": "Antessala",
        "andar": "Subterrâneo",
        "descricao": (
            "Um pequeno cômodo de passagem que liga os blocos de celas ao resto\n"
            "do subterrâneo. Há portas para o norte e para o leste, uma sala\n"
            "redonda a oeste, e os dois blocos de celas ao sul."
        ),
        "saidas": {
            "sudoeste": "sub_celas2",
            "sudeste": "sub_celas4",
            "oeste": "sub_sala3",
            "norte": "sub_deposito",
            "leste": "sub_sala7",
        },
        "detalhes": {
            "portas": "A porta do norte é de madeira grossa. A do leste tem uma pequena janela de grade.",
        },
    },
    "sub_deposito": {
        "nome": "Depósito",
        "andar": "Subterrâneo",
        "descricao": (
            "Um depósito abarrotado de móveis velhos e equipamentos: bancos,\n"
            "baús, castiçais, ferramentas. Tudo coberto por lençóis cinzentos de\n"
            "poeira. No centro, uma mesa larga ainda tem coisas em cima."
        ),
        "saidas": {"sul": "sub_antessala"},
        "detalhes": {
            "mesa": "Ferramentas de jardinagem: tesouras, pás, um regador de cobre. Estranho, aqui embaixo.",
            "baús": "Trancados. Você vai precisar de algo para abri-los.",
            "móveis": "Bancos de capela, um confessionário desmontado, armários sem portas.",
        },
    },
    "sub_sala7": {
        "nome": "Sala do guardião",
        "andar": "Subterrâneo",
        "descricao": (
            "Uma sala mobiliada: uma escrivaninha, uma cadeira, um armário e uma\n"
            "cama dobrável. Quem vigiava as celas morava aqui. Papéis se espalham\n"
            "pelo chão. Ao norte, uma passagem estreita."
        ),
        "saidas": {"oeste": "sub_antessala", "norte": "sub_passagem"},
        "detalhes": {
            "escrivaninha": "Um livro de registros aberto. A última página tem um nome riscado tantas vezes que rasgou o papel.",
            "papéis": "Listas de nomes, datas, e uma palavra repetida na margem: 'florescer'.",
            "armário": "Hábitos de freira, bem dobrados. E um molho de chaves pendurado num prego vazio. Só o prego.",
        },
    },
    "sub_passagem": {
        "nome": "Passagem estreita",
        "andar": "Subterrâneo",
        "descricao": (
            "Um corredor apertado, onde raízes atravessam as frestas das pedras.\n"
            "Pequenas flores brancas brotam delas, mesmo sem luz nenhuma. A\n"
            "passagem segue para o leste, rumo a uma sala ampla."
        ),
        "saidas": {"sul": "sub_sala7", "leste": "sub_salao9"},
        "detalhes": {
            "raízes": "Grossas como um braço. Quando você encosta, elas parecem mornas.",
            "flores": "Brancas, de pétalas finas. Viram-se devagar na sua direção. Ou foi impressão?",
        },
    },
    "sub_salao9": {
        "nome": "Salão da escada",
        "andar": "Subterrâneo",
        "descricao": (
            "Um salão circular. Rente à parede, uma escada em espiral sobe pela\n"
            "escuridão. Lá de cima vem uma luz fraca e um cheiro doce de flores."
        ),
        "saidas": {"oeste": "sub_passagem", "subir": "ter_torre5b"},
        "detalhes": {
            "escada": "Degraus de pedra gastos no meio de tanto uso. Sobem até o térreo.",
            "luz": "É luz do dia? Ou de velas? Daqui não dá para saber.",
        },
    },
    # ------------------------------------------------------------------
    # TÉRREO
    # ------------------------------------------------------------------
    "ter_torre5b": {
        "nome": "Torre do símbolo",
        "andar": "Térreo",
        "descricao": (
            "A escada termina numa torre redonda. No chão de pedra, um pentagrama\n"
            "foi desenhado com algo escuro, e pétalas de flor estão arrumadas\n"
            "nas cinco pontas. Uma passagem leva para o sul."
        ),
        "saidas": {"descer": "sub_salao9", "sul": "ter_torre5a"},
        "detalhes": {
            "pentagrama": "As linhas são precisas, feitas com paciência. O traço escuro é seco… e não é tinta.",
            "pétalas": "Frescas. Alguém as colocou aqui há pouco tempo.",
        },
    },
    "ter_torre5a": {
        "nome": "Torre leste",
        "andar": "Térreo",
        "descricao": (
            "Uma torre redonda com escada em caracol junto à parede. Por uma\n"
            "seteira entra um fio de luz cinzenta. A oeste, uma porta dá para\n"
            "um pátio."
        ),
        "saidas": {"norte": "ter_torre5b", "oeste": "ter_patio4"},
        "detalhes": {
            "seteira": "Lá fora, só neblina. Você não reconhece a paisagem.",
        },
    },
    "ter_patio4": {
        "nome": "Pátio norte",
        "andar": "Térreo",
        "descricao": (
            "Um pátio a céu aberto. O ar frio é um alívio depois do subterrâneo.\n"
            "Nos cantos, o entulho foi engolido por roseiras selvagens. Ao norte,\n"
            "uma estrutura de pedra parecida com um pequeno altar."
        ),
        "saidas": {
            "leste": "ter_torre5a",
            "noroeste": "ter_torre3a",
            "oeste": "ter_sala2",
            "sul": "ter_salao6",
        },
        "detalhes": {
            "altar": "Uma pedra lisa com um nicho vazio. Algo ficava aqui. Uma imagem, talvez.",
            "roseiras": "Espinhos longos e flores vermelhas demais. Elas cresceram por cima das pedras caídas.",
            "céu": "Nublado. Impossível dizer que horas são.",
        },
    },
    "ter_torre3a": {
        "nome": "Torre noroeste",
        "andar": "Térreo",
        "descricao": (
            "Uma torre redonda com escada em caracol. Uma corda grossa desce do\n"
            "alto e balança sozinha. Ao norte, a passagem para a torre dos sinos."
        ),
        "saidas": {"norte": "ter_torre3b", "sudeste": "ter_patio4", "sul": "ter_sala2"},
        "detalhes": {
            "corda": "Está presa a alguma coisa lá em cima. Os sinos, provavelmente.",
        },
    },
    "ter_torre3b": {
        "nome": "Torre dos sinos",
        "andar": "Térreo",
        "descricao": (
            "A base da torre dos sinos. Bem no alto, na escuridão, você vê o\n"
            "contorno de um grande sino de bronze. Pombos se agitam lá em cima."
        ),
        "saidas": {"sul": "ter_torre3a"},
        "detalhes": {
            "sino": "Enorme. Se tocasse, seria ouvido a quilômetros. Talvez seja melhor não tocar.",
        },
    },
    "ter_sala2": {
        "nome": "Pequena sala",
        "andar": "Térreo",
        "descricao": (
            "Uma sala pequena entre as torres e os pátios. Há um banco de madeira\n"
            "e ganchos na parede, como uma sala de espera ou um vestiário."
        ),
        "saidas": {"norte": "ter_torre3a", "oeste": "ter_torre1", "leste": "ter_patio4", "sul": "ter_patio7"},
        "detalhes": {
            "ganchos": "Um véu de freira continua pendurado num deles.",
            "banco": "Gasto pelo uso. Muita gente esperou aqui.",
        },
    },
    "ter_torre1": {
        "nome": "Torre oeste",
        "andar": "Térreo",
        "descricao": (
            "Uma torre redonda. No centro, um pequeno móvel de madeira com uma\n"
            "gaveta. A escada em caracol sobe junto à parede."
        ),
        "saidas": {"leste": "ter_sala2"},
        "detalhes": {
            "móvel": "A gaveta está emperrada. Algo se mexe lá dentro quando você sacode o móvel.",
        },
    },
    "ter_patio7": {
        "nome": "Pátio da fonte",
        "andar": "Térreo",
        "descricao": (
            "Um claustro a céu aberto. No centro, uma fonte redonda de pedra\n"
            "ainda tem água, escura e parada. Ao redor dela crescem flores de\n"
            "todas as cores, como se fosse primavera só aqui."
        ),
        "saidas": {"norte": "ter_sala2", "leste": "ter_salao6", "sudoeste": "ter_torre9"},
        "detalhes": {
            "fonte": "No fundo da água brilham moedas. E, no centro, a estátua de uma mulher cujo rosto é todo coberto de flores esculpidas.",
            "flores": "Nenhuma delas murchou. Nem uma folha seca.",
            "água": "Seu reflexo olha de volta. Por um segundo, você não reconhece o próprio rosto.",
        },
    },
    "ter_salao6": {
        "nome": "Grande salão",
        "andar": "Térreo",
        "descricao": (
            "Um salão enorme, com o teto alto apoiado em colunas. Os bancos foram\n"
            "empurrados contra as paredes. No canto leste, outro pentagrama,\n"
            "maior, foi desenhado no chão."
        ),
        "saidas": {"norte": "ter_patio4", "oeste": "ter_patio7", "sul": "ter_corredor8"},
        "detalhes": {
            "pentagrama": "Dentro dele há um círculo limpo de poeira, do tamanho de uma pessoa deitada.",
            "bancos": "Empurrados às pressas. Alguns estão tombados.",
            "colunas": "Esculpidas com flores que sobem até o teto.",
        },
    },
    "ter_corredor8": {
        "nome": "Corredor sul",
        "andar": "Térreo",
        "descricao": (
            "Um corredor longo que corre ao longo da muralha sul, ligando duas\n"
            "torres. Janelas estreitas deixam entrar a neblina."
        ),
        "saidas": {"norte": "ter_salao6", "oeste": "ter_torre9", "leste": "ter_torre10"},
        "detalhes": {
            "janelas": "Lá fora, uma floresta densa some na neblina. Nenhuma estrada à vista.",
        },
    },
    "ter_torre9": {
        "nome": "Torre sudoeste",
        "andar": "Térreo",
        "descricao": (
            "Uma torre redonda com escada em caracol. Uma porta pesada, trancada\n"
            "com uma barra de ferro, parece dar para fora do convento."
        ),
        "saidas": {"nordeste": "ter_patio7", "leste": "ter_corredor8"},
        "detalhes": {
            "porta": "A barra de ferro está presa por um cadeado enferrujado. Seria a saída?",
        },
    },
    "ter_torre10": {
        "nome": "Torre sudeste",
        "andar": "Térreo",
        "descricao": (
            "Uma torre redonda e vazia. O vento assobia pelas frestas. No chão,\n"
            "pegadas na poeira entram… mas nenhuma sai."
        ),
        "saidas": {"oeste": "ter_corredor8"},
        "detalhes": {
            "pegadas": "Pés descalços, pequenos. Param no meio da sala.",
        },
    },
}
