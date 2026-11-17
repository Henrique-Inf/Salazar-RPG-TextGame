"""Rolagens de dados."""

import random


def rolar(lados, quantidade=1):
    """Rola `quantidade` dados de `lados` faces e devolve a lista de resultados."""
    return [random.randint(1, lados) for _ in range(quantidade)]


def rolar_atributo():
    """Rola 4d6 e descarta o menor. Devolve (total, rolagens)."""
    dados = sorted(rolar(6, 4), reverse=True)
    return sum(dados[:3]), dados
