#Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.

print("digite um número:")
num=int(input())
if num > 0:
    print(int(str(num)[::-1]))
    