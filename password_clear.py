# import du module os
import os

# fonction password_clear qui éfface le contenu du fichier contenant les mots de passes
def password_clear():
    if os.path.exists("password.txt"):
        with open("password.txt", "w") as file:
            file.truncate()
    print("Le fichier a ete nettoyer avec succes!\n")



