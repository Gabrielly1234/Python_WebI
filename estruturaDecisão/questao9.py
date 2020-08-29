#Faça um Programa que leia três números e mostre-os em ordem decrescente.
print("num1:")
num1=int(input())
print("num2:")
num2=int(input())
print("num3:")
num3=int(input())

maior=0
if num1>num2 and num1>num3:
    maior=num1
if num2> num1 and num2>num3:
    maior=num2
if num3> num1 and num3>num2:
    maior= num3

menor=0
if num1<num2 and num1<num3:
    menor=num1
if num2<num1 and num2<num3:
    menor=num2
if num3<num1 and num3<num2:
    menor= num3

neutro=0
if num1<maior and num1>menor:
    neutro=num1
if num2<maior and num2>menor:
    neutro=num2
if num3!=maior and num3>menor:
    neutro=num3

print(maior, neutro, menor)