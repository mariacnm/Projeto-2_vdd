import random
def sorteia_questao(dicionario_questao,nivel):
    lista=dicionario_questao[nivel]
    sorteia= random.choice(list(lista))
    return sorteia



def sorteia_questao_inedida(dicionario_questao,nivel,lista_questao):
    j=1
    dicionario_questao[nivel]