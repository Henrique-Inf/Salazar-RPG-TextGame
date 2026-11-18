"""Confere se o mapa do convento é consistente. Rode com: python -m unittest"""

import unittest
from collections import deque

from salazar.mundo import SALAS, SALA_INICIAL, todas_as_saidas

OPOSTOS = {
    "norte": "sul", "sul": "norte", "leste": "oeste", "oeste": "leste",
    "nordeste": "sudoeste", "sudoeste": "nordeste",
    "noroeste": "sudeste", "sudeste": "noroeste",
    "subir": "descer", "descer": "subir",
    "fora": "dentro", "dentro": "fora",
}


class TestMundo(unittest.TestCase):
    def test_saidas_levam_a_salas_que_existem(self):
        for sala_id, sala in SALAS.items():
            for direcao, destino in todas_as_saidas(sala).items():
                self.assertIn(destino, SALAS, f"{sala_id} -> {direcao} -> {destino}")

    def test_saidas_tem_volta(self):
        for sala_id, sala in SALAS.items():
            for direcao, destino in todas_as_saidas(sala).items():
                volta = todas_as_saidas(SALAS[destino]).get(OPOSTOS[direcao])
                self.assertEqual(volta, sala_id, f"{sala_id} -{direcao}-> {destino} não tem volta")

    def test_todas_as_salas_sao_alcancaveis(self):
        vistas, fila = {SALA_INICIAL}, deque([SALA_INICIAL])
        while fila:
            for destino in todas_as_saidas(SALAS[fila.popleft()]).values():
                if destino not in vistas:
                    vistas.add(destino)
                    fila.append(destino)
        self.assertEqual(vistas, set(SALAS))


if __name__ == "__main__":
    unittest.main()
