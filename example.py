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
            CASeparadoType.ACAO_DO_VENTO,
            CACoefReducaoType.ACAO_DO_VENTO,
            3,
        ),
    ]

    resultado = calc_combi_ultima(cargas_permanentes, cargas_variaveis)
    # resultado = calc_combi_ultima(cargas_permanentes)
    # resultado = calc_combi_ultima(cargas_acidentais=cargas_variaveis)

    pp(resultado.data)
    # print(len(resultado.combis))
    # print(resultado.get_json())
    # resultado.write_json('resultado')
    # resultado.write_csv("resultado")


if __name__ == "__main__":
    main()
