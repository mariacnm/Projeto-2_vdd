from random import randint
def gera_ajuda(questao):
    sorteia_numero=randint(1,2)
    if sorteia_numero == 1:
        sorteia=( ["A","B","C","D"][randint(0,3)])

        if sorteia != questao["correta"]:
            ajuda=questao["opcoes"][sorteia]
            resposta="'''DICA:\n""Opções certamente erradas: {0}'''".format(ajuda)
        else:
            return ""
    else: 
        sorteia=( ["A","B","C","D"][randint(0,3)])

        if sorteia != questao["correta"]:
            ajuda=questao["opcoes"][sorteia]
            ajuda2=questao["opcoes"][sorteia]
            resposta="'DICA: ""Opções certamente erradas: {0} | {1}'".format(ajuda,ajuda2)
        else:
            return ""
    return resposta



questao={
  "titulo": "Qual destes parques não se localiza em São Paulo?!",
  "nivel": "facil",
  "opcoes": {
    "A": "Ibirapuera",
    "B": "Parque do Carmo",
    "C": "Parque Villa Lobos",
    "D": "Morro da Urca"
  },
  "correta": "D"
}
print(gera_ajuda(questao))