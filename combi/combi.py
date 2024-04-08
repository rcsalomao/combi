from __future__ import annotations
from typing import List
import itertools
from enum import Enum, auto


class CPSeparadoType(Enum):
    PESO_PROPRIO_ESTRUTURA_METALICA = auto()
    PESO_PROPRIO_ESTRUTURA_PRE_MOLDADA = auto()
    PESO_PROPRIO_ESTRUTURA_MOLDADA_NO_LOCAL = auto()
    ELEMENTOS_CONSTRUTIVOS_INDUSTRIALIZADOS = auto()
    ELEMENTOS_CONSTRUTIVOS_INDUSTRIALIZADOS_COM_ADICOES_IN_LOCO = auto()
    ELEMENTOS_CONSTRUTIVOS_EM_GERAL_E_EQUIPAMENTOS = auto()
    EFEITOS_DE_RECALQUES_DE_APOIO = auto()
    EFEITOS_DE_RETRACAO_DOS_MATERIAIS = auto()


class CPAgrupadoType(Enum):
    GRANDES_PONTES = auto()
    EDIFICACOES_TIPO_1 = auto()
    EDIFICACOES_TIPO_2 = auto()
    EFEITOS_DE_RECALQUES_DE_APOIO = auto()
    EFEITOS_DE_RETRACAO_DOS_MATERIAIS = auto()


class CargaPermanente(object):
    gamma_g = {
        "separado": {
            "normal": {
                CPSeparadoType.PESO_PROPRIO_ESTRUTURA_METALICA: 1.25,
                CPSeparadoType.PESO_PROPRIO_ESTRUTURA_PRE_MOLDADA: 1.3,
                CPSeparadoType.PESO_PROPRIO_ESTRUTURA_MOLDADA_NO_LOCAL: 1.35,
                CPSeparadoType.ELEMENTOS_CONSTRUTIVOS_INDUSTRIALIZADOS: 1.35,
                CPSeparadoType.ELEMENTOS_CONSTRUTIVOS_INDUSTRIALIZADOS_COM_ADICOES_IN_LOCO: 1.4,
                CPSeparadoType.ELEMENTOS_CONSTRUTIVOS_EM_GERAL_E_EQUIPAMENTOS: 1.5,
                CPSeparadoType.EFEITOS_DE_RECALQUES_DE_APOIO: 1.2,
                CPSeparadoType.EFEITOS_DE_RETRACAO_DOS_MATERIAIS: 1.2,
            },
            "especial": {
                CPSeparadoType.PESO_PROPRIO_ESTRUTURA_METALICA: 1.15,
                CPSeparadoType.PESO_PROPRIO_ESTRUTURA_PRE_MOLDADA: 1.2,
                CPSeparadoType.PESO_PROPRIO_ESTRUTURA_MOLDADA_NO_LOCAL: 1.25,
                CPSeparadoType.ELEMENTOS_CONSTRUTIVOS_INDUSTRIALIZADOS: 1.25,
                CPSeparadoType.ELEMENTOS_CONSTRUTIVOS_INDUSTRIALIZADOS_COM_ADICOES_IN_LOCO: 1.3,
                CPSeparadoType.ELEMENTOS_CONSTRUTIVOS_EM_GERAL_E_EQUIPAMENTOS: 1.4,
                CPSeparadoType.EFEITOS_DE_RECALQUES_DE_APOIO: 1.2,
                CPSeparadoType.EFEITOS_DE_RETRACAO_DOS_MATERIAIS: 1.2,
            },
            "excepcional": {
                CPSeparadoType.PESO_PROPRIO_ESTRUTURA_METALICA: 1.1,
                CPSeparadoType.PESO_PROPRIO_ESTRUTURA_PRE_MOLDADA: 1.15,
                CPSeparadoType.PESO_PROPRIO_ESTRUTURA_MOLDADA_NO_LOCAL: 1.15,
                CPSeparadoType.ELEMENTOS_CONSTRUTIVOS_INDUSTRIALIZADOS: 1.15,
                CPSeparadoType.ELEMENTOS_CONSTRUTIVOS_INDUSTRIALIZADOS_COM_ADICOES_IN_LOCO: 1.2,
                CPSeparadoType.ELEMENTOS_CONSTRUTIVOS_EM_GERAL_E_EQUIPAMENTOS: 1.3,
                CPSeparadoType.EFEITOS_DE_RECALQUES_DE_APOIO: 0.0,
                CPSeparadoType.EFEITOS_DE_RETRACAO_DOS_MATERIAIS: 0.0,
            },
        },
        "agrupado": {
            "normal": {
                CPAgrupadoType.GRANDES_PONTES: 1.3,
                CPAgrupadoType.EDIFICACOES_TIPO_1: 1.35,
                CPAgrupadoType.EDIFICACOES_TIPO_2: 1.4,
                CPAgrupadoType.EFEITOS_DE_RECALQUES_DE_APOIO: 1.2,
                CPAgrupadoType.EFEITOS_DE_RETRACAO_DOS_MATERIAIS: 1.2,
            },
            "especial": {
                CPAgrupadoType.GRANDES_PONTES: 1.2,
                CPAgrupadoType.EDIFICACOES_TIPO_1: 1.25,
                CPAgrupadoType.EDIFICACOES_TIPO_2: 1.3,
                CPAgrupadoType.EFEITOS_DE_RECALQUES_DE_APOIO: 1.2,
                CPAgrupadoType.EFEITOS_DE_RETRACAO_DOS_MATERIAIS: 1.2,
            },
            "excepcional": {
                CPAgrupadoType.GRANDES_PONTES: 1.1,
                CPAgrupadoType.EDIFICACOES_TIPO_1: 1.15,
                CPAgrupadoType.EDIFICACOES_TIPO_2: 1.2,
                CPAgrupadoType.EFEITOS_DE_RECALQUES_DE_APOIO: 0.0,
                CPAgrupadoType.EFEITOS_DE_RETRACAO_DOS_MATERIAIS: 0.0,
            },
        },
    }

    def __init__(
        self, label: str, tipo_carga: CPSeparadoType | CPAgrupadoType, valor: float
    ):
        self.label = label
        self.tipo_carga = tipo_carga
        self.valor = valor
        if isinstance(tipo_carga, CPSeparadoType):
            self.separado_ou_agrupado = "separado"
        elif isinstance(tipo_carga, CPAgrupadoType):
            self.separado_ou_agrupado = "agrupado"
        else:
            raise Exception()

    def get_gamma(self, tipo_combinacao, favoravel=False):
        if favoravel:
            if self.tipo_carga in [
                CPSeparadoType.EFEITOS_DE_RECALQUES_DE_APOIO,
                CPSeparadoType.EFEITOS_DE_RETRACAO_DOS_MATERIAIS,
                CPAgrupadoType.EFEITOS_DE_RECALQUES_DE_APOIO,
                CPAgrupadoType.EFEITOS_DE_RETRACAO_DOS_MATERIAIS,
            ]:
                return 0.0
            else:
                return 1.0
        else:
            return self.gamma_g[self.separado_ou_agrupado][tipo_combinacao][
                self.tipo_carga
            ]


class CASeparadoType(Enum):
    ACOES_TRUNCADAS = auto()
    TEMPERATURA = auto()
    VENTO = auto()
    ACOES_VARIAVEIS_EM_GERAL = auto()


class CAAgrupadoType(Enum):
    PONTES_E_EDIFICACOES_TIPO_1 = auto()
    EDIFICACOES_TIPO_2 = auto()
    ESTRUTURAS_EM_GERAL = auto()


class CACoefReducaoType(Enum):
    EDIFICACOES_DE_ACESSO_RESTRITO = auto()
    EDIFICACOES_DE_ACESSO_PUBLICO = auto()
    BIBLIOTECAS_ARQUIVOS_DEPOSITOS_OFICINAS_E_GARAGENS = auto()
    VENTO = auto()
    TEMPERATURA = auto()
    PASSARELAS_DE_PEDESTRES = auto()
    PONTES_RODOVIARIAS = auto()
    PONTES_FERROVIARIAS_NAO_ESPECIALIZADAS = auto()
    PONTES_FERROVIARIAS_ESPECIALIZADAS = auto()
    VIGAS_DE_ROLAMENTOS_DE_PONTES_ROLANTES = auto()


class CargaAcidental(object):
    gamma_q = {
        "separado": {
            "normal": {
                CASeparadoType.ACOES_TRUNCADAS: 1.2,
                CASeparadoType.TEMPERATURA: 1.2,
                CASeparadoType.VENTO: 1.4,
                CASeparadoType.ACOES_VARIAVEIS_EM_GERAL: 1.5,
            },
            "especial": {
                CASeparadoType.ACOES_TRUNCADAS: 1.1,
                CASeparadoType.TEMPERATURA: 1.0,
                CASeparadoType.VENTO: 1.2,
                CASeparadoType.ACOES_VARIAVEIS_EM_GERAL: 1.3,
            },
            "excepcional": {
                CASeparadoType.ACOES_VARIAVEIS_EM_GERAL: 1.0,
            },
        },
        "agrupado": {
            "normal": {
                CAAgrupadoType.PONTES_E_EDIFICACOES_TIPO_1: 1.5,
                CAAgrupadoType.EDIFICACOES_TIPO_2: 1.4,
            },
            "especial": {
                CAAgrupadoType.PONTES_E_EDIFICACOES_TIPO_1: 1.3,
                CAAgrupadoType.EDIFICACOES_TIPO_2: 1.2,
            },
            "excepcional": {
                CAAgrupadoType.ESTRUTURAS_EM_GERAL: 1.0,
            },
        },
    }

    phi0 = {
        CACoefReducaoType.EDIFICACOES_DE_ACESSO_RESTRITO: 0.5,
        CACoefReducaoType.EDIFICACOES_DE_ACESSO_PUBLICO: 0.7,
        CACoefReducaoType.BIBLIOTECAS_ARQUIVOS_DEPOSITOS_OFICINAS_E_GARAGENS: 0.8,
        CACoefReducaoType.VENTO: 0.6,
        CACoefReducaoType.TEMPERATURA: 0.6,
        CACoefReducaoType.PASSARELAS_DE_PEDESTRES: 0.6,
        CACoefReducaoType.PONTES_RODOVIARIAS: 0.7,
        CACoefReducaoType.PONTES_FERROVIARIAS_NAO_ESPECIALIZADAS: 0.8,
        CACoefReducaoType.PONTES_FERROVIARIAS_ESPECIALIZADAS: 1.0,
        CACoefReducaoType.VIGAS_DE_ROLAMENTOS_DE_PONTES_ROLANTES: 1.0,
    }

    phi1 = {
        CACoefReducaoType.EDIFICACOES_DE_ACESSO_RESTRITO: 0.4,
        CACoefReducaoType.EDIFICACOES_DE_ACESSO_PUBLICO: 0.6,
        CACoefReducaoType.BIBLIOTECAS_ARQUIVOS_DEPOSITOS_OFICINAS_E_GARAGENS: 0.7,
        CACoefReducaoType.VENTO: 0.3,
        CACoefReducaoType.TEMPERATURA: 0.5,
        CACoefReducaoType.PASSARELAS_DE_PEDESTRES: 0.4,
        CACoefReducaoType.PONTES_RODOVIARIAS: 0.5,
        CACoefReducaoType.PONTES_FERROVIARIAS_NAO_ESPECIALIZADAS: 0.7,
        CACoefReducaoType.PONTES_FERROVIARIAS_ESPECIALIZADAS: 1.0,
        CACoefReducaoType.VIGAS_DE_ROLAMENTOS_DE_PONTES_ROLANTES: 0.8,
    }

    phi2 = {
        CACoefReducaoType.EDIFICACOES_DE_ACESSO_RESTRITO: 0.3,
        CACoefReducaoType.EDIFICACOES_DE_ACESSO_PUBLICO: 0.4,
        CACoefReducaoType.BIBLIOTECAS_ARQUIVOS_DEPOSITOS_OFICINAS_E_GARAGENS: 0.6,
        CACoefReducaoType.VENTO: 0.0,
        CACoefReducaoType.TEMPERATURA: 0.3,
        CACoefReducaoType.PASSARELAS_DE_PEDESTRES: 0.3,
        CACoefReducaoType.PONTES_RODOVIARIAS: 0.3,
        CACoefReducaoType.PONTES_FERROVIARIAS_NAO_ESPECIALIZADAS: 0.5,
        CACoefReducaoType.PONTES_FERROVIARIAS_ESPECIALIZADAS: 0.6,
        CACoefReducaoType.VIGAS_DE_ROLAMENTOS_DE_PONTES_ROLANTES: 0.5,
    }

    def __init__(
        self,
        label: str,
        tipo_carga: CASeparadoType | CAAgrupadoType,
        tipo_coef_reducao: CACoefReducaoType,
        valor: float,
        curta_duracao: bool = False,
        sismo: bool = False,
        fogo: bool = False,
    ):
        self.label = label
        self.tipo_carga = tipo_carga
        self.tipo_coef_reducao = tipo_coef_reducao
        self.valor = valor
        self.curta_duracao = curta_duracao
        self.sismo = sismo
        self.fogo = fogo
        if sismo:
            assert not fogo
        if fogo:
            assert not sismo
        if isinstance(tipo_carga, CASeparadoType):
            self.separado_ou_agrupado = "separado"
        elif isinstance(tipo_carga, CAAgrupadoType):
            self.separado_ou_agrupado = "agrupado"
        else:
            raise Exception()

    def get_gamma(self, tipo_combinacao: str, favoravel: bool = False):
        if favoravel:
            return 0.0
        else:
            return self.gamma_q[self.separado_ou_agrupado][tipo_combinacao][
                self.tipo_carga
            ]

    def get_phi0(self, tipo_combinacao: str, carga_principal: CargaAcidental):
        if tipo_combinacao == "especial" and carga_principal.curta_duracao:
            return self.phi2[self.tipo_coef_reducao]
        elif tipo_combinacao == "excepcional" and carga_principal.curta_duracao:
            if carga_principal.sismo:
                return 0.0
            elif carga_principal.fogo:
                return 0.7 * self.phi2[self.tipo_coef_reducao]
            else:
                return self.phi2[self.tipo_coef_reducao]
        else:
            return self.phi0[self.tipo_coef_reducao]

    def get_phi1(self, favoravel: bool = False):
        if favoravel:
            return 0.0
        else:
            return self.phi1[self.tipo_coef_reducao]

    def get_phi2(self, favoravel: bool = False):
        if favoravel:
            return 0.0
        else:
            return self.phi2[self.tipo_coef_reducao]


def append_combo(
    out: List[float], ca: List[float], n_cargas_acidentais: int, tol: float
):
    for o in out:
        residuo = 0.0
        for v in range(n_cargas_acidentais):
            residuo += abs(o[v] - ca[v])
        if residuo < tol:
            return False
    return True


def check_separado_ou_agrupado(carregamentos: List[CargaPermanente | CargaAcidental]):
    assert all(
        x.separado_ou_agrupado == carregamentos[0].separado_ou_agrupado
        for x in carregamentos
    )
    return carregamentos[0].separado_ou_agrupado


def calc_combi_ultima_carga_permanente(
    cargas_permanentes: List[CargaPermanente], tipo_combinacao: str
):
    assert tipo_combinacao in ["normal", "especial", "excepcional"]
    n_cargas_permanentes = len(cargas_permanentes)
    combos_fav_desfav = list(
        itertools.product([True, False], repeat=n_cargas_permanentes)
    )
    combis = []
    for i in range(len(combos_fav_desfav)):
        cp = []
        for j in range(n_cargas_permanentes):
            cp.append(
                cargas_permanentes[j].get_gamma(
                    tipo_combinacao, combos_fav_desfav[i][j]
                )
                * cargas_permanentes[j].valor
            )
        combis.append(cp)
    return combis


def calc_combi_ultima_carga_acidental(
    cargas_acidentais: List[CargaAcidental], tipo_combinacao: str, tol: float = 1e-8
):
    assert tipo_combinacao in ["normal", "especial", "excepcional"]
    n_cargas_acidentais = len(cargas_acidentais)
    combos_fav_desfav = list(
        itertools.product([True, False], repeat=(n_cargas_acidentais))
    )
    combis = []
    for i in range(len(combos_fav_desfav)):
        for k in range(n_cargas_acidentais):
            ca = []
            for j in range(n_cargas_acidentais):
                ca.append(
                    cargas_acidentais[j].get_gamma(
                        tipo_combinacao, combos_fav_desfav[i][j]
                    )
                    * cargas_acidentais[j].get_phi0(
                        tipo_combinacao, cargas_acidentais[k]
                    )
                    * cargas_acidentais[j].valor
                )
            ca[k] = (
                cargas_acidentais[k].get_gamma(tipo_combinacao, combos_fav_desfav[i][k])
                * cargas_acidentais[k].valor
            )
            if append_combo(combis, ca, n_cargas_acidentais, tol):
                combis.append(ca)
    return combis


def calc_combi_ultima(
    cargas_permanentes: List[CargaPermanente] = None,
    cargas_acidentais: List[CargaAcidental] = None,
    tipo_combinacao: str = "normal",
    tol: float = 1e-8,
):
    if cargas_permanentes is not None:
        separado_ou_agrupado_cp = check_separado_ou_agrupado(cargas_permanentes)
    if cargas_acidentais is not None:
        separado_ou_agrupado_ca = check_separado_ou_agrupado(cargas_acidentais)
    if (cargas_permanentes is not None) and (cargas_acidentais is not None):
        if separado_ou_agrupado_ca == "agrupado":
            assert separado_ou_agrupado_cp == "agrupado"

    combis = []
    if (cargas_permanentes is not None) and (cargas_acidentais is None):
        cp_combi_ultima = calc_combi_ultima_carga_permanente(
            cargas_permanentes, tipo_combinacao
        )
        for cp in cp_combi_ultima:
            combis.append((cp, []))
    elif (cargas_permanentes is None) and (cargas_acidentais is not None):
        ca_combi_ultima = calc_combi_ultima_carga_acidental(
            cargas_acidentais, tipo_combinacao, tol
        )
        for ca in ca_combi_ultima:
            combis.append(([], ca))
    elif (cargas_permanentes is None) and (cargas_acidentais is None):
        return []
    else:
        cp_combi_ultima = calc_combi_ultima_carga_permanente(
            cargas_permanentes, tipo_combinacao
        )
        ca_combi_ultima = calc_combi_ultima_carga_acidental(
            cargas_acidentais, tipo_combinacao, tol
        )
        for cp in cp_combi_ultima:
            for ca in ca_combi_ultima:
                combis.append((cp, ca))
    labels = (
        [cp.label for cp in cargas_permanentes]
        if cargas_permanentes is not None
        else [],
        [ca.label for ca in cargas_acidentais] if cargas_acidentais is not None else [],
    )
    return {"labels": labels, "combis": combis}


def calc_combi_servico_carga_permanente(cargas_permanentes: List[CargaPermanente]):
    combi = []
    for cp in cargas_permanentes:
        combi.append(cp.valor)
    return combi


def calc_combi_servico_carga_acidental(
    cargas_acidentais: List[CargaAcidental], tipo_combinacao: str, tol: float = 1e-8
):
    assert tipo_combinacao in ["quase permanente", "frequente", "raro"]
    n_cargas_acidentais = len(cargas_acidentais)
    combos_fav_desfav = list(
        itertools.product([True, False], repeat=(n_cargas_acidentais))
    )
    combis = []
    if tipo_combinacao == "quase permanente":
        for i in range(len(combos_fav_desfav)):
            ca = []
            for j in range(n_cargas_acidentais):
                ca.append(
                    cargas_acidentais[j].get_phi2(combos_fav_desfav[i][j])
                    * cargas_acidentais[j].valor
                )
            if append_combo(combis, ca, n_cargas_acidentais, tol):
                combis.append(ca)
    elif tipo_combinacao == "frequente":
        for i in range(len(combos_fav_desfav)):
            for k in range(n_cargas_acidentais):
                ca = []
                for j in range(n_cargas_acidentais):
                    ca.append(
                        cargas_acidentais[j].get_phi2(combos_fav_desfav[i][j])
                        * cargas_acidentais[j].valor
                    )
                ca[k] = (
                    cargas_acidentais[k].get_phi1(combos_fav_desfav[i][k])
                    * cargas_acidentais[k].valor
                )
                if append_combo(combis, ca, n_cargas_acidentais, tol):
                    combis.append(ca)
    elif tipo_combinacao == "raro":
        for i in range(len(combos_fav_desfav)):
            for k in range(n_cargas_acidentais):
                ca = []
                for j in range(n_cargas_acidentais):
                    ca.append(
                        cargas_acidentais[j].get_phi1(combos_fav_desfav[i][j])
                        * cargas_acidentais[j].valor
                    )
                ca[k] = cargas_acidentais[k].valor if combos_fav_desfav[i][k] else 0.0
                if append_combo(combis, ca, n_cargas_acidentais, tol):
                    combis.append(ca)
    return combis


def calc_combi_servico(
    cargas_permanentes: List[CargaPermanente] = None,
    cargas_acidentais: List[CargaAcidental] = None,
    tipo_combinacao: str = "frequente",
    tol: float = 1e-8,
):
    if cargas_permanentes is not None:
        separado_ou_agrupado_cp = check_separado_ou_agrupado(cargas_permanentes)
    if cargas_acidentais is not None:
        separado_ou_agrupado_ca = check_separado_ou_agrupado(cargas_acidentais)
    if (cargas_permanentes is not None) and (cargas_acidentais is not None):
        if separado_ou_agrupado_ca == "agrupado":
            assert separado_ou_agrupado_cp == "agrupado"

    combis = []
    if (cargas_permanentes is not None) and (cargas_acidentais is None):
        cp_combi_servico = calc_combi_servico_carga_permanente(cargas_permanentes)
        combis.append((cp_combi_servico, []))
    elif (cargas_permanentes is None) and (cargas_acidentais is not None):
        ca_combi_servico = calc_combi_servico_carga_acidental(
            cargas_acidentais, tipo_combinacao, tol
        )
        for ca in ca_combi_servico:
            combis.append(([], ca))
    elif (cargas_permanentes is None) and (cargas_acidentais is None):
        return []
    else:
        cp_combi_servico = calc_combi_servico_carga_permanente(cargas_permanentes)
        ca_combi_servico = calc_combi_servico_carga_acidental(
            cargas_acidentais, tipo_combinacao, tol
        )
        for ca in ca_combi_servico:
            combis.append((cp_combi_servico, ca))
    labels = (
        [cp.label for cp in cargas_permanentes]
        if cargas_permanentes is not None
        else [],
        [ca.label for ca in cargas_acidentais] if cargas_acidentais is not None else [],
    )
    return {"labels": labels, "combis": combis}
