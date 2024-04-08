from combi import (
    CPAgrupadoType,
    CPSeparadoType,
    CargaPermanente,
    CAAgrupadoType,
    CASeparadoType,
    CACoefReducaoType,
    CargaAcidental,
    calc_combi_ultima,
    calc_combi_servico,
)
from pprint import pp
# import json
# import pandas as pd


def main():
    cargas_permanentes = [
        CargaPermanente(
            "cp1",
            CPSeparadoType.ELEMENTOS_CONSTRUTIVOS_INDUSTRIALIZADOS_COM_ADICOES_IN_LOCO,
            1,
        ),
        CargaPermanente(
            "cp2",
            CPSeparadoType.ELEMENTOS_CONSTRUTIVOS_INDUSTRIALIZADOS_COM_ADICOES_IN_LOCO,
            2,
        ),
        CargaPermanente(
            "cp3",
            CPSeparadoType.ELEMENTOS_CONSTRUTIVOS_INDUSTRIALIZADOS_COM_ADICOES_IN_LOCO,
            3,
        ),
    ]
    cargas_variaveis = [
        CargaAcidental(
            "ca1",
            CASeparadoType.ACOES_VARIAVEIS_EM_GERAL,
            CACoefReducaoType.EDIFICACOES_DE_ACESSO_PUBLICO,
            1,
        ),
        CargaAcidental(
            "ca2",
            CASeparadoType.ACOES_VARIAVEIS_EM_GERAL,
            CACoefReducaoType.EDIFICACOES_DE_ACESSO_PUBLICO,
            2,
        ),
        CargaAcidental(
            "ca3",
            CASeparadoType.VENTO,
            CACoefReducaoType.VENTO,
            3,
        ),
    ]

    combis = calc_combi_ultima(cargas_permanentes, cargas_variaveis)
    # combis = calc_combi_ultima(cargas_permanentes)
    # combis = calc_combi_ultima(cargas_acidentais=cargas_variaveis)

    pp(combis)
    # pp(combis["labels"])
    # pp(combis["combis"])
    # print(len(combis["combis"]))
    # print(json.dumps(combis))
    # print(
    #     pd.DataFrame(combis["combis"], columns=[",".join(g) for g in combis["labels"]])
    # )


if __name__ == "__main__":
    main()
