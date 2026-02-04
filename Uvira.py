import streamlit as st
import json


print(f" BIENVENUS A AGENCE OKAPI UVIRA")

# Charger les colis depuis le fichier JSON
try:
    with open("registre_colis.json", "r", encoding="utf-8") as f:
        colis_list = json.load(f)
except FileNotFoundError:
    colis_list = []

while True:
    print(f"\nMENU PRINCIPAL ")
    print(f"1.  Enregistrer un envoi (nouveau client)")
    print(f"2. Afficher la liste des colis")
    print(f"3.  Livrer un colis")
    print(f"4. Quitter")

    choix = input("Choisissez une option : ")

    match choix:
       
        case "1":
            print(f"Enregistrement d’un nouvel envoi")

            expediteur_nom = input("Nom expéditeur : ")
            expediteur_prenom = input("Prénom expéditeur : ")
            expediteur_carte = input("Carte expéditeur (10 chiffres) : ")
            while not (expediteur_carte.isdigit() and len(expediteur_carte) == 10):
                print(f" Erreur : la carte doit contenir exactement 10 chiffres.")
                expediteur_carte = input("Carte expéditeur (10 chiffres) : ")

            destinataire_nom = input("Nom destinataire : ")
            destinataire_prenom = input("Prénom destinataire : ")
            destinataire_carte = input("Carte destinataire (10 chiffres) : ")
            while not (destinataire_carte.isdigit() and len(destinataire_carte) == 10):
                print(f" Erreur : la carte doit contenir exactement 10 chiffres.")
                destinataire_carte = input("Carte destinataire (10 chiffres) : ")

            code = input("Code colis (10 chiffres) : ")
            while not (code.isdigit() and len(code) == 10):
                print(f"Erreur : le code doit contenir exactement 10 chiffres.")
                code = input("Code colis (10 chiffres) : ")

            carte_electeur = input("Carte électeur (chiffres uniquement) : ")
            while not carte_electeur.isdigit():
                print(f"Erreur : la carte doit contenir uniquement des chiffres.")
                carte_electeur = input("Carte électeur (chiffres uniquement) : ")

            try:
                poids = int(input("Poids (kg) : "))
            except ValueError:
                poids = 0
                print(f"Poids invalide, valeur par défaut = 0")

            try:
                valeur = int(input("Valeur déclarée : "))
            except ValueError:
                valeur = 0
                print(f"Valeur invalide, valeur par défaut = 0")

            try:
                tarif = int(input("Tarif : "))
            except ValueError:
                tarif = 0
                print(f"Tarif invalide, valeur par défaut = 0")

            depart = input("Ville départ : ")
            arrivee = input("Ville arrivée : ")

            colis = {
                "code": code,
                "carte_electeur": carte_electeur,
                "poids": poids,
                "valeur": valeur,
                "tarif": tarif,
                "depart": depart,
                "arrivee": arrivee,
                "expediteur": f"{expediteur_nom} {expediteur_prenom}",
                "destinataire": f"{destinataire_nom} {destinataire_prenom}"
            }
            colis_list.append(colis)

            with open("registre_colis.json", "w", encoding="utf-8") as f:
                json.dump(colis_list, f, ensure_ascii=False, indent=4)

            print(f" Colis {code} enregistré avec succès !")

        #colis
        case "2":
            print(f" Liste des colis enregistrés")
            if not colis_list:
                print(f"Aucun colis enregistré.")
            else:
                for i, colis in enumerate(colis_list, start=1):
                    print(f"\n--- Colis {i} ---")
                    print(f"Code : {colis['code']}")
                    print(f"Expéditeur : {colis['expediteur']}")
                    print(f"Destinataire : {colis['destinataire']}")
                    print(f"Carte électeur : {colis['carte_electeur']}")
                    print(f"Poids : {colis['poids']} kg")
                    print(f"Valeur déclarée : {colis['valeur']}")
                    print(f"Ville départ : {colis['depart']}")
                    print(f"Ville arrivée : {colis['arrivee']}")
                    print(f"Tarif : {colis['tarif']}")
                    print(f"-----------------------------")

        # === LIVRER UN COLIS ===
        case "3":
            print(f"Livraison d’un colis")
            code_livraison = input("Entrez le code du colis à livrer : ")
            collecteur_nom = input("Nom collecteur : ")
            collecteur_prenom = input("Prénom collecteur : ")
            collecteur_carte = input("Carte collecteur : ")

            colis_trouve = next((c for c in colis_list if c["code"] == code_livraison), None)
            if not colis_trouve:
                print(f"Colis {code_livraison} introuvable.")
            elif not collecteur_nom or not collecteur_prenom or not collecteur_carte:
                print(f" Informations collecteur incomplètes.")
            else:
                colis_list.remove(colis_trouve)
                with open("registre_colis.json", "w", encoding="utf-8") as f:
                    json.dump(colis_list, f, ensure_ascii=False, indent=4)
                print(f"Colis {code_livraison} livré et retiré de la liste.")

        # quitter (utoke)
        case "4":
            print(f"Fin du programme")
            print(f"Nombre total de colis enregistrés : {len(colis_list)}")
            break

        # par de faut
        case _:
            print(f" Choix invalide ({choix}). Réessayez.")