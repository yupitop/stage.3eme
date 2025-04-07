premier_chiffre=int(input("premier nombre/chiffre: "))
deuxieme_chiffre=int(input("deuxieme nombre/chiffre: "))
operation=input("operation: ")
if operation=="/" :
    print(premier_chiffre/deuxieme_chiffre)
elif operation=="*":
    print(premier_chiffre*deuxieme_chiffre)
elif operation=="+":
    print(premier_chiffre+deuxieme_chiffre) 
elif operation=="-":
    print(premier_chiffre-deuxieme_chiffre)
else:
    print("un probleme est survenu" )
  
  