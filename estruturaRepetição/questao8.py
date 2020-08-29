#Faça um programa que leia 5 números e informe a soma e a média dos números.
i=0
soma=0
for i in range (5):
    print("insira um número:")
    num=int(input())
    soma= soma+num 

print(" soma:",soma)
media=soma/5
print("média:",media)

