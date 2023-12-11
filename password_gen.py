# Importation des modules os et random
import os
import random

# password_generator génère des caractères aléatoires pour former les mots de passes
def password_generator():

    # Paramétrage des mots de passe

    char_num = int(input("Combien de mot de passe souhaitez vous générer ? : "))
    password_num = int(input("Combien de caractère souhaitez vous ? : "))

    # Boucle de génération des caractère aléatoire à partir de code ASCII

    for j in range(char_num):
        password = []
        password_gen = []
        for i in range(password_num):
            password.append(chr(random.randint(33, 126)))
            password_gen = "".join(password)  # La liste de caractères est fusionnée
        print(password_gen)  # Chaque de mot de passe est affiché
        # Création d'un ficher "password.txt" en mode écriture pour sauvegarder les mots de passe générés
        with open("password.txt", "a+") as file:

            file.write(password_gen + "\n")  # Le mot de passe généré est stocké dans "password.txt"
    file.close()  # Le fichier est finalement refermé après utilisation

