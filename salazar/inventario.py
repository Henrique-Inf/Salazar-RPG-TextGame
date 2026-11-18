"""Inventário: pegar, usar e examinar itens (a lógica, sem menus)."""

from .dados import CLASSES
from .itens import ITENS
from .mundo import obter_sala


def obter_item(heroi, item_id):
    """Devolve {"nome", "descricao"} de um item, inclusive os do equipamento inicial."""
    if item_id.startswith("kit:"):
        indice = int(item_id.split(":")[1])
        nome = CLASSES[heroi.classe]["equipamento"][indice]
        return {"nome": nome, "descricao": f"Parte do seu equipamento de {heroi.classe}."}
    return ITENS[item_id]


def nome_item(heroi, item_id):
    return obter_item(heroi, item_id)["nome"]


def itens_no_chao(heroi):
    """Ids dos itens que dá para pegar na sala atual (e que ainda não foram pegos)."""
    sala = obter_sala(heroi.local)
    ids = []
    for entrada in sala.get("itens", []):
        if isinstance(entrada, str):
            item_id, flag = entrada, None
        else:
            item_id, flag = entrada["id"], entrada.get("flag")
        if flag is None or flag in heroi.flags:
            ids.append(item_id)
    kit_flag = sala.get("kit_flag")
    if kit_flag and kit_flag in heroi.flags:
        ids += [f"kit:{i}" for i in range(len(CLASSES[heroi.classe]["equipamento"]))]
    if sala.get("reposicao"):  # sala de testes: o item some só enquanto você está com ele
        return [i for i in ids if i not in heroi.inventario]
    return [i for i in ids if i not in heroi.pegos]


def pegar(heroi, item_id):
    """Põe o item no inventário. Devolve o nome do item."""
    heroi.inventario.append(item_id)
    if not obter_sala(heroi.local).get("reposicao"):
        heroi.pegos.append(item_id)
    return nome_item(heroi, item_id)


def usar(heroi, item_id):
    """Usa um item na sala atual. Devolve o texto do que aconteceu."""
    uso = obter_sala(heroi.local).get("usos", {}).get(item_id)
    if not uso:
        return "Isso não parece servir para nada aqui."
    flag = uso.get("flag")
    if flag and flag in heroi.flags:
        return uso.get("ja", "Você já fez isso.")
    if flag:
        heroi.flags.append(flag)
    return uso["texto"]


def texto_detalhe(heroi, detalhe):
    """Texto de uma coisa examinável. Pode mudar depois de certos eventos."""
    if isinstance(detalhe, str):
        return detalhe
    texto = detalhe["texto"]
    for alternativa in detalhe.get("depois", []):
        if alternativa["flag"] in heroi.flags:
            texto = alternativa["texto"]
    return texto
