#Faça um programa que calcule o número médio de alunos por turma. 
# Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
# As turmas não podem ter mais de 40 alunos.

print("quantidade de turmas:")
quant=int(input())

i=0
soma=0
for i in range (quant):
    print("quantidade de aluno:")
    quantalu=int(input())
    
    if quantalu <= 40:
        soma=soma+quantalu
    else: 
        print("tente novamente")
media=soma/quant 
print("média de alunos por turma:", media)
