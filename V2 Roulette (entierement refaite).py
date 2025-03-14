import random
import time


#fonction pour voir l'argent
def v_argent():
    print("\n------------------------------")
    print(f"\nVous avez {argent} €")
    print("\n------------------------------")


#mis en place des variables
argent = 1000
couleurs = ["Rouge", "Noir", "Rouge", "Noir", "Rouge", "Noir", "Vert"]



#boucle principale
while argent > 0:

    #afficher l'argent de l'utilisateur grâce à sa fonction
    v_argent()
    
    #choix du montant de la mise
    qmise = int(input("\nCombien voulez-vous miser ? : "))
    argent = argent - qmise

    #choix de la couleur pariée
    qcouleur = int(input("\nSur quelle couleur voulez-vous parrier ? (1 pour rouge, 2 pour noir, 3 pour vert) : "))
    if qcouleur == 1:
        qcouleur = "Rouge"
    elif qcouleur ==2:
        qcouleur = "Noir"
    else:
        qcouleur = "Vert"

    #tirage au sort daans la list couleurs
    couleur_R = random.choice(couleurs)
    couleurF = couleur_R

    time.sleep(1)

    #annonce le résultat de la couleur
    if couleurF == "Rouge":
        print("C'est tombé sur la couleur Rouge !")

    elif couleurF == "Noir":
        print("C'est tombé sur la couleur Noire !")

    elif couleurF == "Vert":
        print("C'est tombé sur la couleur Verte !")


    #calcul des gains et des pertes
    #calcul pour la couleur rouge
    if qcouleur == "Rouge":
        if qcouleur == couleurF:
            qmise = qmise * 2
            argent = argent + qmise
            print(f"\nVous avez gagné {qmise} € !")
        else:
            qmise = qmise / 2
            argent = argent + qmise
            print(f"\nVous avez perdu {qmise} €")

    #calcul pour la couleur noire
    elif qcouleur == "Noir":
        if qcouleur == couleurF:
            qmise = qmise * 2
            argent = argent + qmise
            print(f"\nVous avez gagné {qmise} € !")
        else:
            qmise = qmise / 2
            argent = argent + qmise
            print(f"\nVous avez perdu {qmise} €")

    #calcul pour la couleur verte
    elif qcouleur == "Vert":
        if qcouleur == couleurF:
            qmise = qmise * 3
            argent = argent + qmise
            print(f"\nVous avez gagné {qmise} € !")
        else:
            qmise = qmise / 3
            argent = argent + qmise
            print(f"\nVous avez perdu {qmise} €")



    time.sleep(1)


#demande à l'utilisateur si il veut quitter la partie ou rejouer
    qrejouer = input("\nVoulez-vous rejouer ? : ")
    if qrejouer == "oui":
        print("\nC'est repartit !")

    else:
        print("\nMerci d'avoir joué !\n")
        break
