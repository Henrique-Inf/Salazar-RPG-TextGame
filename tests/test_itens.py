"""Confere os itens e garante que o jogo pode ser zerado. Rode com: python -m unittest"""

import unittest

from salazar.dados import CLASSES
from salazar.inventario import itens_no_chao, nome_item, pegar, usar, texto_detalhe
from salazar.itens import ITENS
from salazar.mundo import SALAS, saidas_disponiveis
from salazar.personagem import Personagem

ATRIBUTOS = {"FOR": 15, "DES": 14, "CON": 13, "INT": 12, "SAB": 10, "CAR": 8}


def novo_heroi(classe="Guerreiro"):
    return Personagem("Teste", "Humano", classe, "Neutro", dict(ATRIBUTOS))


def ir_para(heroi, sala):
    heroi.local = sala


class TestItens(unittest.TestCase):
    def test_itens_do_mapa_existem(self):
        for sala_id, sala in SALAS.items():
            for entrada in sala.get("itens", []):
                item_id = entrada if isinstance(entrada, str) else entrada["id"]
                self.assertIn(item_id, ITENS, f"{sala_id} tem o item {item_id}, que não existe")

    def test_usos_apontam_para_itens_que_existem(self):
        for sala_id, sala in SALAS.items():
            for item_id in sala.get("usos", {}):
                self.assertIn(item_id, ITENS, f"{sala_id}: uso do item {item_id}, que não existe")

    def test_todo_item_pode_ser_encontrado(self):
        """Todo item de itens.py precisa estar em alguma sala."""
        no_mapa = set()
        for sala in SALAS.values():
            for entrada in sala.get("itens", []):
                no_mapa.add(entrada if isinstance(entrada, str) else entrada["id"])
        self.assertEqual(set(ITENS), no_mapa)

    def test_equipamento_inicial_aparece_ao_abrir_os_baus(self):
        for classe, dados in CLASSES.items():
            heroi = novo_heroi(classe)
            ir_para(heroi, "sub_deposito")
            heroi.flags.append("baus_abertos")
            nomes = [nome_item(heroi, i) for i in itens_no_chao(heroi)]
            for equipamento in dados["equipamento"]:
                self.assertIn(equipamento, nomes, classe)


class TestPartida(unittest.TestCase):
    def test_da_para_zerar_o_jogo(self):
        heroi = novo_heroi()

        # 1. a tesoura está no depósito, à vista
        ir_para(heroi, "sub_deposito")
        self.assertIn("tesoura", itens_no_chao(heroi))
        pegar(heroi, "tesoura")
        self.assertNotIn("tesoura", itens_no_chao(heroi))  # não reaparece

        # 2. os baús estão trancados e a chave ainda não apareceu
        self.assertNotIn("chave_enferrujada", itens_no_chao(heroi))

        # 3. a tesoura abre a gaveta na torre oeste, e as chaves aparecem
        ir_para(heroi, "ter_torre1")
        self.assertNotIn("chaves", itens_no_chao(heroi))
        self.assertIn("gaveta está emperrada", texto_detalhe(heroi, SALAS["ter_torre1"]["detalhes"]["móvel"]))
        usar(heroi, "tesoura")
        self.assertIn("aberta", texto_detalhe(heroi, SALAS["ter_torre1"]["detalhes"]["móvel"]))
        pegar(heroi, "chaves")

        # 4. as chaves abrem os baús; surge o equipamento e a chave do cadeado
        ir_para(heroi, "sub_deposito")
        usar(heroi, "chaves")
        chao = itens_no_chao(heroi)
        self.assertIn("chave_enferrujada", chao)
        self.assertEqual(len([i for i in chao if i.startswith("kit:")]), len(CLASSES["Guerreiro"]["equipamento"]))
        for item_id in chao:
            pegar(heroi, item_id)
        self.assertEqual(itens_no_chao(heroi), [])

        # 5. as chaves não servem no cadeado, mas a chave enferrujada serve
        ir_para(heroi, "ter_torre9")
        self.assertNotIn("fora", saidas_disponiveis(SALAS["ter_torre9"], heroi.flags))
        usar(heroi, "chaves")
        self.assertNotIn("porta_aberta", heroi.flags)
        usar(heroi, "chave_enferrujada")
        self.assertIn("porta_aberta", heroi.flags)

        # 6. a saída está liberada
        self.assertEqual(saidas_disponiveis(SALAS["ter_torre9"], heroi.flags)["fora"], "ext_estrada")

    def test_item_sem_uso_na_sala_nao_faz_nada(self):
        heroi = novo_heroi()
        ir_para(heroi, "sub_cela")
        self.assertIn("não parece servir", usar(heroi, "tesoura"))
        self.assertEqual(heroi.flags, [])

    def test_usar_duas_vezes_nao_repete(self):
        heroi = novo_heroi()
        ir_para(heroi, "ter_torre1")
        usar(heroi, "tesoura")
        self.assertEqual(usar(heroi, "tesoura"), "A gaveta já está aberta.")
        self.assertEqual(heroi.flags.count("gaveta_aberta"), 1)

    def test_save_guarda_inventario_e_eventos(self):
        import tempfile
        heroi = novo_heroi()
        pegar(heroi, "tesoura")
        heroi.flags.append("gaveta_aberta")
        with tempfile.TemporaryDirectory() as pasta:
            carregado = Personagem.carregar(heroi.salvar(pasta))
        self.assertEqual(carregado.inventario, ["tesoura"])
        self.assertEqual(carregado.pegos, ["tesoura"])
        self.assertEqual(carregado.flags, ["gaveta_aberta"])

    def test_save_antigo_sem_inventario_ainda_carrega(self):
        import json, tempfile, pathlib
        antigo = {"nome": "Velho", "raca": "Anão", "classe": "Mago", "alinhamento": "Neutro",
                  "atributos_base": ATRIBUTOS, "bonus_escolhidos": {}, "nivel": 1, "pv_atual": 6,
                  "local": "sub_cela", "visitados": ["sub_cela"]}
        with tempfile.TemporaryDirectory() as pasta:
            arquivo = pathlib.Path(pasta) / "velho.json"
            arquivo.write_text(json.dumps(antigo), encoding="utf-8")
            heroi = Personagem.carregar(arquivo)
        self.assertEqual(heroi.inventario, [])
        self.assertEqual(heroi.flags, [])


if __name__ == "__main__":
    unittest.main()
