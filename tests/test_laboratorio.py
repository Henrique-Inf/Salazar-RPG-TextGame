"""Testes da sala de testes. Rode com: python -m unittest"""

import unittest

from salazar.dados import CLASSES, RACAS
from salazar.ferramentas_teste import (
    ANDARES, curar, esvaziar_inventario, personagem_de_teste, reiniciar,
)
from salazar.inventario import itens_no_chao, pegar, usar
from salazar.itens import ITENS
from salazar.laboratorio import SALA_LAB_ID, SALAS_LAB
from salazar.mundo import SALAS, obter_sala, todas_as_flags


class TestPersonagemDeTeste(unittest.TestCase):
    def test_todas_as_combinacoes_de_raca_e_classe(self):
        for raca in RACAS:
            for classe in CLASSES:
                heroi = personagem_de_teste(raca, classe)
                self.assertGreaterEqual(heroi.pv_maximo, 1, (raca, classe))
                self.assertEqual(heroi.local, SALA_LAB_ID)
                self.assertTrue(heroi.modo_teste)
                self.assertEqual(len(heroi.bonus_escolhidos), RACAS[raca].get("escolhas_extras", 0))

    def test_atributo_principal_recebe_o_melhor_valor(self):
        heroi = personagem_de_teste("Humano", "Mago")
        self.assertEqual(heroi.atributos_base["INT"], 15)

    def test_modo_de_teste_nao_vai_para_o_save(self):
        import json, tempfile
        heroi = personagem_de_teste("Anão", "Clérigo")
        with tempfile.TemporaryDirectory() as pasta:
            arquivo = heroi.salvar(pasta)
            self.assertNotIn("modo_teste", json.loads(arquivo.read_text(encoding="utf-8")))


class TestSalaDeTestes(unittest.TestCase):
    def test_itens_da_sala_existem(self):
        for entrada in SALAS_LAB[SALA_LAB_ID]["itens"]:
            item_id = entrada if isinstance(entrada, str) else entrada["id"]
            self.assertIn(item_id, ITENS)

    def test_todos_os_itens_do_jogo_estao_na_sala(self):
        ids = {e if isinstance(e, str) else e["id"] for e in SALAS_LAB[SALA_LAB_ID]["itens"]}
        self.assertEqual(ids, set(ITENS))

    def test_itens_do_chao_nao_acabam(self):
        heroi = personagem_de_teste("Humano", "Guerreiro")
        self.assertIn("tesoura", itens_no_chao(heroi))
        pegar(heroi, "tesoura")
        self.assertNotIn("tesoura", itens_no_chao(heroi))  # você já está com ele
        esvaziar_inventario(heroi)
        self.assertIn("tesoura", itens_no_chao(heroi))     # e ele volta

    def test_pegar_na_sala_de_testes_nao_estraga_o_convento(self):
        heroi = personagem_de_teste("Humano", "Guerreiro")
        pegar(heroi, "tesoura")
        self.assertEqual(heroi.pegos, [])
        heroi.local = "sub_deposito"
        self.assertIn("tesoura", itens_no_chao(heroi))

    def test_bau_de_teste(self):
        heroi = personagem_de_teste("Humano", "Guerreiro")
        self.assertNotIn("chave_enferrujada", itens_no_chao(heroi))
        usar(heroi, "chaves")
        chao = itens_no_chao(heroi)
        self.assertIn("chave_enferrujada", chao)
        self.assertEqual(len([i for i in chao if i.startswith("kit:")]), len(CLASSES["Guerreiro"]["equipamento"]))

    def test_curar_e_reiniciar(self):
        heroi = personagem_de_teste("Anão", "Bárbaro")
        heroi.pv_atual = 1
        curar(heroi)
        self.assertEqual(heroi.pv_atual, heroi.pv_maximo)
        pegar(heroi, "chaves")
        usar(heroi, "chaves")
        heroi.local = "ter_torre9"
        reiniciar(heroi)
        self.assertEqual((heroi.inventario, heroi.flags, heroi.local), ([], [], SALA_LAB_ID))

    def test_ferramenta_de_teletransporte_tem_salas_em_todos_os_andares(self):
        andares_com_sala = {s["andar"] for s in list(SALAS.values()) + list(SALAS_LAB.values())}
        self.assertEqual(andares_com_sala, set(ANDARES))


class TestMundo(unittest.TestCase):
    def test_obter_sala(self):
        self.assertEqual(obter_sala("sub_cela")["nome"], SALAS["sub_cela"]["nome"])
        self.assertEqual(obter_sala(SALA_LAB_ID)["nome"], "Sala de testes")
        with self.assertRaises(KeyError):
            obter_sala("nao_existe")

    def test_todas_as_flags(self):
        for flag in ("gaveta_aberta", "baus_abertos", "porta_aberta", "lab_bau"):
            self.assertIn(flag, todas_as_flags())

    def test_sala_de_testes_nao_aparece_no_convento(self):
        self.assertNotIn(SALA_LAB_ID, SALAS)


if __name__ == "__main__":
    unittest.main()
