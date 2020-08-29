#Faça um Programa que leia três números e mostre o maior deles.

print("primeiro num:")
num1=int(input())

print("segundo num:")
num2=int(input())

print("terceiro num:")
num3=int(input())

maior=0
menor=0

if num1>num2 and num1>num3:
    maior=num1
if num2> num1 and num2>num3:
    maior=num2
if num3> num1 and num3>num2:
    maior= num3

print ("o maior num é:", maior)