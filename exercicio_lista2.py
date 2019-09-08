#2 Faça um programa que percorre uma lista com o seguinte formato: [['Brasil', 'Italia',
#[10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7,8]]]. Essa lista indica o
#número de faltas que cada time fez em cada jogo. Na lista acima, no jogo entre Brasil
#e Itália, o Brasil fez 10 faltas e a Itália fez 9.
#O programa deve imprimir na tela:
#- o total de faltas do campeonato
#- o time que fez mais faltas
#- o time que fez menos faltas
#-----------------------------------------------
#inicializacao de variaveis1--------------------
lista = [['Brasil', 'Italia', [10, 9]],
         ['Brasil', 'Espanha', [5, 7]],
         ['Italia', 'Espanha', [7,8]]]

itenA=0
acumulador=0
passo = 0
#---------------------------
#print(brasil, italia, espanha) #teste saida
#solucao do total-----------------------------
while(passo<3):
  itenA=lista[passo][2][0]
  acumulador = itenA+acumulador
  itenA=lista[passo][2][1]
  acumulador = itenA+acumulador
  #print (itenA) #teste saida
  #print (itenB) #teste saida
  #print("---------------") #teste saida
  passo = passo + 1
#--------------------------------------------
#inicializacao de variaveis 2
passo = 0
passo2 = 0
#aux = 0 #solucao2
buscaTime = 0
buscaFalta = 0
brasil = 0
espanha = 0
italia = 0
#----------------------------------------------
#solucao maior e menor

#dicionario = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #solucao2

while(passo2<2):
  while(passo<3):
    
    buscaTime = lista[passo][passo2]
    buscaFalta = lista[passo][2][passo2]
    
    if buscaTime == "Brasil":
      brasil = brasil + buscaFalta
    elif buscaTime == "Italia":
      italia += buscaFalta
    else:
      espanha += buscaFalta
    
    #print("----",brasil, italia, espanha,"---") #teste saida
    #print("----",passo) #teste saida
    #print(buscaTime) #teste saida
    #print(buscaFalta,) #teste saida
    #print("-----------") #teste saida
    
   # dicionario[aux*2] = buscaTime #solucao 2  
   # dicionario[(aux*2)+1] = buscaFalta # solucao 2
    #aux +=1
    passo = passo + 1
  passo2 = passo2+1
  passo = 0

maior = brasil
maiorStr = "brasil"
menor = brasil
menorStr = "brasil"

if maior <= espanha:
  maior = espanha
  maiorStr = "espanha"
else:
  menor = espanha
  menorStr = "espanha"

if maior <= italia :
  maior = italia
  maiorStr = "italia"
else:
  menor = italia
  menorStr = "italia"


print(brasil, italia, espanha)


print("-----------exercicio2-----------")
print("Total de faltas: ",acumulador)
print("Time que fez mais faltas: ", maiorStr)
print("Time que fez menos faltas: ", menorStr)
print("--------------------------------")
