def valida_questao(questao):
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
