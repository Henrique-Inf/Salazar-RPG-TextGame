"""O personagem do jogador (Salazar) e suas regras de cálculo."""

import json
from dataclasses import dataclass, field, asdict
from pathlib import Path

from .dados import ATRIBUTOS, NOMES_ATRIBUTOS, RACAS, CLASSES
from .mundo import SALA_INICIAL

PASTA_SAVES = Path(__file__).resolve().parent.parent / "saves"


def modificador(valor):
    return (valor - 10) // 2


def com_sinal(n):
    return f"+{n}" if n >= 0 else str(n)


@dataclass
class Personagem:
    nome: str
    raca: str
    classe: str
    alinhamento: str
    atributos_base: dict
    bonus_escolhidos: dict = field(default_factory=dict)  # ex.: +1 do Meio-Elfo
    nivel: int = 1
    pv_atual: int = None
    local: str = SALA_INICIAL
    visitados: list = field(default_factory=list)

    def __post_init__(self):
        if self.pv_atual is None:
            self.pv_atual = self.pv_maximo

    # --- atributos -------------------------------------------------------
    @property
    def atributos(self):
        bonus_raca = RACAS[self.raca]["bonus"]
        return {
            a: self.atributos_base[a] + bonus_raca.get(a, 0) + self.bonus_escolhidos.get(a, 0)
            for a in ATRIBUTOS
        }

    def mod(self, atributo):
        return modificador(self.atributos[atributo])

    # --- valores derivados -----------------------------------------------
    @property
    def bonus_proficiencia(self):
        return 2 + (self.nivel - 1) // 4

    @property
    def pv_maximo(self):
        dado = CLASSES[self.classe]["dado_vida"]
        extra = RACAS[self.raca].get("pv_extra_por_nivel", 0)
        media = dado // 2 + 1
        pv = dado + self.mod("CON") + extra
        pv += (self.nivel - 1) * (media + self.mod("CON") + extra)
        return max(pv, 1)

    @property
    def classe_armadura(self):
        base, usa_des, limite, extra, escudo = CLASSES[self.classe]["ca"]
        ca = base + escudo
        if usa_des:
            des = self.mod("DES")
            ca += min(des, limite) if limite is not None else des
        if extra:
            ca += self.mod(extra)
        return ca

    @property
    def iniciativa(self):
        return self.mod("DES")

    @property
    def deslocamento(self):
        return RACAS[self.raca]["deslocamento"]

    def salvaguarda(self, atributo):
        bonus = self.mod(atributo)
        if atributo in CLASSES[self.classe]["salvaguardas"]:
            bonus += self.bonus_proficiencia
        return bonus

    # --- exibição --------------------------------------------------------
    def ficha(self):
        linhas = [
            "=" * 46,
            f"  {self.nome.upper()}".center(46),
            f"{self.raca} · {self.classe} · Nível {self.nivel}".center(46),
            f"{self.alinhamento}".center(46),
            "=" * 46,
            f"  PV {self.pv_atual}/{self.pv_maximo}   CA {self.classe_armadura}   "
            f"Iniciativa {com_sinal(self.iniciativa)}   Desl. {self.deslocamento:g} m",
            f"  Bônus de proficiência: {com_sinal(self.bonus_proficiencia)}",
            "-" * 46,
            "  ATRIBUTO         VALOR  MOD  SALVAGUARDA",
        ]
        for a in ATRIBUTOS:
            prof = "*" if a in CLASSES[self.classe]["salvaguardas"] else " "
            linhas.append(
                f"  {NOMES_ATRIBUTOS[a]:<15}  {self.atributos[a]:>5}  {com_sinal(self.mod(a)):>3}"
                f"  {com_sinal(self.salvaguarda(a)):>5} {prof}"
            )
        linhas += [
            "  (* = proficiente)",
            "-" * 46,
            "  Traços: " + ", ".join(RACAS[self.raca]["tracos"]),
            "  Equipamento: " + ", ".join(CLASSES[self.classe]["equipamento"]),
            "=" * 46,
        ]
        return "\n".join(linhas)

    # --- salvar / carregar -----------------------------------------------
    def salvar(self, pasta=PASTA_SAVES):
        pasta = Path(pasta)
        pasta.mkdir(parents=True, exist_ok=True)
        arquivo = pasta / f"{self.nome.lower().replace(' ', '_')}.json"
        arquivo.write_text(json.dumps(asdict(self), ensure_ascii=False, indent=2), encoding="utf-8")
        return arquivo

    @classmethod
    def carregar(cls, arquivo):
        dados = json.loads(Path(arquivo).read_text(encoding="utf-8"))
        return cls(**dados)


def listar_saves(pasta=PASTA_SAVES):
    pasta = Path(pasta)
    return sorted(pasta.glob("*.json")) if pasta.exists() else []
