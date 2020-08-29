#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina 
# ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:# Média de Aproveitamento  Conceito
#Entre 9.0 e 10.0        A
#Entre 7.5 e 9.0         B
#Entre 6.0 e 7.5         C
#Entre 4.0 e 6.0         D
#Entre 4.0 e zero        E

print("insira a nota1:")
nota1=float(input())

print ("insira a nota2:")
nota2= float(input())

soma= nota1+nota2
media= soma/2

if media > 9.0 and media<10.0:
      print("A")
if media > 7.5 and media<9.0:
      print("B")
if media > 6.0 and media<7.5:
      print("C")
if media > 4.0 and media<6.0:
      print("D")
if media > 0 and media<4.0:
      print("E")