
liste_operateurs = {"+", "-", "*", "/"}

def tokenize(expression: str) -> list[str]:
    tokens = []
    for element in expression:
        tokens.append(str(element))

    return tokens

def infix_to_postfix(tokens: list[str]) -> list[str]:
    priorite_operateurs = {"+": 1, "-": 1, "*": 2, "/": 2,}
    liste_output = []
    pile_operateurs = []

    for token in tokens:
        if token.isnumeric():
            liste_output.append(token)
        
        elif token in priorite_operateurs:
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
            
            """
            Erreur potentielle si parenthèses mal équilibrées
            if not operator_stack:
                raise ValueError("Parenthèses mal équilibrées")
            """
            pile_operateurs.pop()

        """
        Erreur potentielle si token ni chiffre ni opérateur
        else:
            raise ValueError("Parenthèses mal équilibrées")
        """
    while pile_operateurs:
        sommet_pile = pile_operateurs.pop()

        """
        Erreur potentielle si parenthèses mal équilibrées
        if sommet_pile in ("(", ")"):
            raise ValueError("Parenthèses mal équilibrées")
        """

        liste_output.append(sommet_pile)
    
    return liste_output

def evaluate_postfix(tokens: list[str]) -> float:
    liste_calcul = []
    resultat = 0

    for token in tokens:
        if token not in liste_operateurs:
            liste_calcul.append(float(token))

        elif token in liste_operateurs:
            """
            if len(stack) < 2:
                    raise ValueError("Insufficient operands for operation.")
            """
            print(liste_calcul)

            b = int(liste_calcul.pop())
            a = int(liste_calcul.pop())

            print(a)
            print(b)

            if token == "+":
                resultat == (a + b)
            elif token == "-":
                resultat == (a - b)
            elif token == "*":
                resultat == (a * b)
            elif token == "/":
                if b == 0:
                    raise ZeroDivisionError("Division by zero.")
                resultat == (a / b)
            
            liste_calcul.append(resultat)

    return liste_calcul

    
 

expr = "3+4*2/(1-5)"
expr2 = (infix_to_postfix(tokenize(expr)))
print(expr2)
print(evaluate_postfix(expr2))
