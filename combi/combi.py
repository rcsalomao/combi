from __future__ import annotations

import csv
import itertools
import json
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
    PROTENSAO = auto()
    ELEMENTOS_ESTRUTURAIS_DE_MADEIRA_EM_GERAL_NBR7190_2022 = auto()
    ELEMENTOS_ESTRUTURAIS_INDUSTRIALIZADOS_DE_MADEIRA_NBR7190_2022 = auto()
    ACOES_PERMANENTES_NBR6118_2023 = auto()


class CPAgrupadoType(Enum):
    GRANDES_PONTES = auto()
    EDIFICACOES_TIPO_1 = auto()
    EDIFICACOES_TIPO_2 = auto()
    EFEITOS_DE_RECALQUES_DE_APOIO = auto()
    EFEITOS_DE_RETRACAO_DOS_MATERIAIS = auto()
    PROTENSAO = auto()


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
                CPSeparadoType.PROTENSAO: 1.2,
                CPSeparadoType.ELEMENTOS_ESTRUTURAIS_DE_MADEIRA_EM_GERAL_NBR7190_2022: 1.30,
                CPSeparadoType.ELEMENTOS_ESTRUTURAIS_INDUSTRIALIZADOS_DE_MADEIRA_NBR7190_2022: 1.25,
                CPSeparadoType.ACOES_PERMANENTES_NBR6118_2023: 1.4,
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
                CPSeparadoType.PROTENSAO: 1.2,
                CPSeparadoType.ELEMENTOS_ESTRUTURAIS_DE_MADEIRA_EM_GERAL_NBR7190_2022: 1.20,
                CPSeparadoType.ELEMENTOS_ESTRUTURAIS_INDUSTRIALIZADOS_DE_MADEIRA_NBR7190_2022: 1.15,
                CPSeparadoType.ACOES_PERMANENTES_NBR6118_2023: 1.3,
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
                CPSeparadoType.PROTENSAO: 1.2,
                CPSeparadoType.ELEMENTOS_ESTRUTURAIS_DE_MADEIRA_EM_GERAL_NBR7190_2022: 1.15,
                CPSeparadoType.ELEMENTOS_ESTRUTURAIS_INDUSTRIALIZADOS_DE_MADEIRA_NBR7190_2022: 1.10,
                CPSeparadoType.ACOES_PERMANENTES_NBR6118_2023: 1.2,
            },
        },
        "agrupado": {
            "normal": {
                CPAgrupadoType.GRANDES_PONTES: 1.3,
                CPAgrupadoType.EDIFICACOES_TIPO_1: 1.35,
                CPAgrupadoType.EDIFICACOES_TIPO_2: 1.4,
                CPAgrupadoType.EFEITOS_DE_RECALQUES_DE_APOIO: 1.2,
                CPAgrupadoType.EFEITOS_DE_RETRACAO_DOS_MATERIAIS: 1.2,
                CPSeparadoType.PROTENSAO: 1.2,
            },
            "especial": {
                CPAgrupadoType.GRANDES_PONTES: 1.2,
                CPAgrupadoType.EDIFICACOES_TIPO_1: 1.25,
                CPAgrupadoType.EDIFICACOES_TIPO_2: 1.3,
                CPAgrupadoType.EFEITOS_DE_RECALQUES_DE_APOIO: 1.2,
                CPAgrupadoType.EFEITOS_DE_RETRACAO_DOS_MATERIAIS: 1.2,
                CPSeparadoType.PROTENSAO: 1.2,
            },
            "excepcional": {
                CPAgrupadoType.GRANDES_PONTES: 1.1,
                CPAgrupadoType.EDIFICACOES_TIPO_1: 1.15,
                CPAgrupadoType.EDIFICACOES_TIPO_2: 1.2,
                CPAgrupadoType.EFEITOS_DE_RECALQUES_DE_APOIO: 0.0,
                CPAgrupadoType.EFEITOS_DE_RETRACAO_DOS_MATERIAIS: 0.0,
                CPSeparadoType.PROTENSAO: 1.2,
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
            elif self.tipo_carga in [
                CPSeparadoType.PROTENSAO,
                CPAgrupadoType.PROTENSAO,
            ]:
                return 0.9
            else:
                return 1.0
        else:
            return self.gamma_g[self.separado_ou_agrupado][tipo_combinacao][
                self.tipo_carga
            ]


class CASeparadoType(Enum):
    ACOES_TRUNCADAS = auto()
    EFEITO_DE_TEMPERATURA = auto()
    ACAO_DO_VENTO = auto()
    ACOES_VARIAVEIS_EM_GERAL = auto()
    EFEITO_DE_TEMPERATURA_GERADA_POR_EQUIPAMENTOS_NBR8800_2024 = auto()
    ACOES_VARIAVEIS_EM_GERAL_NBR6118_2024 = auto()
    EFEITO_DE_TEMPERATURA_NBR6118_2024 = auto()


class CAAgrupadoType(Enum):
    PONTES_E_EDIFICACOES_TIPO_1 = auto()
    EDIFICACOES_TIPO_2 = auto()


class CACoefReducaoType(Enum):
    EDIFICACOES_DE_ACESSO_RESTRITO = auto()
    EDIFICACOES_DE_ACESSO_PUBLICO = auto()
    BIBLIOTECAS_ARQUIVOS_DEPOSITOS_OFICINAS_E_GARAGENS = auto()
    EFEITO_DE_TEMPERATURA = auto()
    ACAO_DO_VENTO = auto()
    PASSARELAS_DE_PEDESTRES = auto()
    PONTES_RODOVIARIAS = auto()
    PONTES_FERROVIARIAS_NAO_ESPECIALIZADAS = auto()
    PONTES_FERROVIARIAS_ESPECIALIZADAS = auto()
    VIGAS_DE_ROLAMENTO_DE_PONTES_ROLANTES = auto()
    PILARES_OU_OUTROS_ELEMENTOS_OU_SUBESTRUTURAS_QUE_SUPORTAM_VIGAS_DE_ROLAMENTO_DE_PONTES_ROLANTES = auto()


class CargaAcidental(object):
    gamma_q = {
        "separado": {
            "normal": {
                CASeparadoType.ACOES_TRUNCADAS: 1.2,
                CASeparadoType.EFEITO_DE_TEMPERATURA: 1.2,
                CASeparadoType.ACAO_DO_VENTO: 1.4,
                CASeparadoType.ACOES_VARIAVEIS_EM_GERAL: 1.5,
                CASeparadoType.EFEITO_DE_TEMPERATURA_GERADA_POR_EQUIPAMENTOS_NBR8800_2024: 1.5,
                CASeparadoType.ACOES_VARIAVEIS_EM_GERAL_NBR6118_2024: 1.4,
                CASeparadoType.EFEITO_DE_TEMPERATURA_NBR6118_2024: 1.2,
            },
            "especial": {
                CASeparadoType.ACOES_TRUNCADAS: 1.1,
                CASeparadoType.EFEITO_DE_TEMPERATURA: 1.0,
                CASeparadoType.ACAO_DO_VENTO: 1.2,
                CASeparadoType.ACOES_VARIAVEIS_EM_GERAL: 1.3,
                CASeparadoType.EFEITO_DE_TEMPERATURA_GERADA_POR_EQUIPAMENTOS_NBR8800_2024: 1.3,
                CASeparadoType.ACOES_VARIAVEIS_EM_GERAL_NBR6118_2024: 1.2,
                CASeparadoType.EFEITO_DE_TEMPERATURA_NBR6118_2024: 1.0,
            },
            "excepcional": {
                CASeparadoType.ACOES_TRUNCADAS: 1.0,
                CASeparadoType.EFEITO_DE_TEMPERATURA: 1.0,
                CASeparadoType.ACAO_DO_VENTO: 1.0,
                CASeparadoType.ACOES_VARIAVEIS_EM_GERAL: 1.0,
                CASeparadoType.EFEITO_DE_TEMPERATURA_GERADA_POR_EQUIPAMENTOS_NBR8800_2024: 1.0,
                CASeparadoType.ACOES_VARIAVEIS_EM_GERAL_NBR6118_2024: 1.0,
                CASeparadoType.EFEITO_DE_TEMPERATURA_NBR6118_2024: 0.0,
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
                CAAgrupadoType.PONTES_E_EDIFICACOES_TIPO_1: 1.0,
                CAAgrupadoType.EDIFICACOES_TIPO_2: 1.0,
            },
        },
    }

    phi0 = {
        CACoefReducaoType.EDIFICACOES_DE_ACESSO_RESTRITO: 0.5,
        CACoefReducaoType.EDIFICACOES_DE_ACESSO_PUBLICO: 0.7,
        CACoefReducaoType.BIBLIOTECAS_ARQUIVOS_DEPOSITOS_OFICINAS_E_GARAGENS: 0.8,
        CACoefReducaoType.ACAO_DO_VENTO: 0.6,
        CACoefReducaoType.EFEITO_DE_TEMPERATURA: 0.6,
        CACoefReducaoType.PASSARELAS_DE_PEDESTRES: 0.6,
        CACoefReducaoType.PONTES_RODOVIARIAS: 0.7,
        CACoefReducaoType.PONTES_FERROVIARIAS_NAO_ESPECIALIZADAS: 0.8,
        CACoefReducaoType.PONTES_FERROVIARIAS_ESPECIALIZADAS: 1.0,
        CACoefReducaoType.VIGAS_DE_ROLAMENTO_DE_PONTES_ROLANTES: 1.0,
        CACoefReducaoType.PILARES_OU_OUTROS_ELEMENTOS_OU_SUBESTRUTURAS_QUE_SUPORTAM_VIGAS_DE_ROLAMENTO_DE_PONTES_ROLANTES: 0.7,
    }

    phi1 = {
        CACoefReducaoType.EDIFICACOES_DE_ACESSO_RESTRITO: 0.4,
        CACoefReducaoType.EDIFICACOES_DE_ACESSO_PUBLICO: 0.6,
        CACoefReducaoType.BIBLIOTECAS_ARQUIVOS_DEPOSITOS_OFICINAS_E_GARAGENS: 0.7,
        CACoefReducaoType.ACAO_DO_VENTO: 0.3,
        CACoefReducaoType.EFEITO_DE_TEMPERATURA: 0.5,
        CACoefReducaoType.PASSARELAS_DE_PEDESTRES: 0.4,
        CACoefReducaoType.PONTES_RODOVIARIAS: 0.5,
        CACoefReducaoType.PONTES_FERROVIARIAS_NAO_ESPECIALIZADAS: 0.7,
        CACoefReducaoType.PONTES_FERROVIARIAS_ESPECIALIZADAS: 1.0,
        CACoefReducaoType.VIGAS_DE_ROLAMENTO_DE_PONTES_ROLANTES: 0.8,
        CACoefReducaoType.PILARES_OU_OUTROS_ELEMENTOS_OU_SUBESTRUTURAS_QUE_SUPORTAM_VIGAS_DE_ROLAMENTO_DE_PONTES_ROLANTES: 0.6,
    }

    phi2 = {
        CACoefReducaoType.EDIFICACOES_DE_ACESSO_RESTRITO: 0.3,
        CACoefReducaoType.EDIFICACOES_DE_ACESSO_PUBLICO: 0.4,
        CACoefReducaoType.BIBLIOTECAS_ARQUIVOS_DEPOSITOS_OFICINAS_E_GARAGENS: 0.6,
        CACoefReducaoType.ACAO_DO_VENTO: 0.0,
        CACoefReducaoType.EFEITO_DE_TEMPERATURA: 0.3,
        CACoefReducaoType.PASSARELAS_DE_PEDESTRES: 0.3,
        CACoefReducaoType.PONTES_RODOVIARIAS: 0.3,
        CACoefReducaoType.PONTES_FERROVIARIAS_NAO_ESPECIALIZADAS: 0.5,
        CACoefReducaoType.PONTES_FERROVIARIAS_ESPECIALIZADAS: 0.6,
        CACoefReducaoType.VIGAS_DE_ROLAMENTO_DE_PONTES_ROLANTES: 0.5,
        CACoefReducaoType.PILARES_OU_OUTROS_ELEMENTOS_OU_SUBESTRUTURAS_QUE_SUPORTAM_VIGAS_DE_ROLAMENTO_DE_PONTES_ROLANTES: 0.4,
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


def check_separado_ou_agrupado(carregamentos: list[CargaPermanente | CargaAcidental]):
    test = set([c.separado_ou_agrupado for c in carregamentos])
    assert (
        len(test) == 1
    ), "Para um mesmo conjunto, há carregamentos do tipo 'separado' e 'agrupado', o que não é permitido por norma"
    return test.pop()


def calc_combi_ultima_carga_permanente(
    cargas_permanentes: list[CargaPermanente], tipo_combinacao: str
):
    assert tipo_combinacao in ["normal", "especial", "excepcional"]
    n_cargas_permanentes = len(cargas_permanentes)
    combos_fav_desfav = list(
        itertools.product([True, False], repeat=n_cargas_permanentes)
    )
    label_combis = []
    combis = []
    for i in range(len(combos_fav_desfav)):
        lbls = []
        cps = []
        for j in range(n_cargas_permanentes):
            gamma_g = cargas_permanentes[j].get_gamma(
                tipo_combinacao, combos_fav_desfav[i][j]
            )
            lbls.append(str(gamma_g) + "*" + cargas_permanentes[j].label)
            cps.append(gamma_g * cargas_permanentes[j].valor)
        label_combis.append(" + ".join(lbls))
        combis.append(cps)
    return (label_combis, combis)


def calc_combi_ultima_carga_acidental(
    cargas_acidentais: list[CargaAcidental],
    tipo_combinacao: str,
):
    assert tipo_combinacao in ["normal", "especial", "excepcional"]
    n_cargas_acidentais = len(cargas_acidentais)
    combos_fav_desfav = list(
        itertools.product([True, False], repeat=(n_cargas_acidentais))
    )
    label_combis = []
    combis = []
    carregamentos_acidentais_principais = []
    for i in range(len(combos_fav_desfav)):
        for k in range(n_cargas_acidentais):
            lbls = []
            cas = []
            for j in range(n_cargas_acidentais):
                gamma_q = cargas_acidentais[j].get_gamma(
                    tipo_combinacao, combos_fav_desfav[i][j]
                )
                phi0 = cargas_acidentais[j].get_phi0(
                    tipo_combinacao, cargas_acidentais[k]
                )
                lbls.append(
                    str(gamma_q) + "*" + str(phi0) + "*" + cargas_acidentais[j].label
                )
                cas.append(gamma_q * phi0 * cargas_acidentais[j].valor)
            gamma_q = cargas_acidentais[k].get_gamma(
                tipo_combinacao, combos_fav_desfav[i][k]
            )
            lbls[k] = str(gamma_q) + "*" + cargas_acidentais[k].label
            cas[k] = gamma_q * cargas_acidentais[k].valor
            label_combis.append(" + ".join(lbls))
            combis.append(cas)
            carregamentos_acidentais_principais.append(cargas_acidentais[k].label)
    return (label_combis, combis, carregamentos_acidentais_principais)


def calc_combi_servico_carga_permanente(cargas_permanentes: list[CargaPermanente]):
    lbls = []
    cps = []
    for i in range(len(cargas_permanentes)):
        lbls.append(cargas_permanentes[i].label)
        cps.append(cargas_permanentes[i].valor)
    label_combis = [" + ".join(lbls)]
    combi = [cps]
    return (label_combis, combi)


def calc_combi_servico_carga_acidental(
    cargas_acidentais: list[CargaAcidental],
    tipo_combinacao: str,
):
    assert tipo_combinacao in ["quase permanente", "frequente", "raro"]
    n_cargas_acidentais = len(cargas_acidentais)
    combos_fav_desfav = list(
        itertools.product([True, False], repeat=(n_cargas_acidentais))
    )
    label_combis = []
    combis = []
    carregamentos_acidentais_principais = []
    if tipo_combinacao == "quase permanente":
        for i in range(len(combos_fav_desfav)):
            lbls = []
            cas = []
            for j in range(n_cargas_acidentais):
                phi2 = cargas_acidentais[j].get_phi2(combos_fav_desfav[i][j])
                lbls.append(str(phi2) + "*" + cargas_acidentais[j].label)
                cas.append(phi2 * cargas_acidentais[j].valor)
            label_combis.append(lbls)
            combis.append(cas)
            carregamentos_acidentais_principais.append(None)
    elif tipo_combinacao == "frequente":
        for i in range(len(combos_fav_desfav)):
            for k in range(n_cargas_acidentais):
                lbls = []
                cas = []
                for j in range(n_cargas_acidentais):
                    phi2 = cargas_acidentais[j].get_phi2(combos_fav_desfav[i][j])
                    lbls.append(str(phi2) + "*" + cargas_acidentais[j].label)
                    cas.append(phi2 * cargas_acidentais[j].valor)
                phi1 = cargas_acidentais[k].get_phi1(combos_fav_desfav[i][k])
                lbls[k] = str(phi1) + "*" + cargas_acidentais[k].label
                cas[k] = phi1 * cargas_acidentais[k].valor
                label_combis.append(lbls)
                combis.append(cas)
                carregamentos_acidentais_principais.append(cargas_acidentais[k].label)
    elif tipo_combinacao == "raro":
        for i in range(len(combos_fav_desfav)):
            for k in range(n_cargas_acidentais):
                lbls = []
                cas = []
                for j in range(n_cargas_acidentais):
                    phi1 = cargas_acidentais[j].get_phi1(combos_fav_desfav[i][j])
                    lbls.append(str(phi1) + "*" + cargas_acidentais[j].label)
                    cas.append(phi1 * cargas_acidentais[j].valor)
                phi = 1.0 if combos_fav_desfav[i][k] else 0.0
                lbls[k] = str(phi) + "*" + cargas_acidentais[k].label
                cas[k] = phi * cargas_acidentais[k].valor
                label_combis.append(lbls)
                combis.append(cas)
                carregamentos_acidentais_principais.append(cargas_acidentais[k].label)
    return (label_combis, combis, carregamentos_acidentais_principais)


class Combi(object):
    def __init__(self, data: dict):
        self._data = data

    @property
    def data(self):
        return self._data

    @property
    def label_carregamentos(self):
        return self.data["label_carregamentos"]

    @property
    def combis(self):
        return self.data["combis"]

    def get_json(self):
        return json.dumps(
            self.data,
            indent=2,
            ensure_ascii=False,
        )

    def write_json(self, file_name: str):
        json_string = self.get_json()
        with open(file_name + ".json", "w") as file:
            file.write(json_string)

    def write_csv(self, file_name: str):
        with open(file_name + ".csv", "w") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(
                ["label_combis"]
                + ["carregamento_acidental_principal"]
                + self.label_carregamentos["carregamentos_permanentes"]
                + self.label_carregamentos["carregamentos_acidentais"]
            )
            for c in self.combis:
                csv_writer.writerow(
                    [c["label"]]
                    + [c["carregamento_acidental_principal"]]
                    + c["carregamentos_permanentes"]
                    + c["carregamentos_acidentais"]
                )


def calc_combi_ultima(
    cargas_permanentes: list[CargaPermanente] = None,
    cargas_acidentais: list[CargaAcidental] = None,
    tipo_combinacao: str = "normal",
):
    if cargas_permanentes is not None:
        separado_ou_agrupado_cps = check_separado_ou_agrupado(cargas_permanentes)
    if cargas_acidentais is not None:
        separado_ou_agrupado_cas = check_separado_ou_agrupado(cargas_acidentais)
    if (cargas_permanentes is not None) and (cargas_acidentais is not None):
        if separado_ou_agrupado_cas == "agrupado":
            assert (
                separado_ou_agrupado_cps == "agrupado"
            ), "O conjunto de carregamentos permanentes deve ser do tipo 'agrupado', em conformidade com o tipo do conjunto de carregamentos variáveis"

    label_combis = []
    combis = []
    carregamentos_acidentais_principais = []
    if (cargas_permanentes is not None) and (cargas_acidentais is None):
        label_cps_combi_ultima, cps_combi_ultima = calc_combi_ultima_carga_permanente(
            cargas_permanentes, tipo_combinacao
        )
        for cps in cps_combi_ultima:
            combis.append((cps, []))
            carregamentos_acidentais_principais.append(None)
        label_combis = label_cps_combi_ultima
    elif (cargas_permanentes is None) and (cargas_acidentais is not None):
        (
            label_cas_combi_ultima,
            cas_combi_ultima,
            carregamentos_acidentais_principais_,
        ) = calc_combi_ultima_carga_acidental(cargas_acidentais, tipo_combinacao)
        for cas in cas_combi_ultima:
            combis.append(([], cas))
        label_combis = label_cas_combi_ultima
        carregamentos_acidentais_principais = carregamentos_acidentais_principais_
    elif (cargas_permanentes is None) and (cargas_acidentais is None):
        return []
    else:
        label_cps_combi_ultima, cps_combi_ultima = calc_combi_ultima_carga_permanente(
            cargas_permanentes, tipo_combinacao
        )
        (
            label_cas_combi_ultima,
            cas_combi_ultima,
            carregamentos_acidentais_principais_,
        ) = calc_combi_ultima_carga_acidental(cargas_acidentais, tipo_combinacao)
        for m, cps in enumerate(cps_combi_ultima):
            for n, cas in enumerate(cas_combi_ultima):
                combis.append((cps, cas))
                label_combis.append(
                    label_cps_combi_ultima[m] + " + " + label_cas_combi_ultima[n]
                )
                carregamentos_acidentais_principais.append(
                    carregamentos_acidentais_principais_[n]
                )
    label_carregamentos = {
        "carregamentos_permanentes": [cp.label for cp in cargas_permanentes]
        if cargas_permanentes is not None
        else [],
        "carregamentos_acidentais": [ca.label for ca in cargas_acidentais]
        if cargas_acidentais is not None
        else [],
    }
    combis = [
        {
            "label": label_combis[i],
            "carregamentos_permanentes": cps,
            "carregamentos_acidentais": cas,
            "carregamento_acidental_principal": carregamentos_acidentais_principais[i],
        }
        for i, (cps, cas) in enumerate(combis)
    ]
    return Combi(
        {
            "label_carregamentos": label_carregamentos,
            "combis": combis,
        }
    )


def calc_combi_servico(
    cargas_permanentes: list[CargaPermanente] = None,
    cargas_acidentais: list[CargaAcidental] = None,
    tipo_combinacao: str = "frequente",
):
    if cargas_permanentes is not None:
        separado_ou_agrupado_cps = check_separado_ou_agrupado(cargas_permanentes)
    if cargas_acidentais is not None:
        separado_ou_agrupado_cas = check_separado_ou_agrupado(cargas_acidentais)
    if (cargas_permanentes is not None) and (cargas_acidentais is not None):
        if separado_ou_agrupado_cas == "agrupado":
            assert separado_ou_agrupado_cps == "agrupado"

    label_combis = []
    combis = []
    carregamentos_acidentais_principais = []
    if (cargas_permanentes is not None) and (cargas_acidentais is None):
        label_cps_combi_servico, cps_combi_servico = (
            calc_combi_servico_carga_permanente(cargas_permanentes)
        )
        for cps in cps_combi_servico:
            combis.append((cps, []))
            carregamentos_acidentais_principais.append(None)
        label_combis = label_cps_combi_servico
    elif (cargas_permanentes is None) and (cargas_acidentais is not None):
        (
            label_cas_combi_servico,
            cas_combi_servico,
            carregamentos_acidentais_principais_,
        ) = calc_combi_servico_carga_acidental(cargas_acidentais, tipo_combinacao)
        for cas in cas_combi_servico:
            combis.append(([], cas))
        label_combis = label_cas_combi_servico
        carregamentos_acidentais_principais = carregamentos_acidentais_principais_
    elif (cargas_permanentes is None) and (cargas_acidentais is None):
        return []
    else:
        label_cps_combi_servico, cps_combi_servico = (
            calc_combi_servico_carga_permanente(cargas_permanentes)
        )
        (
            label_cas_combi_servico,
            cas_combi_servico,
            carregamentos_acidentais_principais_,
        ) = calc_combi_servico_carga_acidental(cargas_acidentais, tipo_combinacao)
        for m, cps in enumerate(cps_combi_servico):
            for n, cas in enumerate(cas_combi_servico):
                combis.append((cps, cas))
                label_combis.append(
                    label_cps_combi_servico[m] + " + " + label_cas_combi_servico[n]
                )
                carregamentos_acidentais_principais.append(
                    carregamentos_acidentais_principais_[n]
                )
    label_carregamentos = {
        "carregamentos_permanentes": [cp.label for cp in cargas_permanentes]
        if cargas_permanentes is not None
        else [],
        "carregamentos_acidentais": [ca.label for ca in cargas_acidentais]
        if cargas_acidentais is not None
        else [],
    }
    combis = [
        {
            "label": label_combis[i],
            "carregamentos_permanentes": cps,
            "carregamentos_acidentais": cas,
            "carregamento_acidental_principal": carregamentos_acidentais_principais[i],
        }
        for i, (cps, cas) in enumerate(combis)
    ]
    return Combi(
        {
            "label_carregamentos": label_carregamentos,
            "combis": combis,
        }
    )
