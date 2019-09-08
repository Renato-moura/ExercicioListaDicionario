#2 Uma pista de Kart permite 10 voltas para cada um de 6 corredores. Escreva um programa que leia todos os tempos em segundos e os guarde em um dicionário, em que a chave e´ o nome do corredor. Ao final diga de quem foi a melhor volta da prova e em que volta; e ainda a classificação final em ordem (1o o campeão). O campeão e´ o que tem a menor media de tempos.

lista = []
piloto0 = {}
piloto1 = {}

corredor = 0
while corredor < 2:
  volta = 0
  registro = {}
  registroLista = {}

  print("----------------------------------")
  nome = input("nome do piloto ("+str(corredor+1)+") : ") 

  
  while volta < 2:  
   
     
    print("volta de numero: "+str(volta+1))
    tempo = int(input("tempo em segundos: "))
    
    registroLista[volta] = tempo
    #registroLista["volta"+str(volta)] = volta
    registro[nome]=registroLista

    if corredor == 0:
     piloto0 = registro.copy()
    elif corredor == 1:
      piloto1 = registro.copy()  
    
    print("piloto0: ",piloto0)
    print("--------------------")
    print("piloto1: ",piloto1)
    print("--------------------")
    print("corredor :",corredor)
    print("--------------------")

    volta +=1
  lista.append(nome) 
  corredor += 1
  print("----------------------------------")


media=0
piloto=""
pilotoTempo=""
soma = 0
faster = 0
voltaRec = 0
j=0
while j<2:
  i=0

  while i<2 :
  
    faster = piloto0[lista[j]][i]
    piloto = lista[j]
    voltaRec = i

    if piloto0[lista[j]][i] < faster:
      faster = piloto0[lista[j]][i]
      piloto = lista[j]
      voltaRec = i

    soma += piloto0[lista[j]][i]
    

    i+=1

  media = soma = soma/len(lista)
  pilotoTempo = lista[j]

  if media < soma:
    media = soma
    pilotoTempo = lista[j]

  j+=1
print(faster,piloto,voltaRec)
print(media, pilotoTempo)