from threading import main_thread


def questao_para_texto(dicionario_questao,id):
    questao="----------------------------------------\n"
    questao+='QUESTAO {0} \n'.format(id)
    questao+="\n"
    questao+="{0} \n".format(dicionario_questao["titulo"])
    questao+="\n"
    questao+='RESPOSTAS:\n'
    questao+="A:"" "+dicionario_questao['opcoes']["A"]
    questao+="\n"
    questao+="B:"" "+dicionario_questao['opcoes']["B"]
    questao+="\n"
    questao+="C:"" "+dicionario_questao['opcoes']["C"]
    questao+="\n"
    questao+="D:"" "+dicionario_questao['opcoes']["D"]
    return questao


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
