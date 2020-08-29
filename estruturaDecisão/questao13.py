#Faça um Programa que leia um número e exiba o dia correspondente da semana. 
# (1-Domingo, 2- Segunda, etc.), 
# se digitar outro valor deve aparecer valor inválido.

print("Dia da semana:")
dia=int(input())

semana=[
 "teste",
 "domingo",
 "segunda",
 "terça",
 "quarta",
 "quinta",
 "sexta",
 "sábado"
]
print (semana[dia])