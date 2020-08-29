#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" 
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
#Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
#entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente"

print("Telefonou para a vítima? s/n")
resp1=str(input())
print ("Esteve no local do crime? s/n")
resp2= str(input())
print ("Mora perto da vítima? s/n")
resp3= str(input())
print("Devia para a vítima? s/n")
resp4= str(input())
print ("Já trabalhou com a vítima? s/n")
resp5= str(input())

resposta=0
if resp1=="s":
    resposta= resposta+1
if resp2=="s":
    resposta= resposta+1
if resp3=="s":
    resposta= resposta+1
if resp4=="s":
    resposta= resposta+1
if resp5=="s":
    resposta= resposta+1

total= resposta

if total > 2:
    print("Suspeito")
if total > 3 and total<4:
    print("Cúmplice")
if total==5:
    print("Assasino")
if total <2:
    print("inocente")