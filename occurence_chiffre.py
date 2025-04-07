nombre=0
chiffre=0
def nombre_chiffres():
   nombre=input("nombre: ") 
   chiffre=input("chiffre: ")
   occurence=str(nombre).count(str(chiffre))
   return(occurence)
print(nombre_chiffres())
    
