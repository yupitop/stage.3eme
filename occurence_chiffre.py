def nombre_chiffres():
   try:
       nombre=input("nombre : ")
       if not nombre.replace('.', '', 1).replace(',', '', 1).isdigit(): 
           print("Erreur : le nombre saisi contient des lettres")
           return
       chiffre=input("chiffre: ")
       occurence=str(nombre).count(str(chiffre))
       return(occurence)
   except ValueError:
       print("Erreur : le nombre saisi n'est pas un entier")

print(nombre_chiffres())
