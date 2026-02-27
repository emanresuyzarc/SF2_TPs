import tkinter as tk
import shunting_yard as sy

def cliquer():
    expr_postfix = sy.infix_to_postfix(sy.tokenize(str(etiquette_saisie)))
    resultat = sy.evaluate_postfix(str(etiquette_saisie))

    etiquette_postfix.config(text=f"{expr_postfix}")
    etiquette_resultat.config(text=f"{resultat}")


fenetre = tk.Tk()
fenetre.title("Algorithme Shunting Yard")

bouton_conversion = tk.Button(fenetre, text="Convertir en notation postfixée", command=cliquer)
etiquette_saisie = tk.Entry(fenetre, text="")
etiquette_postfix = tk.Label(fenetre, text=" - ")
etiquette_resultat = tk.Label(fenetre, text=" - ")
etiquette_erreur = tk.Label(fenetre, text=" - ")

etiquette_saisie.pack(pady=10)
bouton_conversion.pack(pady=10)
etiquette_postfix.pack(pady=10)
etiquette_resultat.pack(pady=10) 
etiquette_erreur.pack(pady=10)

expression = "3+4*2/(1-5)"
fenetre.mainloop()
