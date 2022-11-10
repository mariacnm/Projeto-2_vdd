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
questao = {
  'titulo': 'Qual o resultado da operação 57 + 32?',
  'nivel': 'facil',
  'opcoes': {'A': '-19', 'B': '85', 'C': '89', 'D': '99'},
  'correta': 'C'
}
print(valida_questao(questao))