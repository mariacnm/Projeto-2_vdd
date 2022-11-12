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
    