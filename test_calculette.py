def nombre_chiffres(nombre, chiffre):
    try:
        # Nettoyer la chaîne : remplacer virgule par point, supprimer les espaces
        nombre = nombre.replace(',', '.').replace(' ', '')
        
        # Vérifier si c'est un nombre valide (entier ou flottant)
        float(nombre)  # Cette ligne lèvera ValueError si le nombre est invalide

        # Supprimer le point décimal pour compter tous les chiffres
        nombre_sans_point = nombre.replace('.', '')

        # Vérifier que tous les caractères restants sont des chiffres
        if not nombre_sans_point.isdigit():
            print("Erreur : le nombre saisi contient des lettres")
            return None

        occurence = nombre_sans_point.count(str(chiffre))
        return occurence
    except ValueError:
        print("Erreur : le nombre saisi n'est pas un nombre valide")
        return None


def test_occurence_chiffres():
    print("Test de la fonction occurence_chiffres")
    print("---------------------------")

    # Test 1 : nombre sans chiffre
    print("Test 1 : nombre sans chiffre")
    result = nombre_chiffres("123", "4")
    assert result == 0, f"Erreur : résultat attendu 0, obtenu {result}"

    # Test 2 : nombre avec un chiffre
    print("Test 2 : nombre avec un chiffre")
    result = nombre_chiffres("123", "3")
    assert result == 1, f"Erreur : résultat attendu 1, obtenu {result}"

    # Test 3 : nombre avec plusieurs chiffres
    print("Test 3 : nombre avec plusieurs chiffres")
    result = nombre_chiffres("123123", "3")
    assert result == 2, f"Erreur : résultat attendu 2, obtenu {result}"

    # Test 4 : nombre décimal
    print("Test 4 : nombre décimal")
    result = nombre_chiffres("12.34", "3")
    assert result == 1, f"Erreur : résultat attendu 1, obtenu {result}"

    # Test 5 : nombre avec une virgule
    print("Test 5 : nombre avec une virgule")
    result = nombre_chiffres("12,34", "3")
    assert result == 1, f"Erreur : résultat attendu 1, obtenu {result}"

    # Test 6 : nombre avec plusieurs occurrences du même chiffre
    print("Test 6 : nombre avec plusieurs occurrences du même chiffre")
    result = nombre_chiffres("111", "1")
    assert result == 3, f"Erreur : résultat attendu 3, obtenu {result}"

    # Test 7 : nombre avec des espaces
    print("Test 7 : nombre avec des espaces")
    result = nombre_chiffres("12 34", "3")
    assert result == 1, f"Erreur : résultat attendu 1, obtenu {result}"

    # Test 8 : nombre avec des lettres
    print("Test 8 : nombre avec des lettres")
    result = nombre_chiffres("12a34", "3")
    assert result is None, f"Erreur : résultat attendu None, obtenu {result}"

    print("Tous les tests ont été passés avec succès")

# Lancer les tests
test_occurence_chiffres()
