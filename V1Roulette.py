import random
import time
import json

argent = 1000
couleurs = ["Rouge", "Noire", "Rouge", "Noire", "Rouge", "Noire", "Blanche"]

#affiche l'argent de l'utilisateur
def v_argent():
    print("\n-----------------------------------------")
    print(f"        Il vous reste {argent} €")
    print("-----------------------------------------")

#affiche l'argent de l'utilisateur à la fin de la partie
def argent_f():
    print("--------------------------------------------------------")
    print(f"Vous avez donc {argent} €")
    print("--------------------------------------------------------")
    time.sleep(1)

#calcul de l'argent de l'utilisateur après avoir misé
def argent_mise():
    argent = argent - mise
    print(f"\n        Il vous reste {argent} €")

#calcul des gains et des pertes d'argent
def c_gain():
    if couleur_pariée == 1:
        couleur_choisie = couleurs[0] and couleurs[2] and couleurs[4]
        if couleur == couleur_choisie:
            mise = mise * 2
            argent = argent + mise
        else:
            mise = mise / 2
            argent = argent + mise

    elif couleur_pariée == 2:
        couleur_choisie = couleurs[1] and couleurs[3] and couleurs[5]
        if couleur == couleur_choisie:
            mise = mise * 2
            argent = argent + mise
        else:
            mise = mise / 2
            argent = argent + mise

    else:
        couleur_choisie = couleurs[6]
        if couleur == couleur_choisie:
            mise = mise * 4
            argent = argent + mise
        else:
            mise = mise / 4
            argent = argent + mise







#boucle principale
while argent > 0:
    
    #choix aléatoire de la couleur et affiche l'argent
    couleur_aleatoire = random.choice(couleurs)
    couleur = couleur_aleatoire
    v_argent()

    #choix du montant de la mise
    while True:
        try:
            mise = int(input(f"Combien d'argent voulez-vous miser en sachant que vous avez {argent} € : "))
            if mise < 0 or mise > argent:
                print("\033[31mLa mise doit être un nombre positif ou vous ne possèdez pas cet argent.\033[0m")
                print(f"\033[31mVous possèdez {argent} €\033[0m")
            else:
                break
        except ValueError:
            print("\033[31mCe n'est pas un nombre entier ou vous ne possèdez pas cet argent ! Essayez encore.\033[0m")

    #calcul et affiche l'argent restant après avoir misé
    argent_mise()

    #choix de la couleur
    while True:
        try:
            couleur_pariée = int(input("\n Sur quelle couleur voulez vous parrier ? (1 pour rouge, 2 pour noire, 3 pour blanche) : "))
            if couleur_pariée in [1, 2, 3]:
                break
            else:
                print("\033[31mChoix invalide. Veuillez entrer 1, 2 ou 3.\033[0m")
        except ValueError:
            print("\033[31mCe n'est pas un nombre entier ! Essayez encore.\033[0m")


    #calcul des gains et des pertes d'argent
    c_gain()


    #rappel de la couleur pariée
    print("\n--------------------------------------------------------")
    print(f"Vous avez choisis la couleur {couleur_pariée}")

    time.sleep(1)

    #résultat de la couleur choisie aléatoirement
    print(f"\n     C'est tombé sur la couleur : {couleur} !")
    time.sleep(1)

    #affiche l'argent de l'utilisateur après la partie
    print("--------------------------------------------------------")
    print(f"Vous avez donc {argent} €")
    print("--------------------------------------------------------")
    time.sleep(1)

    #arrête la partie quand l'utilisateur n'a plus d'argent
    if argent <= 0:
        print("\n Vous n'avez plus d'argent. Fin de la partie.")
        break

    #demande si l'utilisateur veut rejouer
    rejouer = input("\n Voulez-vous rejouer ? (oui pour continuer, autre touche pour quitter) : ").lower()
    if rejouer != "oui":
        print("\n Merci d'avoir joué ! \n")
        break