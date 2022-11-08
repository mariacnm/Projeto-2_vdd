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

    dic={}
    for a,b in range(questao):
        if a == "titulo" :
            a+=1
            if a =="nivel":
                a+=1
                if a== "opcoes":
                    a+=1
                    if a== "correta":
                        a+=1
                    else:dic["correta"]="nao encontrado"
                else:
                    dic["opcoes"]="nao encontrado"      
            else:
                 dic["nivel"]="nao encontrado"
        else:
            dic["titulo"]="nao encontrado"
import random
def sorteia_questao(dicionario_questao,nivel):
    lista=dicionario_questao[nivel]
    sorteia= random.choice(list(lista))
    return sorteia
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


print("Olá! você esta na Fortuna DesSfotf e terá a oportunidade de enriquecer!")
nome=input("Qual seu nome")
print("ok {0}, você tem direito a pular 3 vezes e 2 ajudas!\n".format(nome))


input("Aperte ENTER para continuar....\n")

print("O jogo já vai começar! Lá vem a primeira questão!\n")
print("Vamos começar com a questões do nível FACIL!")
input("Aperte ENTER para continuar....\n")

listas_questoes= {
  "facil": [
    {
      "titulo": "Qual o resultado da operação 57 + 32?",
      "nivel": "facil",
      "opcoes": {
        "A": "-19",
        "B": "85",
        "C": "89",
        "D": "99"
      },
      "correta": "C"
    },
    {
      "titulo": "Qual destes parques não se localiza em São Paulo?!",
      "nivel": "facil",
      "opcoes": {
        "A": "Ibirapuera",
        "B": "Parque do Carmo",
        "C": "Parque Villa Lobos",
        "D": "Morro da Urca"
      },
      "correta": "D"
    },
    {
      "titulo": "Qual destas não é uma linguagem de programação?",
      "nivel": "facil",
      "opcoes": {
        "A": "Miratdes",
        "B": "Python",
        "C": "Lua",
        "D": "C++"
      },
      "correta": "A"
    },
    {
      "titulo": "Dentre os listados, qual destes esportes é menos praticado no Brasil?",
      "nivel": "facil",
      "opcoes": {
        "A": "Natação",
        "B": "Vôlei",
        "C": "Ski Cross Country",
        "D": "Natação"
      },
      "correta": "C"
    }
  ],
  "medio": [
    {
      "titulo": "Qual destes números é primo?",
      "nivel": "medio",
      "opcoes": {
        "A": "259",
        "B": "85",
        "C": "49",
        "D": "19"
      },
      "correta": "D"
    },
    {
      "titulo": "Na Conjectura de _______, escolhendo-se um número natural inicial n, onde n > 0, os seguintes critérios serão obedecidos: Se n for par o seu sucessor será a metade e se n for ímpar o seu sucessor será o triplo mais um, gerando então um novo número. Qual o nome da conjectura?",
      "nivel": "medio",
      "opcoes": {
        "A": "Collatz",
        "B": "Goldbach",
        "C": "Poincaré",
        "D": "Hodge"
      },
      "correta": "A"
    },
    {
      "titulo": "Qual a segunda pessoa mais seguida no Instagram?",
      "nivel": "medio",
      "opcoes": {
        "A": "Cristiano Ronaldo",
        "B": "Dwayne Johnson",
        "C": "Kim Kardashian",
        "D": "Kylie Jenner"
      },
      "correta": "D"
    }
  ],
  "dificil": [
    {
      "titulo": "A reprodução dos seres vivos é um processo biológico através do qual os organismos geram descendência. Qual desta não é uma forma de reprodução assexuada?",
      "nivel": "dificil",
      "opcoes": {
        "A": "Autogamia",
        "B": "Esporulação",
        "C": "Partenogênese",
        "D": "Divisão binária"
      },
      "correta": "A"
    },
    {
      "titulo": "Qual o resultado da operação 5 + 2 * 3 ^ 2, onde ^ representa potenciação?",
      "nivel": "dificil",
      "opcoes": {
        "A": "441",
        "B": "86",
        "C": "Nenhuma das outras respostas",
        "D": "23"
      },
      "correta": "D"
    }
  ]
}

questoes_sorteadas= sorteia_questao(listas_questoes,"facil")
texto=questao_para_texto(questoes_sorteadas,1)
print("{0} \n" .format(texto))
resposta=input("Qual e sua resposta?\n")
#print("Qual e sua reposta?\n")
if resposta == questoes_sorteadas["correta"]:
    print("Você ACertou! Seu Prêmio atual é de R$ 1000,00")
else:
     print("Que pena! Você errou e vai sair sem nada :(")