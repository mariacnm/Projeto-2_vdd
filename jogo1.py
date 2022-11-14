import random
from random import randint
from funcoes import transforma_base
from funcoes import valida_questoes
from funcoes import sorteia_questao
from funcoes import questao_para_texto
from funcoes import sorteia_questao_inedita
from funcoes import gera_ajuda
from colorama import Fore, Back, Style, init, deinit


questoes=[   {'titulo': 'Qual o resultado da operação 57 + 32?',
    'nivel': 'facil',
    'opcoes': {'A': '-19', 'B': '85', 'C': '89', 'D': '99'},
    'correta': 'C'},

    {'titulo': 'Qual a capital do Brasil?',
    'nivel': 'facil',
    'opcoes': {'A': 'Brasília', 'B': 'Rio de janeiro', 'C': 'São Paulo', 'D': 'Osasco'},
    'correta': 'A'},

    {'titulo': 'De onde a cantora Billie Eilish é?:',
    'nivel': 'facil',
    'opcoes': {'A': 'Brasília', 'B': 'Los Angeles', 'C': 'California', 'D': 'Nova Iorque'},
    'correta': 'B'},

    {'titulo': 'De onde a cantora Billie Eilish é?',
    'nivel': 'facil',
    'opcoes': {'A': 'California', 'B': 'Los Angeles', 'C': 'New york', 'D': 'Washington'},
    'correta': 'D'},

    {'titulo': 'qual a capital dos Estados Unidos da América?',
    'nivel': 'facil',
    'opcoes': {'A': 'Brasília', 'B': 'Los Angeles', 'C': 'California', 'D': 'Nova Iorque'},
    'correta': 'B'},
    
    {'titulo': 'qual seleção contem mais titulos da Copa do Mundo de futebol?',
    'nivel': 'facil',
    'opcoes': {'A': 'Brasil', 'B': 'Argentina', 'C': 'Alemanha', 'D': 'Italia'},
    'correta': 'B'},

    {'titulo': 'De qual cidade vieram os Beatles?:',
    'nivel': 'facil',
    'opcoes': {'A': 'Liverpool', 'B': 'São francisco', 'C': 'Miami', 'D': 'San Diego'},
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
    'correta': 'C'},

    {'titulo': 'Em qual ano o TikTok atingiu 1 bilhão de usuários?',
    'nivel': 'facil',
    'opcoes': {'A': '2019', 'B': '2021', 'C': '2015', 'D': '2018'},
    'correta': 'B'},
    
    {'titulo': 'Qual destes não é um app com foco em streaming de vídeo?',
    'nivel': 'facil',
    'opcoes': {'A': 'Netflix', 'B': 'Disney Plus', 'C': 'TIDAL', 'D': 'HBO Max'},
    'correta': 'C'},

    {'titulo': 'Qual é o país mais populoso do mundo?:',
    'nivel': 'facil',
    'opcoes': {'A': 'China', 'B': 'Brasil', 'C': 'Estados Unidos', 'D': 'Russia'},
    'correta': 'A'},

    {'titulo': 'Qual destes parques não se localiza em São Paulo?!',
    'nivel': 'facil',
    'opcoes': {'A': 'Ibirapuera', 'B': 'Parque do Carmo', 'C': 'Parque Villa Lobos', 'D': 'Morro da Urca'},
    'correta': 'D'},

    {'titulo': 'Qual destas não é uma linguagem de programação?',
    'nivel': 'facil',
    'opcoes': {'A': 'Miratdes', 'B': 'Python', 'C': 'Lua', 'D': 'C++'},
    'correta': 'A'},

    {'titulo': 'Em que ano o homem pisou na lua?',
    'nivel': 'facil',
    'opcoes': {'A': '1969', 'B': '1980', 'C': '1960', 'D': '1970'},
    'correta': 'A'},

    {'titulo': 'Em qual cidade está o monumento Coliseu, também conhecido como Anfiteatro Flaviano?',
    'nivel': 'facil',
    'opcoes': {'A': 'Roma', 'B': 'Los Angeles', 'C': 'São Paulo', 'D': 'Washington'},
    'correta': 'A'},

    {'titulo': 'Dentre os listados, qual destes esportes é menos praticado no Brasil?',
    'nivel': 'facil',
    'opcoes': {'A': 'Natação', 'B': 'Vôlei', 'C': 'Ski Cross Country', 'D': 'Futebol'},
    'correta': 'C'},

    {'titulo': 'Quem é o autor da série literária Sítio do Picapau Amarelo?',
    'nivel': 'facil',
    'opcoes': {'A': 'Monteiro Lobato', 'B': 'Chico Buarque', 'C': 'Mauricio de souza', 'D': 'Anitta Malfatti'},
    'correta': 'A'},

    {'titulo': 'Quantas teclas há em um piano clássico?:',
    'nivel': 'facil',
    'opcoes': {'A': '70', 'B': '80', 'C': '88', 'D': '95'},
    'correta': 'C'},
    
    {'titulo': 'Qual o resultado da operação 5 + 2 * 3?',
    'nivel': 'medio',
    'opcoes': {'A': '21', 'B': '11', 'C': '30', 'D': '10'},
    'correta': 'B'},

    {'titulo': 'Em que ano aconteceu o acidente na Usina Nuclear de Chernobyl?',
    'nivel': 'medio',
    'opcoes': {'A': '1979', 'B': '1986', 'C': '1984', 'D': '1980'},
    'correta': 'B'},


    {'titulo': 'Qual destas é uma pseudociência que estuda os corpos celestes e as prováveis relações que possuem com a vida das pessoas e os acontecimentos na Terra?',
    'nivel': 'medio',
    'opcoes': {'A': 'Astronomia', 'B': 'Física quântica', 'C': 'Astrologia', 'D': 'Computação'},
    'correta': 'C'},
    
    {'titulo': 'Qual é o ponto mais alto do mundo?',
    'nivel': 'medio',
    'opcoes': {'A': 'Monte Verde', 'B': 'Monte Everest', 'C': 'Monte Urais', 'D': 'Montes Claros'},
    'correta': 'B'},

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

    {'titulo': 'Qual é o planeta mais próximo do sol?',
    'nivel': 'medio',
    'opcoes': {'A': 'Neturno', 'B': 'Saturno', 'C': 'Mercúrio', 'D': 'Jupiter'},
    'correta': 'C'},

    {'titulo': 'Qual destes números é primo?',
    'nivel': 'medio',
    'opcoes': {'A': '259', 'B': '85', 'C': '49', 'D': '19'},
    'correta': 'D'},

    {'titulo': 'Quem pintou o quadro Mona Lisa?:',
    'nivel': 'medio',
    'opcoes': {'A': 'Picasso', 'B': ' Leonardo Da Vinci', 'C': 'Pablo Pierre', 'D': 'Van Gogh'},
    'correta': 'B'},


    {'titulo': 'Na Conjectura de _______, escolhendo-se um número natural inicial n, onde n > 0, os seguintes critérios serão obedecidos: Se n for par o seu sucessor será a metade e se n for ímpar o seu sucessor será o triplo mais um, gerando então um novo número. Qual o nome da conjectura?',
    'nivel': 'medio',
    'opcoes': {'A': 'Collatz', 'B': 'Goldbach', 'C': 'Poincaré', 'D': 'Hodge'},
    'correta': 'A'},

    {'titulo': 'Como faço para chamar o SAMU?',
    'nivel': 'medio',
    'opcoes': {'A': 'Ligue 101', 'B': 'Ligue 192', 'C': 'Ligue 109', 'D': 'Ligue 122'},
    'correta': 'B'},

    {'titulo': 'Qual parte da planta é responsável pela fotossíntese?',
    'nivel': 'medio',
    'opcoes': {'A': 'Caule', 'B': 'Folha', 'C': 'Cabo', 'D': 'Sintonela'},
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

    {'titulo': 'Quando é verão no Brasil, qual é a estação do ano na Europa?',
    'nivel': 'dificil',
    'opcoes': {'A': 'Verão', 'B': 'Outono', 'C': 'Inverno', 'D': 'Primavera'},
    'correta': 'C'},

    {'titulo': 'Qual foi a série mais assistida da Netflix em 2019?',
    'nivel': 'dificil',
    'opcoes': {'A': 'Cobra Kai', 'B': 'The Sandman', 'C': 'Stranger things', 'D': 'Lendas do Amanha'},
    'correta': 'C'},

    {'titulo': 'Qual a altura do Cristo Redentor?',
    'nivel': 'dificil',
    'opcoes': {'A': 'entre 0 e 20 metros', 'B': 'Entre 21 e 40 metros', 'C': 'Entre 41 e 60 metros', 'D': 'Mais que 60 metros'},
    'correta': 'B'},

    {'titulo': 'Em que ano faleceu Charles Babbage?',
    'nivel': 'dificil',
    'opcoes': {'A': '2022', 'B': '1791', 'C': '1935', 'D': '1871'},
    'correta': 'A'},

    {'titulo': 'Quais são as cores dos anéis olímpicos?',
    'nivel': 'dificil',
    'opcoes': {'A': 'Azul, Amarelo, Preto, Verde, vermelho', 'B': 'Vermelho, Azul, Amarelo, Verde, Preto', 'C': 'Preto, Azul, Amarelo, Vermelho, Verde', 'D': 'Verde, Amarelo, Preto, Vermelho, Azul'},
    'correta': 'A'},

    {'titulo': 'Einstein foi Nobel de física em qual ano?',
    'nivel': 'dificil',
    'opcoes': {'A': '1906', 'B': '1905', 'C': '1920', 'D': '1921'},
    'correta': 'D'},

    {'titulo': 'Como a Nike era chamada inicialmente?:',
    'nivel': 'dificil',
    'opcoes': {'A': 'Blue Ribbon Sports', 'B': 'Spide guer Sports', 'C': 'IUB Sports', 'D': 'Sports war'},
    'correta': 'A'},

    {'titulo': 'Qual o número atômico do nitrogênio?',
    'nivel': 'dificil',
    'opcoes': {'A': '9', 'B': '7', 'C': '6', 'D': '8'},
    'correta': 'B'},

    {'titulo': 'Qual é a cor da língua da girafa?',
    'nivel': 'dificil',
    'opcoes': {'A': 'Vermelha', 'B': 'Roxa', 'C': 'Preta', 'D': 'Laranja'},
    'correta': 'B'},

    {'titulo': 'Qual esporte pratica o atleta inglês David Beckham?',
    'nivel': 'dificil',
    'opcoes': {'A': 'Basquete', 'B': 'Futebol', 'C': 'Natação', 'D': 'Corrida'},
    'correta': 'B'},

    {'titulo': 'Qual o ponto de fusão do nitrogênio?',
    'nivel': 'dificil',
    'opcoes': {'A': '120º C', 'B': '15º C', 'C': '-210º C', 'D': '-180º C'},
    'correta': 'C'},
    
    {'titulo': 'Quantos gols Pelé fez oficialmente?',
    'nivel': 'dificil',
    'opcoes': {'A': '815', 'B': '762', 'C': '1100', 'D': '1057'},
    'correta': 'B'},

    {'titulo': 'Qual é o ingrediente base da bebida japonesa saquê?',
    'nivel': 'dificil',
    'opcoes': {'A': 'Salmão', 'B': 'Arroz', 'C': 'Shoyu', 'D': 'Miso'},
    'correta': 'B'},

    {'titulo': 'Qual é o livro mais vendido do mundo, depois da Bíblia?',
    'nivel': 'dificil',
    'opcoes': {'A': 'Odisseia', 'B': 'O Mundo se Despedaça ', 'C': 'As Mil e Uma Noites', 'D': 'Dom Quixote'},
    'correta': 'D'},

    {'titulo': 'quantos livros Sócrates escreveu?',
    'nivel': 'dificil',
    'opcoes': {'A': '23', 'B': '18', 'C': '19', 'D': '0'},
    'correta': 'D'},

    {'titulo': 'O que é Necrose?',
    'nivel': 'dificil',
    'opcoes': {'A': 'Uma banda de Rock', 'B': 'Uma marca de luxo', 'C': 'Cidade Francesa', 'D': 'Morte de tecido orgânico'},
    'correta': 'D'}
]

#começando o jogo perguntando o nome
#começando o jogo perguntando o nome
print("Olá! você esta na Fortuna DesSfotf e terá a oportunidade de enriquecer!")
nome=input("Qual seu nome? ")
print(Fore.YELLOW + "ok {0}, você tem direito a pular 3 vezes e 2 ajudas!\n".format(nome.upper())+ Fore.RESET)

#enter
input("Aperte ENTER para continuar....\n")

#o jogo vai começar
print("O jogo já vai começar! Lá vem a primeira questão!\n")
print(Fore.RED +"Vamos começar com a questões do nível FÁCIL!"+ Fore.RESET)
input("Aperte ENTER para continuar....\n")

trans_base = transforma_base(questoes)
lista_p = [1000,5000,10000,30000,50000,100000,300000,500000,1000000]
lista_sorteadas = []
continuar = True
pontuacao = 0
id = 1
ajuda = 2 
total1 = 0
pulo = 3
total2 = 0
loop=True


while loop:
  while continuar:
    trans_base = transforma_base(questoes)
    for i in range(len(lista_p)):
      if pontuacao == 0 or pontuacao == 1000 or pontuacao == 5000:
        sorteia_inedita = sorteia_questao_inedita(trans_base,'facil',lista_sorteadas)
      if pontuacao == 10000:
        print(Fore.RED+"\nHEY! Você passou para o nível MÉDIO!"+ Fore.RESET)
      if pontuacao == 10000 or pontuacao == 30000 or pontuacao == 50000 or pontuacao == 100000:
        sorteia_inedita = sorteia_questao_inedita(trans_base,'medio',lista_sorteadas)
      if pontuacao == 100000:
        print(Fore.RED+ "\nHEY! Você passou para o nível DIFÍCIL!"+ Fore.RESET)
      if pontuacao == 100000 or pontuacao == 300000 or pontuacao == 500000:
        sorteia_inedita = sorteia_questao_inedita(trans_base,'dificil',lista_sorteadas)
      if pontuacao == 1000000:
        print(Fore.GREEN+"PARABÉNS, você zerou o jogo e ganhou um milhão de reais!"+Fore.RESET)
        continuar = False
        break

      print(questao_para_texto(sorteia_inedita,id))
      resposta=input(Fore.GREEN+"Qual a sua resposta? "+Fore.RESET).upper()
      while resposta not in sorteia_inedita['opcoes'] and resposta != 'AJUDA' and resposta != 'PARAR' and resposta != 'PULA':
        print('Opcão inválida')
        print("As opções de resposta são 'A', 'B', 'C', 'D', 'ajuda', 'pula' e 'parar'!")
        resposta = input(Fore.GREEN+"Qual a sua resposta? "+Fore.RESET).upper()

      if resposta == 'AJUDA':
        if ajuda > 1:
          total1 = ajuda - 1
          print("\nOk,lá vem ajuda! Você ainda tem {} ajudas!".format(total1))
          input("Aperte ENTER para continuar...\n")
          print(gera_ajuda(sorteia_inedita))
          input("Aperte ENTER para continuar...\n")
          print(questao_para_texto(sorteia_inedita,id))
          resposta = input(Fore.GREEN+"Qual a sua resposta? "+Fore.RESET).upper()
          while resposta == "AJUDA":
            print('Não deu! Você já pediu ajuda nessa questão')
            input('Aperte ENTER para continuar...')
            resposta = input(Fore.GREEN+"Qual a sua resposta? "+Fore.RESET).upper()

        if ajuda == 1:
          print("Ok,lá vem ajuda! ATENÇÃO: você não tem mais direito a ajudas!")
          input("Aperte ENTER para continuar...\n")
          print(gera_ajuda(sorteia_inedita))
          input("Aperte ENTER para continuar...\n")
          print(questao_para_texto(sorteia_inedita,id))
          resposta = input("Qual sua resposta?").upper()
          while resposta == "AJUDA":
              print("Não deu! Você já pediu ajuda nessa questão")
              input("Aperte ENTER para continuar...")
              resposta = input(Fore.GREEN+"Qual a sua resposta? "+Fore.RESET).upper()
              ajuda += 1

        if ajuda == 0:
          print('Não deu! Você não tem mais direito a ajudas!')
          enter = input("Aperte ENTER para continuar...\n")
          print(questao_para_texto(sorteia_inedita,id))
          resposta = input("Qual sua resposta?").upper()
          while resposta == "AJUDA":
            print('Não deu! Você já pediu ajuda nessa questão')
            input('Aperte ENTER para continuar...')
            resposta = input(Fore.GREEN+"Qual a sua resposta? "+Fore.RESET).upper()
            ajuda += 1
        ajuda-=1

      if resposta == "PARAR":
          parar = input("Deseja mesmo para [S/N]?? Caso responda 'S', sairá com R${:.2f}!".format(lista_p[i- 1])).upper()
          while parar != "S" and parar != "N":
              print("Opção inválida")
              parar = input("Deseja mesmo para [S/N]?? Caso responda 'S', sairá com R${0}.00!".format(lista_p[i-1]))
          if parar == "S":
              print("Ok! Você parou e seu prêmio é de R${0}.00".format(lista_p[i-1]))
              continuar = False
              break           
          if parar == "N":
              print(questao_para_texto(sorteia_inedita,id))
              resposta = input(Fore.GREEN+"Qual a sua resposta? "+Fore.RESET).upper()

      if resposta == 'PULA':
          while pulo > 0:
              if pulo <= 3 and pulo != 1:
                total2 = pulo - 1
                print("\nOk, pulando! Você ainda tem {} pulos!".format(total2))
                input("Aperte ENTER para continuar...\n")
              if pontuacao == 0 or pontuacao == 1000 or pontuacao == 5000:
                sorteia_inedita = sorteia_questao_inedita(trans_base,'facil',lista_sorteadas)
              if pontuacao == 10000:
                print("\nHEY! Você passou para o nível MÉDIO!")
              if pontuacao == 10000 or pontuacao == 30000 or pontuacao == 50000 or pontuacao == 100000:
                sorteia_inedita = sorteia_questao_inedita(trans_base,'medio',lista_sorteadas)
              if pontuacao == 100000:
                print("\nHEY! Você passou para o nível DIFÍCIL!")
              if pontuacao == 100000 or pontuacao == 300000 or pontuacao == 500000:
                sorteia_inedita = sorteia_questao_inedita(trans_base,'dificil',lista_sorteadas)
              if pontuacao == 1000000:
                print(Fore.GREEN+"PARABÉNS, você zerou o jogo e ganhou um milhão de reais!"+Fore.RESET)
                continuar  = False
                break

              print(questao_para_texto(sorteia_inedita,id))
              resposta = input(Fore.GREEN+"Qual a sua resposta? "+Fore.RESET).upper()
              pulo -= 1

              if pulo == 1:
                total2 = pulo -1
                print("\nOk, pulando! ATENÇÃO: Você não tem mais direito a pulos!")
                enter = input("Aperte ENTER para continuar...\n")
              while resposta == 'PULA' and pulo == 0:
                print("\nVocê não tem mais direito a pulos!")
                resposta = input(Fore.GREEN+"Qual a sua resposta? "+Fore.RESET).upper()
              if resposta != 'PULA':
                break

      if resposta == sorteia_inedita['correta']:
        pontuacao = lista_p[i]
        print("Você acertou! Seu prêmio atual é de R${0}.00 :D".format(pontuacao))
        i += 1
      if resposta != sorteia_inedita['correta']: 
        print("Que pena! Você errou e vai sair sem nada :(")
        continuar = False
        break
    
      id +=1
      continuar 
      print("---------------------------------------------------------------------------")
      
