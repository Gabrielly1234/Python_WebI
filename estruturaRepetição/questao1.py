#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido 
# e continue pedindo até que o usuário informe um valor válido.

print("insira uma nota de 0 a 10")
nota= float(input())

while nota <0 or nota > 10:
    print("insira uma nota de 0 a 10")
    nota= float(input())
    print("valor inválido") 
  