def calculette():
    try:
        num1 = float(input("Entrez le premier nombre : "))
        op = input("Entrez l'opérateur (+, -, *, /) : ")
        num2 = float(input("Entrez le deuxième nombre : "))

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

        print("Résultat : ", result)
    except ZeroDivisionError:
        print("Erreur : division par zéro")
    except ValueError:
        print("Erreur : opérateur invalide")

calculette()
  