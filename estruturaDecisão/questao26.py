#Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#Álcool:
#até 20 litros, desconto de 3% por litro, acima de 20 litros, desconto de 5% por litro
#Gasolina:
#até 20 litros, desconto de 4% por litro - acima de 20 litros, desconto de 6% por 
# litro Escreva um algoritmo que leia o número de litros vendidos, 
#o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina)
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 
#o preço do litro do álcool é R$ 1,90.


print("O que deseja? A/G")
resp=str(input())
print("Quantos litros?:")
quantlitro=int(input())
gasolina= 2.50
alcool=1.90
valor=0
des=0
conta=0
if resp == "G":
  valor=gasolina
  #--------calculando o desconto----------
  if quantlitro < 20: 
    conta= valor*0.04
    des=conta*quantlitro
  if quantlitro >20: 
    conta=valor*0.06
    des=conta*quantlitro

if resp == "A":
    valor=alcool
    if quantlitro<20:
         conta=valor*0.03
         des= conta*quantlitro
    if quantlitro>20:
        conta=valor*0.05
        des= conta*quantlitro 

cal= valor*quantlitro
total= cal- des

print ("-----", total)

