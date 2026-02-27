
liste_operateurs = {"+", "-", "*", "/"}

def tokenize(expression: str) -> list[str]:
    print(expression)
    tokens = []
    nombre = ""

    for element in expression:
        print(element)

        if element == " ":
            continue

        elif element == "-" and tokens[-1] in liste_operateurs:
            nombre += element

        elif element.isdigit() or element == "." or element == ",":
            nombre += element
        
        elif element in liste_operateurs:
            if nombre:
                tokens.append(nombre)
                nombre = ""
            tokens.append(element)

        elif element == "(" or element == ")":
            if nombre:
                tokens.append(nombre)
                nombre = ""
            tokens.append(element)
        
        else:
            raise ValueError(f"Élement invalide : {element}")
        
    tokens.append(nombre)

    return tokens


def infix_to_postfix(tokens: list[str]) -> list[str]:
    priorite_operateurs = {"+": 1, "-": 1, "*": 2, "/": 2,}
    liste_output = []
    pile_operateurs = []

    for token in tokens:
        try:
            float(token)
            liste_output.append(token)
        except ValueError:
            pass
        
        if token in priorite_operateurs:
            while pile_operateurs:
                sommet_pile = pile_operateurs[-1]

                if sommet_pile in priorite_operateurs and (priorite_operateurs[sommet_pile] >= priorite_operateurs[token]):
                    liste_output.append(pile_operateurs.pop())

                else:
                    break
            pile_operateurs.append(token)

        elif token == "(":
            pile_operateurs.append(token)
        
        elif token == ")":
            while pile_operateurs and pile_operateurs[-1] != "(":
                liste_output.append(pile_operateurs.pop())
                
            if not pile_operateurs:
                raise ValueError("Parenthèses mal équilibrées")
            pile_operateurs.pop()

        else:
            raise ValueError("Opérateur inconnu")

    while pile_operateurs:
        sommet_pile = pile_operateurs.pop()

        if sommet_pile in ("(", ")"):
            raise ValueError("Parenthèses mal équilibrées")
 
        liste_output.append(sommet_pile)
    
    return liste_output

def evaluate_postfix(tokens):
    pile_calcul = []

    for token in tokens:
        if token not in liste_operateurs:
            pile_calcul.append(float(token))
            print(pile_calcul)
        
        else:

            b = pile_calcul.pop()
            a = pile_calcul.pop()

            if token == "+":
                resultat = (a + b)
            elif token == "-":
                resultat = (a - b)
            elif token == "*":
                resultat = (a * b)
            elif token == "/":
                if b == 0:
                    raise ZeroDivisionError("Division par zéro")
                resultat = (a / b)
            
            pile_calcul.append(resultat)

    return pile_calcul[0]

print((tokenize("3+4*2/(1-5)+3.46")))