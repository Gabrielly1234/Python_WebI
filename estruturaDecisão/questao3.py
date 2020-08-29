#Faça um Programa que verifique se uma letra digitada é "F" ou "M".
#  Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

print("indique seu sexo:")
sex=str(input())

if sex!= "f" and sex!= "m":
    print("sex inválido")
else:
    print("sex válido")
