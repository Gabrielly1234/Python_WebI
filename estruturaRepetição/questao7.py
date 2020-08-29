#Faça um programa que leia 5 números e informe o maior número.

i=0
maior= -9999
for i in range(5):
    print("informe 5 números:")
    num= int(input())
    if num> maior:
        maior=num
print(maior)
