# Escreva um programa que l�^ duas notas de v�rios alunos e armazena tais notas em um dicion�rio, em que a chave e� o nome do aluno. A entrada de dados deve terminar quando for lida uma string vazia como nome. A seguir, fa�a um loop que pede o nome do aluno e mostra sua me�dia.
dicionario = {}

nome = input("nome do aulo: ")
while nome != "":
  nota1 = float(input("digite a primeira nota: "))
  nota2 = float(input("digite a primeira nota: "))
  
  dicionario[nome] = (nota1+nota2)/2
      
  print(dicionario)
  print("------------------------")
  nome = input("\n nome do aulo: ")
  

print("fim",len(dicionario))
print("\n------------------------")
nomeBusca = input("nome do aulo: ")

print("media: ",dicionario[nomeBusca])