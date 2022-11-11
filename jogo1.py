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

def valida_questoes (lista_questoes):
    def valida_questao(questao):

        lista1 = ['A', 'B', 'C', 'D']
        lista2 = ['facil', 'medio', 'dificil']
        dic = {}
        saida_opcoes = {}

        if len(questao) != 4: 
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
    
#começando o jogo perguntando o nome
print("Olá! você esta na Fortuna DesSfotf e terá a oportunidade de enriquecer!")
nome=input("Qual seu nome? ")
print("ok {0}, você tem direito a pular 3 vezes e 2 ajudas!\n".format(nome))

#enter
input("Aperte ENTER para continuar....\n")

#o jogo vai começar
print("O jogo já vai começar! Lá vem a primeira questão!\n")
print("Vamos começar com a questões do nível FACIL!")
input("Aperte ENTER para continuar....\n")
questoes = [
  {
    'titulo': 'Qual o resultado da operação 57 + 32?',
    'nivel': 'facil',
    'opcoes': {'A': '-19', 'B': '85', 'C': '89', 'D': '99'},
    'correta': 'C'
  },
  {
    'titulo': 'Qual a capital do Brasil?',
    'nivel': 'facil',
    'opcoes': {'A': 'Brasília', 'B': 'Rio de janeiro', 'C': 'São Paulo', 'D': 'Osasco'},
    'correta': 'A'
  },
  {
    'titulo': 'Quem é considerada a primeira pessoa programadora do mundo?!',
    'nivel': 'medio',
    'opcoes': {'A': 'Marie Curie', 'B': 'Alan Turing', 'C': 'Ada Lovelace', 'D': 'Edsger Dijkstra'},
    'correta': 'C'
  }
]







trans_base = transforma_base(questoes)
if trans_base["facil"]:
    for i in range(len(trans_base['facil'])):
        valida1 = valida_questoes(trans_base['facil'][i])
        print(valida1)
        #if valida1 == []:
            #sorteia=(sorteia_questao(trans_base,'facil'))
            
        #else: 
            #del trans_base['facil'][i]
        #else:
            #del trans_base['facil'][i]
#else:
    #if pont == 5000:'''

    

