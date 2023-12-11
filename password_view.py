# import du module os
import os

# password_show affiche les mots de passes contenus dans le fichier de sauvegarde
def password_show():
    if os.path.exists("password.txt"):
        with open("password.txt", "r+") as file:
            print(file.readlines())
            file.close()
    else:
        print("Le fichier spécifié n'existe pas !")
