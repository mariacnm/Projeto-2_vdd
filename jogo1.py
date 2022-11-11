from funcoes import transforma_base

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


questoes=[
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


from funcoes import valida_questoes
from funcoes import sorteia_questao
from funcoes import questao_para_texto

trans_base = transforma_base(questoes)


if trans_base["facil"]:
    for i in range(len(trans_base['facil'])):
        valida1= (valida_questoes(trans_base["facil"]))
        print(valida1)

        #else: 
            #del trans_base['facil'][i]
        #else:
            #del trans_base['facil'][i]
#else:
    #if pont == 5000:'''