import random
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

def valida_questao(questao):

    lista1 = ['A', 'B', 'C', 'D']
    lista2 = ['facil', 'medio', 'dificil']
    dic = {}
    saida_opcoes = {}

    if len(questao.keys()) != 4: 
        dic['outro'] = 'numero_chaves_invalido' 

    if 'titulo' not in questao.keys(): 
        dic['titulo'] = 'nao_encontrado'
    else:
        if questao['titulo'].strip() == '':
            dic['titulo'] = 'vazio' 

    if 'nivel' not in questao.keys(): 
        dic['nivel'] = 'nao_encontrado'
    else:
        if questao['nivel'] not in lista2: 
            dic['nivel'] = 'valor_errado' 

    if 'opcoes' not in questao.keys(): 
        dic['opcoes'] = 'nao_encontrado'
    else:
        if len(questao['opcoes'].keys()) != 4: 
            dic['opcoes'] = 'tamanho_invalido' 
        else:
            for a,b in questao['opcoes'].items():
                if a in lista1:
                    if b.strip() == '':
                        saida_opcoes[a] = 'vazia'
                        dic['opcoes'] = saida_opcoes
                else:
                    saida_opcoes[a] = 'chave_invalida_ou_nao_encontrada'
                    dic['opcoes'] = saida_opcoes 

    if 'correta' not in questao.keys():
        dic['correta'] = 'nao_encontrado'
    else: 
        if questao['correta'] not in lista1:
            dic['correta'] = 'valor_errado'

    return dic
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

def sorteia_questao(dicionario_questao,nivel):
    lista=dicionario_questao[nivel]
    sorteia= random.choice(list(lista))
    return sorteia

def questao_para_texto(dicionario_questao,id):
        return '----------------------------------------\nQUESTAO {}\n\n{}\n\nRESPOSTAS:\nA: {}\nB: {}\nC: {}\nD: {}'.format(id, dicionario_questao['titulo'], dicionario_questao['opcoes']['A'], dicionario_questao['opcoes']['B'], dicionario_questao['opcoes']['C'], dicionario_questao['opcoes']['D'])

import random

def gera_ajuda(questao):
    lista2 = []
    
    for a,b in questao.items():

        if questao['correta'] == 'A':
            lista2.append(questao['opcoes']['B'])
            lista2.append(questao['opcoes']['C'])
            lista2.append(questao['opcoes']['D'])

        if questao['correta'] == 'B':
            lista2.append(questao['opcoes']['A'])
            lista2.append(questao['opcoes']['C'])
            lista2.append(questao['opcoes']['D'])

        if questao['correta'] == 'C':
            lista2.append(questao['opcoes']['A'])
            lista2.append(questao['opcoes']['B'])
            lista2.append(questao['opcoes']['D'])

        if questao['correta'] == 'D':
            lista2.append(questao['opcoes']['A'])
            lista2.append(questao['opcoes']['B'])
            lista2.append(questao['opcoes']['C'])

    string = 'DICA:\nOpções certamente erradas: {0}'.format(random.choice(lista2))
    return string
    

