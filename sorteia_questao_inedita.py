import random


def sorteia_questao_inedita(dicionario_questao,nivel,lista_sorteadas):
    for i in range(len(dicionario_questao)):
        questao_inedita=random.choice(dicionario_questao[nivel])
        if questao_inedita not in lista_sorteadas:
            lista_sorteadas.append(questao_inedita)
            return questao_inedita
        else :
            return questao_inedita
        


questoes={
  'facil':
    [
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
      }
    ]
  
}
nivel="facil"
lista=[]
for i in range(len(questoes)):
  sorteia=sorteia_questao_inedita(questoes,nivel,lista)
  lista.append(sorteia)
  print (lista)