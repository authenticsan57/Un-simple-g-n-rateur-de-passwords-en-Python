# import de tous les autres fichiers
from password_view import password_show
from password_clear import password_clear
from password_gen import password_generator

# Affichage des options du menu du générateur
quitt = "y"
while quitt != "n":
    print(" 1- Générer des mots de passe\n"
          " 2- Afficher les mots de passe sauvegarder\n"
          " 3- Néttoyer le fichier de stockage\n"
          " 0- Quitter\n")
    choice = input("Quelle action voulez-vous réaliser ? : ")
    if choice == "1":
        password_generator()
    elif choice == "2":
        password_show()
    elif choice == "3":
        password_clear()
    elif choice == "0":
        pass
    quitt = input("Continuer ? (y/n) : ")
