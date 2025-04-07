nbr_d_apparition=0
chaine=input("quelle est ta chaine de caractère?: ")
lettre=input("quelle est la lettre dont tu veux savoir le nombre d apparition?:")
if lettre in chaine :
    for i in range(len(chaine)):
        if chaine[i]==lettre:
            nbr_d_apparition+=1
print(str(lettre)+" apparait "+str(nbr_d_apparition))
  