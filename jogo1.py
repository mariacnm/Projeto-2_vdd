import random
from random import randint
from funcoes import transforma_base
from funcoes import valida_questoes
from funcoes import sorteia_questao
from funcoes import questao_para_texto
from funcoes import sorteia_questao_inedita
from funcoes import gera_ajuda


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


questoes=[{'titulo': 'Qual o resultado da operação 57 + 32?',
          'nivel': 'facil',
          'opcoes': {'A': '-19', 'B': '85', 'C': '89', 'D': '99'},
          'correta': 'C'},

         {'titulo': 'Qual a capital do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Brasília', 'B': 'Rio de janeiro', 'C': 'São Paulo', 'D': 'Osasco'},
          'correta': 'A'},

         {'titulo': 'Quando é o feriado da Independência do Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': '21 de Abril', 'B': '12 de Outubro', 'C': '07 de Setembro', 'D': '15 de Novembro'},
          'correta': 'C'},

         {'titulo': '_________ é um conjunto de particularidades que caracterizam um grupo de pessoas, uma família ou uma sociedade. É formada por princípios morais, hábitos, costumes, histórias, manifestações religiosas, entre outros. Qual palavra melhor completa o início da frase?',
          'nivel': 'facil',
          'opcoes': {'A': 'Missão', 'B': 'Cultura', 'C': 'Curso superior', 'D': 'Culinária'},
          'correta': 'B'},

         {'titulo': 'Qual destes termos menos tem relação com o fenômeno da globalização?',
          'nivel': 'facil',
          'opcoes': {'A': 'Aculturação', 'B': 'Neoliberalismo', 'C': 'União Europeia', 'D': 'Caldeirão do Huck'},
          'correta': 'D'},

         {'titulo': 'Qual o feriado do aniversário da cidade de São Paulo?',
          'nivel': 'facil',
          'opcoes': {'A': '25 de Janeiro', 'B': '24 de Março', 'C': '9 de Julho', 'D': '12 de Novembro'},
          'correta': 'A'},

         {'titulo': 'Qual destas não é uma fruta?',
          'nivel': 'facil',
          'opcoes': {'A': 'Laranja', 'B': 'Maça', 'C': 'Tomate', 'D': 'Abacate'},
          'correta': 'B'},

         {'titulo': 'Em qual ano o TikTok atingiu 1 bilhão de usuários?',
          'nivel': 'facil',
          'opcoes': {'A': '2019', 'B': '2021', 'C': '2015', 'D': '2018'},
          'correta': 'B'},
         
         {'titulo': 'Qual destes não é um app com foco em streaming de vídeo?',
          'nivel': 'facil',
          'opcoes': {'A': 'Netflix', 'B': 'Disney Plus', 'C': 'TIDAL', 'D': 'HBO Max'},
          'correta': 'C'},

         {'titulo': 'Qual destes parques não se localiza em São Paulo?!',
          'nivel': 'facil',
          'opcoes': {'A': 'Ibirapuera', 'B': 'Parque do Carmo', 'C': 'Parque Villa Lobos', 'D': 'Morro da Urca'},
          'correta': 'D'},

         {'titulo': 'Qual destas não é uma linguagem de programação?',
          'nivel': 'facil',
          'opcoes': {'A': 'Miratdes', 'B': 'Python', 'C': 'Lua', 'D': 'C++'},
          'correta': 'A'},

         {'titulo': 'Dentre os listados, qual destes esportes é menos praticado no Brasil?',
          'nivel': 'facil',
          'opcoes': {'A': 'Natação', 'B': 'Vôlei', 'C': 'Ski Cross Country', 'D': 'Futebol'},
          'correta': 'C'},
         
         {'titulo': 'Qual o resultado da operação 5 + 2 * 3?',
          'nivel': 'medio',
          'opcoes': {'A': '21', 'B': '11', 'C': '30', 'D': '10'},
          'correta': 'B'},

         {'titulo': 'Qual destas é uma pseudociência que estuda os corpos celestes e as prováveis relações que possuem com a vida das pessoas e os acontecimentos na Terra?',
          'nivel': 'medio',
          'opcoes': {'A': 'Astronomia', 'B': 'Física quântica', 'C': 'Astrologia', 'D': 'Computação'},
          'correta': 'C'},

         {'titulo': 'Qual destas não foi considerada em 2007 uma das sete maravilhas do mundo moderno?',
          'nivel': 'medio',
          'opcoes': {'A': 'Muralha da China', 'B': 'Machu Picchu', 'C': 'Cristo Redentor', 'D': 'Torre Eiffel'},
          'correta': 'D'},

         {'titulo': 'Qual destas pessoas conduziu importantes estudos sobre radioatividade, sendo ganhadora de dois prêmios Nobel?',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Paul Erdős', 'C': 'Clive W.J. Granger', 'D': 'Maria Ressa'},
          'correta': 'A'},

         {'titulo': 'Quem é considerada a primeira pessoa programadora do mundo?!',
          'nivel': 'medio',
          'opcoes': {'A': 'Marie Curie', 'B': 'Alan Turing', 'C': 'Ada Lovelace', 'D': 'Edsger Dijkstra'},
          'correta': 'C'},

         {'titulo': 'Qual destes números é primo?',
          'nivel': 'medio',
          'opcoes': {'A': '259', 'B': '85', 'C': '49', 'D': '19'},
          'correta': 'D'},

         {'titulo': 'Na Conjectura de _______, escolhendo-se um número natural inicial n, onde n > 0, os seguintes critérios serão obedecidos: Se n for par o seu sucessor será a metade e se n for ímpar o seu sucessor será o triplo mais um, gerando então um novo número. Qual o nome da conjectura?',
          'nivel': 'medio',
          'opcoes': {'A': 'Collatz', 'B': 'Goldbach', 'C': 'Poincaré', 'D': 'Hodge'},
          'correta': 'A'},

         {'titulo': 'Como faço para chamar o SAMU?',
          'nivel': 'medio',
          'opcoes': {'A': 'Ligue 101', 'B': 'Ligue 192', 'C': 'Ligue 109', 'D': 'Ligue 122'},
          'correta': 'B'},

         {'titulo': 'Qual a segunda pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Kylie Jenner'},
          'correta': 'D'},

         {'titulo': 'Qual a pessoa mais seguida no Instagram?',
          'nivel': 'medio',
          'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Lionel Messi'},
          'correta': 'A'},

         {'titulo': 'A reprodução dos seres vivos é um processo biológico através do qual os organismos geram descendência. Qual desta não é uma forma de reprodução assexuada?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Autogamia', 'B': 'Esporulação', 'C': 'Partenogênese', 'D': 'Divisão binária'},
          'correta': 'A'},

         {'titulo': 'Qual o resultado da operação 5 + 2 * 3 ^ 2, onde ^ representa potenciação?',
          'nivel': 'dificil',
          'opcoes': {'A': '441', 'B': '86', 'C': 'Nenhuma das outras respostas', 'D': '23'},
          'correta': 'D'},

         {'titulo': 'Quem é Oxóssi?!',
          'nivel': 'dificil',
          'opcoes': {'A': 'Rede de mercados', 'B': 'Tipo de poema Dissílabo', 'C': 'Divindade das religiões africanas', 'D': 'Trapper brasileiro'},
          'correta': 'C'},

         {'titulo': 'Qual a altura do Cristo Redentor?',
          'nivel': 'dificil',
          'opcoes': {'A': 'entre 0 e 20 metros', 'B': 'Entre 21 e 40 metros', 'C': 'Entre 41 e 60 metros', 'D': 'Mais que 60 metros'},
          'correta': 'B'},

         {'titulo': 'Em que ano faleceu Charles Babbage?',
          'nivel': 'dificil',
          'opcoes': {'A': '2022', 'B': '1791', 'C': '1935', 'D': '1871'},
          'correta': 'A'},

         {'titulo': 'Einstein foi Nobel de física em qual ano?',
          'nivel': 'dificil',
          'opcoes': {'A': '1906', 'B': '1905', 'C': '1920', 'D': '1921'},
          'correta': 'D'},

         {'titulo': 'Qual o número atômico do nitrogênio?',
          'nivel': 'dificil',
          'opcoes': {'A': '9', 'B': '7', 'C': '6', 'D': '8'},
          'correta': 'B'},

         {'titulo': 'Qual o ponto de fusão do nitrogênio?',
          'nivel': 'dificil',
          'opcoes': {'A': '120º C', 'B': '15º C', 'C': '-210º C', 'D': '-180º C'},
          'correta': 'C'},
         
         {'titulo': 'Quantos gols Pelé fez oficialmente?',
          'nivel': 'dificil',
          'opcoes': {'A': '815', 'B': '762', 'C': '1100', 'D': '1057'},
          'correta': 'B'},

         {'titulo': 'O que é Necrose?',
          'nivel': 'dificil',
          'opcoes': {'A': 'Uma banda de Rock', 'B': 'Uma marca de luxo', 'C': 'Cidade Francesa', 'D': 'Morte de tecido orgânico'},
          'correta': 'D'}
        ]


trans_base = transforma_base(questoes)
lista_p = [1000,5000,10000,30000,50000,100000,300000,500000,1000000]
lista_sorteadas = []
'''w = 0
if trans_base["facil"]:
    for i in range(len(trans_base['facil'])):
        valida1= (valida_questoes(trans_base["facil"]))
        for j in range(len(valida1)):
          if valida1[j] != {}:
            del valida1[j]
    while w < len(lista_p):
      for k in range(len(trans_base['facil'])):
        sorteia = sorteia_questao_inedita(trans_base,'facil',lista_sorteadas)
        lista_sorteadas.append(sorteia)
        print(questao_para_texto(sorteia,k+1))
        resposta=input("Qual a sua resposta? ")
        if resposta == trans_base['facil'][k]['correta']:
          print("Você acertou! Seu prêmio atual é de R$ {:.2f}".format(lista_p[w]))
          if sorteia in lista_sorteadas:
            sorteia_inedita=sorteia_questao_inedita(trans_base,'facil',lista_sorteadas)
            print(questao_para_texto(sorteia_inedita,k+1))
          else:
            sorteia = sorteia_questao(trans_base,'facil')
            lista_sorteadas.append(sorteia)
            print(questao_para_texto(sorteia,k+1))
            resposta=input("Qual a sua resposta? ")
      else:
            print('Que pena! Você errou e vai sair sem nada :(')
      break;'''
      
trans_base = transforma_base(questoes)
lista_p = [1000,5000,10000,30000,50000,100000,300000,500000,1000000]
lista_sorteadas = []
w = 0
lista_sorteadas1 = []
lista_sorteadas2 = []
lista_sorteadas3 = []
continuar = True
pontuacao = 0

while continuar:
  #if trans_base['facil']:

  for k in range(len(trans_base['facil'])):
    valida1 =  valida_questoes(trans_base['facil'][k])
    if valida1 != {}:
      del valida1

  for y in range(len(trans_base['medio'])):

    valida2 =  valida_questoes(trans_base['medio'][y])
    if valida2 != {}:
      del valida2
  for z in range(len(trans_base['dificil'])):

    valida3 =  valida_questoes(trans_base['dificil'][z])
    if valida3 != {}:
      del valida3

  while w < len(lista_p):

    if pontuacao < 10000:
      sorteia_inedita = sorteia_questao_inedita(trans_base,'facil',lista_sorteadas1)
      lista_sorteadas1.append(sorteia_inedita)
      print(questao_para_texto(sorteia_inedita,k+1))
      resposta=input("Qual a sua resposta? ")
    
      if resposta != trans_base['facil'][k]['correta']:
        print('Que pena! Você errou e vai sair sem nada :(')
        continuar = False
      else:
        pontuacao = lista_p[w]
        print("Você acertou! Seu prêmio atual é de R$ {:.2f}".format(pontuacao))
        w+=1

    elif pontuacao == 10000:
      #if pontuacao == 10000:
      sorteia_inedita2 = sorteia_questao_inedita(trans_base,'medio',lista_sorteadas2)
      lista_sorteadas2.append(sorteia_inedita)
      print(questao_para_texto(sorteia_inedita,y+1))
      resposta=input("Qual a sua resposta? ")

      if resposta != trans_base['medio'][y]['correta']:
        print('Que pena! Você errou e vai sair sem nada :(')
        continuar = False

      else:
        if pontuacao == 100000:
          sorteia_inedita3 = sorteia_questao_inedita(trans_base,'dificil',lista_sorteadas3)
          lista_sorteadas3.append(sorteia_inedita)
          print(questao_para_texto(sorteia_inedita,z+1))
          resposta=input("Qual a sua resposta? ")
          if resposta != trans_base['medio'][z]['correta']:
            print('Que pena! Você errou e vai sair sem nada :(')
            continuar = False
          else:
            if pontuacao == 1000000:
              print("Voce ganhou!")
              continuar = False
        else:
          pontuacao = lista_p[w]
          print("Você acertou! Seu prêmio atual é de R$ {:.2f}".format(pontuacao))
          w+=1
  











            #resposta=input("Qual a sua resposta? ")
            #if resposta == trans_base['facil'][k]['correta']:
              #print("Você acertou! Seu prêmio atual é de R$ {:.2f}".format(lista_p[w]))
            #if sorteia in lista_sorteadas:
              
              #sorteia_inedita=sorteia_questao_inedida(trans_base,'facil',lista_sorteadas)
              #print(sorteia_questao_inedida)

