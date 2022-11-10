from threading import main_thread


def questao_para_texto(dicionario_questao,id):
        return '----------------------------------------\nQUESTAO {}\n\n{}\n\nRESPOSTAS:\nA: {}\nB: {}\nC: {}\nD: {}'.format(id, dicionario_questao['titulo'], dicionario_questao['opcoes']['A'], dicionario_questao['opcoes']['B'], dicionario_questao['opcoes']['C'], dicionario_questao['opcoes']['D'])





dicionario_questao={
        'titulo': 'Qual o resultado da operação 57 + 32?',
        'nivel': 'facil',
        'opcoes': {
		      'A': '-19', 
		      'B': '85', 
		      'C': '89', 
		      'D': '99'
	},
        'correta': 'C'
}
id=12
print(questao_para_texto(dicionario_questao,id))
