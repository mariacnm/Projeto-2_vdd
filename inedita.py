import random

def sorteia_questao_inedita(dicionario_questao,nivel,lista_sorteadas):
    questao_inedita=random.choice(dicionario_questao[nivel])
    while questao_inedita in lista_sorteadas:
        questao_inedita=random.choice(dicionario_questao[nivel])
    if questao_inedita not in lista_sorteadas:
        lista_sorteadas.append(questao_inedita)
        return questao_inedita

