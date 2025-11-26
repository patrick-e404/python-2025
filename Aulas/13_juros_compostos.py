#TRABALHANDO COM FUNÇÕES
#TYPE HINTING
#%%
def juros_compostos(aporte:int, taxa:float, anos:int)->float:
    """juros compostos serve para calcular o retorno financeiro a partir de um aporte. Deve-se considerar o valor, a taxa de juros atual e o tempo em anos para calculo do valor a ser retornado.

    aporte:
        numero inteiro, que represente o valor em reais

    taxa:
        um numero float entre 0 e 1 que represente o valor de juros

    anos:
        numero inteiro >= 1 que represente o tempo que o invetiento terá liquidez
    """
    return aporte * (1 + taxa) ** anos

juros_compostos(aporte=1000, taxa=0.13, anos=4)