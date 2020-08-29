#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

print("nome:")
nome=str(input())
while len(nome) != 3:
    print("escreva novamente!")

print("idade:")
ida=int(input())
while len(str(ida)) > 150 :
    print("escreva novamente!")

print("salário")
sal=float(input())
while len(str(sal)) < 0:
    print("escreva novamente!")

print("sexo:f/m")
sex=str(input())
while sex!="f" and sex!="m":
    print("escreva novamente!")

print("Estado Civil: s/c/v/d")
s=str(input())
while s!="s" and s!="c" and s!="v" and s!="d":
    print("escreva novamente!")




