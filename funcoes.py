

def transforma_base(questoes):
    dic2 = {}
    lista1 = []
    lista2 = []
    lista3 = []
    i = 0
    for i in range(len(questoes)):
        verificação=questoes[i]['nivel']
        if verificação== 'facil':
            lista1.append(questoes[i])
            dic2['facil'] = lista1 
        elif verificação== 'medio':
            lista2.append(questoes[i])
            dic2['medio'] = lista2
        elif verificação== 'dificil':
            lista3.append(questoes[i])
            dic2['dificil'] = lista3 
    return dic2


import random
def sorteia_questao(dicionario_questao,nivel):
    lista=dicionario_questao[nivel]
    sorteia= random.choice(list(lista))
    return sorteia



import random


def sorteia_questao_inedita(dicionario_questao,nivel,lista_sorteadas):
    for i in range(len(dicionario_questao)):
        questao_inedita=random.choice(dicionario_questao[nivel])
        if questao_inedita not in lista_sorteadas:
            lista_sorteadas.append(questao_inedita)
            return questao_inedita
        else :
            return questao_inedita




def questao_para_texto(dicionario_questao,id):
        return '----------------------------------------\nQUESTAO {}\n\n{}\n\nRESPOSTAS:\nA: {}\nB: {}\nC: {}\nD: {}'.format(id, dicionario_questao['titulo'], dicionario_questao['opcoes']['A'], dicionario_questao['opcoes']['B'], dicionario_questao['opcoes']['C'], dicionario_questao['opcoes']['D'])


from random import randint
def gera_ajuda(questao):
    sorteia_numero=randint(1,2)
    if sorteia_numero == 1:
        sorteia=( ["A","B","C","D"][randint(0,3)])

        if sorteia != questao["correta"]:
            ajuda=questao["opcoes"][sorteia]
            resposta="'''DICA:\n""Opções certamente erradas: {0}'''".format(ajuda)
        else:
            return ""
    else: 
        sorteia=( ["A","B","C","D"][randint(0,3)])

        if sorteia != questao["correta"]:
            ajuda=questao["opcoes"][sorteia]
            ajuda2=questao["opcoes"][sorteia]
            resposta="'DICA: ""Opções certamente erradas: {0} | {1}'".format(ajuda,ajuda2)
        else:
            return ""
    return resposta




def valida_questoes (lista_questoes):
    def valida_questao (questao):

        saida = {}
        saida_opcoes = {}
        lista_letras = ['A', 'B', 'C', 'D']
        lista_niveis = ['facil', 'medio', 'dificil']

        if len(questao.keys()) != 4: 
           saida['outro'] = 'numero_chaves_invalido' #2

        if 'titulo' not in questao.keys(): #1
            saida['titulo'] = 'nao_encontrado'
        else:
        
            if questao['titulo'].strip() == '':
                saida['titulo'] = 'vazio' #3

        if 'nivel' not in questao.keys(): #1
            saida['nivel'] = 'nao_encontrado'
        else:
            if questao['nivel'] not in lista_niveis: 
                saida['nivel'] = 'valor_errado' #4

        if 'opcoes' not in questao.keys(): #1
            saida['opcoes'] = 'nao_encontrado'
        else:
            if len(questao['opcoes'].keys()) != 4: 
                saida['opcoes'] = 'tamanho_invalido' #5 
            else:
                for letra, valor in questao['opcoes'].items():
                
                    if letra in lista_letras:
                        if valor.strip() == '':
                            saida_opcoes[letra] = 'vazia' #7
                            saida['opcoes'] = saida_opcoes
                    else:
                        saida_opcoes[letra] = 'chave_invalida_ou_nao_encontrada' #6
                        saida['opcoes'] = saida_opcoes 

        if 'correta' not in questao.keys(): #1
            saida['correta'] = 'nao_encontrado'
        else: 
            if questao['correta'] not in lista_letras:
                saida['correta'] = 'valor_errado' #8

        return saida

    lista_saida = []
    for i in lista_questoes:
        lista_saida.append(valida_questao(i))
    return lista_saida

