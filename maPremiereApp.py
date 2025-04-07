
 
from tkinter import * 

fenetre = Tk()

label = Label(fenetre, text="bonjour")
label.pack()

label = Label(fenetre, text="nom prenom")
label.pack()

value = StringVar() 
value.set("texte par défaut")
print(value)
entree = Entry(fenetre, textvariable=str("hello"), width=30)
entree.pack()

fenetre.mainloop()