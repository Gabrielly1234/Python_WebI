#Faça um Programa que peça um número correspondente a um determinado ano 
# e em seguida informe se este ano é ou não bissexto.

print("quantos dias tem o ano?")
dias= int(input())

if dias == 366:
    print("É bissexto")
else:
    print("não é bissexto")