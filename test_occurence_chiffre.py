def nombre_chiffres():
   try:
       nombre=("nombre : ")
       if not nombre.replace('.', '', 1).replace(',', '', 1).isdigit(): 
           print("Erreur : le nombre saisi contient des lettres")
           return
       chiffre=input("chiffre: ")
       occurence=str(nombre).count(str(chiffre))
       return(occurence)
   except ValueError:
       print("Erreur : le nombre saisi n'est pas un entier")

nombre_chiffres()
def test_occurence_chiffres():
    print("Test de la fonction occurence_chiffres")
    print("---------------------------")

    # Test 1 : nombre sans chiffre
    print("Test 1 : nombre sans chiffre")
    result = nombre_chiffres("123", "4")
    assert result == 0, "Erreur : résultat attendu 0, obtenu {}".format(result)

    # Test 2 : nombre avec un chiffre
    print("Test 2 : nombre avec un chiffre")
    result = nombre_chiffres("123", "3")
    assert result == 1, "Erreur : résultat attendu 1, obtenu {}".format(result)

    # Test 3 : nombre avec plusieurs chiffres
    print("Test 3 : nombre avec plusieurs chiffres")
    result = nombre_chiffres("123123", "3")
    assert result == 2, "Erreur : résultat attendu 2, obtenu {}".format(result)

    # Test 4 : nombre décimal
    print("Test 4 : nombre décimal")
    result = nombre_chiffres("12.34", "3")
    assert result == 0, "Erreur : résultat attendu 0, obtenu {}".format(result)

    # Test 5 : nombre avec une virgule
    print("Test 5 : nombre avec une virgule")
    result = nombre_chiffres("12,34", "3")
    assert result == 0, "Erreur : résultat attendu 0, obtenu {}".format(result)

    print("Tous les tests ont été passés avec succès")

test_occurence_chiffres()