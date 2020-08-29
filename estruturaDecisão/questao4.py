#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

print("letra:")
letra= str(input())

vogal= [
    "a","e","i", "o", "u"
]

for test in vogal:

   if ( test== letra):
     print (letra,"é volgal")
   else:
      print (letra,"é consoante")
   