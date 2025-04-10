def calculette(num1, op, num2):
    try:
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        else:
            raise ValueError

        return result
    except ZeroDivisionError:
        return "Erreur : division par zéro"
    except ValueError:
        return "Erreur : opérateur invalide"

def test_calculette():
    print("Test de la fonction calculette")
    print("---------------------------")

    # Test 1 : addition
    print("Test 1 : addition")
    result = calculette(2, "+", 3)
    assert result == 5, "Erreur : résultat attendu 5, obtenu {}".format(result)

    # Test 2 : soustraction
    print("Test 2 : soustraction")
    result = calculette(5, "-", 2)
    assert result == 3, "Erreur : résultat attendu 3, obtenu {}".format(result)

    # Test 3 : multiplication
    print("Test 3 : multiplication")
    result = calculette(4, "*", 5)
    assert result == 20, "Erreur : résultat attendu 20, obtenu {}".format(result)

    # Test 4 : division
    print("Test 4 : division")
    result = calculette(10, "/", 2)
    assert result == 5, "Erreur : résultat attendu 5, obtenu {}".format(result)

    # Test 5 : division par zéro
    print("Test 5 : division par zéro")
    result = calculette(10, "/", 0)
    assert result == "Erreur : division par zéro", "Erreur : résultat attendu Erreur : division par zéro, obtenu {}".format(result)

    print("Tous les tests ont été passés avec succès")

test_calculette()