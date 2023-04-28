# Créé par bretillotp, le 07/04/2023 en Python 3.7
import csv
import tkinter as tk
from tkinter import messagebox as alert
import tkinter.messagebox as messagebox
import os
import pandas
from tkinter import *


# Créer la fenêtre principale
root = tk.Tk()
root.title("Inventaire")


def add():
    add = tk.Tk()
    add.title("Ajouter")

    # Créer le label pour le nom de l'article
    label_name = tk.Label(add, text="Nom de l'article:")
    label_name.grid(row=0, column=0)

    # Créer le champ de saisie pour le nom de l'article
    entry_name = tk.Entry(add)
    entry_name.grid(row=0, column=1)

    # Créer le label pour la quantité
    label_quantity = tk.Label(add, text="Quantité:")
    label_quantity.grid(row=1, column=0)

    # Créer le champ de saisie pour la quantité
    entry_quantity = tk.Entry(add)
    entry_quantity.grid(row=1, column=1)

    # Créer le bouton "Ajouter"
    button_add = tk.Button(add, text="Ajouter", command=lambda: add_item(entry_name, entry_quantity))
    button_add.grid(row=3, column=0, columnspan=2)




# Créer la fonction qui sera appelée lors du clic sur le bouton "Ajouter"
def add_item(entry_name, entry_quantity):
    # Récupérer les valeurs saisies par l'utilisateur
    name = entry_name.get()
    quantity = entry_quantity.get()
    if quantity != "":
        # faire quelque chose si name n'est pas vide
        if os.path.isfile("inventory.csv"):
            # Le fichier inventory.csv existe
            aler = False
            with open("inventory.csv", "r") as f:
                read = csv.reader(f)

                for row in read:

                    if row[0] == name:
                        aler = True
                        alert.showerror("Erreur", "L'article {} est déja présent dans l'inventaire. Si vous souhaitez ajouter des produits {} à l'inventaire vous pouvez vous rendre dans la fenetre Entrer produits".format(name, name))
                        break

            if aler == False:
                # Ajouter les valeurs dans le fichier d'inventaire
                with open("inventory.csv", "a", newline='') as f:
                    writ = csv.writer(f)
                    writ.writerow([name,quantity])

        else:
            # Le fichier inventory.csv n'existe pas il va être créé grâce à la fonction "apend
            with open("inventory.csv", "a", newline='') as f:
                writ = csv.writer(f)
                writ.writerow([name,quantity])

    else:
        alert.showerror("Erreur", "Vous ne pouvez rentrez un produit dans l'inventaire si ce dernier ne contient aucune valeur quantité. Si le produit {} a 0 en stock mettre 0 dans le champ de sisie destiné à la quantité".format(name))

    # Effacer les champs de saisie
    entry_name.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)


# Créer la fonction qui sera appelée lors du clic sur le bouton "Rechercher" situé dans la menubar
def search():
    search = tk.Toplevel()
    search.title("Rechercher")

    # Créer le label pour le nom de l'article
    label_name = tk.Label(search, text="Nom de l'article:")
    label_name.grid(row=0, column=0)

    # Créer le champ de saisie pour le nom de l'article
    entry_name = tk.Entry(search)
    entry_name.grid(row=0, column=1)

    # Créer le bouton "Rechercher"
    button_search = tk.Button(search, text="Rechercher", command=lambda: search_item(entry_name))
    button_search.grid(row=3, column=0, columnspan=2)

# Créer la fonction qui sera appelée lors du clic sur le bouton "Rechercher"
def search_item(entry_name):
    name = entry_name.get()
    # Créer la fenêtre qui donne le message et propose diférentes actions
    top = tk.Toplevel()
    top.title("Rechercher")
    # Rechercher la quantité correspondant à l'article dans le fichier d'inventaire
    with open("inventory.csv", "r") as f:
        read = csv.reader(f)

        for row in read:

            if row[0] == name:
                # Le message s'écrit dans la nouvelle fenetre
                label = tk.Label(top, text="La quantité de l'article {} est : {}".format(name, row[1]))
                label.grid()
                break
        else:
            alert.showerror("Erreur", "L'article {} n'a pas été trouvé dans l'inventaire.".format(name))

    # Effacer le champ de saisie du nom de l'article
    entry_name.delete(0, tk.END)

# Créer la fonction qui sera appelée lors du clic sur le bouton "Entrer produits" de la menubar
def entry():
    entry = tk.Toplevel()
    entry.title("Entrer produits")

    # Créer le label pour le nom de l'article
    label_name = tk.Label(entry, text="Nom de l'article:")
    label_name.grid(row=0, column=0)

    # Créer le champ de saisie pour le nom de l'article
    entry_name = tk.Entry(entry)
    entry_name.grid(row=0, column=1)

    # Créer le label pour la quantité de produits entrée
    label_quantityentry = tk.Label(entry, text="Quantité de produits entrée:")
    label_quantityentry.grid(row=1, column=0)

    # Créer le champ de saisie pour la quantité de produits entrée
    entry_quantityentry = tk.Entry(entry)
    entry_quantityentry.grid(row=1, column=1)

    # Récupérer le nom de l'article saisi par l'utilisateur
    name = entry_name.get()

    # Créer le bouton "Valider"
    button_validentry = tk.Button(entry, text="Valider", command=lambda: valid_entry(entry_quantityentry, entry_name))
    button_validentry.grid(row=2, column=1, columnspan=2)


# Créer la fonction qui sera appelée lors du clic sur le bouton "Entrer produits" de la menubar
def export():
    export = tk.Toplevel()
    export.title("Soustraire produits")

    # Créer le label pour le nom de l'article
    label_name = tk.Label(export, text="Nom de l'article:")
    label_name.grid(row=0, column=0)

    # Créer le champ de saisie pour le nom de l'article
    entry_name = tk.Entry(export)
    entry_name.grid(row=0, column=1)

    # Créer le label pour la quantité de produits entrée
    label_quantityexport = tk.Label(export, text="Quantité de produits soustraite:")
    label_quantityexport.grid(row=1, column=0)

    # Créer le champ de saisie pour la quantité de produits entrée
    entry_quantityexport = tk.Entry(export)
    entry_quantityexport.grid(row=1, column=1)

    # Récupérer le nom de l'article saisi par l'utilisateur
    name = entry_name.get()

    # Créer le bouton "Valider"
    button_validexport = tk.Button(export, text="Valider", command=lambda: valid_export(entry_quantityexport, entry_name))
    button_validexport.grid(row=2, column=1, columnspan=2)


# Créer la fonction qui sera appelée lors du clic sur le bouton "Valider" pour la page "Entrer produits"
def valid_entry(entry_quantityentry, entry_name):

    # Récupérer les valeurs saisies par l'utilisateur
    name = entry_name.get()
    entry_quantity = entry_quantityentry.get()

    # Mettre à jour la quantité de produits dans le fichier CSV
    aler = False
    with open("inventory.csv", "r") as f:
        read = csv.reader(f)
        for row in read:
            if row[0] == name:
                aler = True
                new = int(row[1]) + int(entry_quantity)
                with open("inventory.csv", "r") as f:
                    read = csv.reader(f)
                    rows = [row if row[0] != name else [row[0], new] for row in read]

                with open("inventory.csv", "w", newline='') as f:
                    writ = csv.writer(f)
                    writ.writerows(rows)

                #Alerte informant l'utilisateur que l'action a été éfectuée
                messagebox.showwarning("Attention", "Vous avez modifié la quantité du produit." "Le stock contient {} {}." .format(new, name, entry) )

    if aler == False:
        alert.showerror("Erreur", "L'article {} n'a pas été trouvé dans l'inventaire.".format(name))


# Créer la fonction qui sera appelée lors du clic sur le bouton "Valider" pour la page "Soustraire produits"
def valid_export(entry_quantityexport, entry_name):
    # Récupérer les valeurs saisies par l'utilisateur
    name = entry_name.get()
    entry_quantity = entry_quantityexport.get()

    # Mettre à jour la quantité de produits dans le fichier CSV
    aler = False
    with open("inventory.csv", "r") as f:
        read = csv.reader(f)
        for row in read:
            if row[0] == name:
                aler = True
                new = int(row[1]) - int(entry_quantity)
                with open("inventory.csv", "r") as f:
                    read = csv.reader(f)
                    rows = [row if row[0] != name else [row[0], new] for row in read]

                with open("inventory.csv", "w", newline='') as f:
                    writ = csv.writer(f)
                    writ.writerows(rows)

                #Alerte informant l'utilisateur que l'action a été éfectuée
                messagebox.showwarning("Attention", "Vous avez modifié la quantité du produit." "Le stock contient {} {}." .format(new, name, entry) )

    if aler == False:
        alert.showerror("Erreur", "L'article {} n'a pas été trouvé dans l'inventaire.".format(name))


def h():
    root=Tk()
    label=Label(root)
    def ta_fonction(*args):
        label['text']= pandas.read_csv('inventory.csv')
    ta_fonction()
    label.pack(side=TOP)


# Créer le bouton "Ajouter"
button_add = tk.Button(root, text="Ajouter", command=add)
button_add.grid(row=2, column=0, columnspan=2)

# Créer le bouton "Rechercher"
button_search = tk.Button(root, text="Rechercher", command=search)
button_search.grid(row=3, column=0, columnspan=2)

# Créer le bouton "Entrer produits"
button_search = tk.Button(root, text="Entrer produits", command=entry)
button_search.grid(row=4, column=0, columnspan=2)

# Créer le bouton "Sortir produits"
button_search = tk.Button(root, text="Sortir produits", command=export)
button_search.grid(row=5, column=0, columnspan=2)

# Créer le bouton "Inventaire"
button_class = tk.Button(root, text="Inventaire", command=h)
button_class.grid(row=6, column=0, columnspan=2)



# Afficher la fenêtre
root.mainloop()




