from tkinter import *
from tkinter.messagebox import *


fenetre = Tk()

label = Label(fenetre, text="bonjour")
label.pack()

value1 = StringVar()
value1.set("nom, prenom")
entree1 = Entry(fenetre, textvariable=value1, width=30)
entree1.pack()

label = Label(fenetre, text="age")
label.pack()
s = Spinbox(fenetre, from_=0, to=100)
s.pack()

value3 = StringVar()
value3.set("adress mail")
entree3 = Entry(fenetre, textvariable=value3, width=30)
entree3.pack()

value2 = StringVar()
value2.set("entreprise")
entree2 = Entry(fenetre, textvariable=value2, width=50)
entree2.pack()

valueok="societe generale"

def check_value():
    if value2.get()==valueok:
       global suite
       bouton = Checkbutton(fenetre, text="avez vous des bases en informatiques ?")
       bouton.pack()
       bouton = Checkbutton(fenetre, text="le domaine finacier vous interreste il ?")
       bouton.pack()
       bouton = Checkbutton(fenetre, text="est-ce votre premier stage ?")
       bouton.pack()
       bouton = Checkbutton(fenetre, text="avez vous de la famille, des amis travaillant actuellement ou non ici ? ")
       bouton.pack()
       bouton = Checkbutton(fenetre, text="faites vous ce stage dans uncadre scolaire ?")
       bouton.pack()
       bouton = Button(fenetre, text="envoyer",command=lambda: callback())
    else:
       label = Label(fenetre, text="nous ne gerons pas cette entreprise veuillez reesayer")
       label.pack()
bouton = Button(fenetre, text="Vérifier", command=lambda: check_value())
bouton.pack()


def callback():
    if askyesno('Titre 1', 'Êtes-vous sûr de vouloir faire ça?'):
        showwarning('Titre 2', 'formulaire envoyé')
    else:
        showinfo('Titre 3', 'annualion')
        showerror("Titre 4", "Aurevoir")

Button(text='envoyer', command=callback).pack()

def alert():
    showinfo("alerte", "error not difined")

menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Créer", command=alert)
menu1.add_command(label="Editer", command=alert)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.quit)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Couper", command=alert)
menu2.add_command(label="Copier", command=alert)
menu2.add_command(label="Coller", command=alert)
menubar.add_cascade(label="Editer", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=alert)
menubar.add_cascade(label="Aide", menu=menu3)

fenetre.config(menu=menubar)  


fenetre.mainloop()


