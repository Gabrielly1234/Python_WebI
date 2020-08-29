#Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs
#  e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs 
# e o valor para em cada um.


print("quant cd:")
quant= int(input())
i=0
soma=0
for i in range (quant):
    print(" valor:")
    valor=float(input())
    soma=soma+valor
media=soma/quant

print("valor investido:", soma)
print("valor médio:", media)