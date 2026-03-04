import tkinter as tk
import shunting_yard as sy


fenetre = tk.Tk()
fenetre.title("Algorithme Shunting Yard")

expr_var = tk.StringVar()

def cliquer():
        try:
            expression = expr_var.get()
            expr_postfix = sy.infix_to_postfix(sy.tokenize(expression))
            resultat = sy.evaluate_postfix(expr_postfix)

            etiquette_postfix.config(text=f"{expr_postfix}")
            etiquette_resultat.config(text=f"{resultat}")
            etiquette_erreur.config(text=" - ", fg="black")
        except Exception as e:
            etiquette_erreur.config(text=f"Erreur : {e}", fg="red")
            etiquette_postfix.config(text=" - ")
            etiquette_resultat.config(text=" - ")
              

bouton_conversion = tk.Button(fenetre, text="Convertir en notation postfixée", command=cliquer)
etiquette_saisie = tk.Entry(fenetre, textvariable=expr_var)
etiquette_postfix = tk.Label(fenetre, text=" - ")
etiquette_resultat = tk.Label(fenetre, text=" - ")
etiquette_erreur = tk.Label(fenetre, text=" - ")

etiquette_saisie.pack(pady=10)
bouton_conversion.pack(pady=10)
etiquette_postfix.pack(pady=10)
etiquette_resultat.pack(pady=10) 
etiquette_erreur.pack(pady=10)

fenetre.mainloop()
