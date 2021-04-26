# -*- coding: utf-8 -*-
from random import *
jeu = [11, 11, 11, 11]
#Création de la liste jeu
def ajout_carte(main):
    a = choice(jeu) #On sélectionne aléatoirement une carte dans la liste 'jeu'
    main.append(a) #On ajoute cette carte a la liste 'main'
    jeu.remove(a) #On retire cette carte de la liste 'jeu' pour qu'elle ne soit pas retiré
    return main #On retourne la liste 'main'

def tirage():
    cartes = [] #On crée la liste vide 'cartes'
    for i in range(2):#On répète deux fois le tirage
        cartes.append(ajout_carte([]))#On affecte le résultat de ce tirage dans la lise 'cartes'
        print(cartes)
    if cartes[0] == 11 and cartes[1] == 11:#On vérifie si les deux cartes de la liste sont des 11
        cartes[0] = 1#si c'est le cas on remplace le premier 11 par 1
    return cartes #on retourne la liste 'cartes'

def total(main):
    somme = sum(main) #On fait la somme de la liste 'main'
    if somme > 21 and main.count(11)!=0: #On teste si la somme est supérieur à 21 et que la liste contient un 11
        main[main.index(11)] = 1 #Si c'est le cas on remplace le 11 par 1
        somme = sum(main) #On refait la somme de la liste modifié
    return somme # On retourne la somme

def jouer():
    print("Bonjour et bienvenue au jeu de Black Jack!")
    k = input("Souhaitez vous débuter une partie? OUI ou NON:")
    while k != "OUI":
        k = input("Souhaitez vous débuter une partie? OUI ou NON:")
    if k == "OUI":
        x = tirage()# La variable 'x' contiendra les deux cartes du joueur
        y = tirage()#La variable 'y' contiendra les deux cartes de l'ordinateur
        j = []#On crée la liste 'j' qui contiendra les cartes du joueur
        o = []#On crée la liste 'o' qui contiendra les cartes de l'ordinateur
        t = 0  #On crée la variable 't' qui contiendra le total des cartes du joueur
        d = 0#On crée la variable 'd' qui contiendra le total des cartes de l'ordinateur
        for k in y:
            o.append(k[0])#On transforme la liste de liste 'y' en liste simple 'o' qui contient les cartes de l'ordinateur
        for k in x:
            j.append(k[0])#On transforme la liste de liste 'x' en liste simple 'j' qui contient les cartes du joueur
        d = total(o) #On fait le total des cartes de l'ordinateur
        t = total(j)#On fait le total des cartes du joueur
        print("Vos cartes sont", j, "Le total est de:",t)#On affiche les cartes du joueur et leurs total
        print("La première cartes de l'ordinateur est", o[0])#On affiche la première carte de l'ordinateur
        s = input("Souhaitez vous une nouvelle carte? Tapez N pour une nouvelle carte; P pour ne pas avoir de nouvelle carte:")
        #On demande au joueur s'il souhaite une nouvelle carte
        while s == "N":
            x.append(ajout_carte([]))#On ajoute une nouvelle carte à la liste de liste 'x'
            a = x.pop()#On isole la liste contenant la nouvelle carte
            for i in a:
                v = i #La variable 'v' contient la nouvelle carte sous forme d'int
            j.append(v)#On ajoute la nouvelle carte sous forme d'int a la liste simple 'j'
            print("Vos cartes sont", j)#On affiche la nouvelle main du joueur
            t = total(j)#On calcule le nouveau total
            if t > 21:#Si le total est supérieur à 21
                print("Vous avez perdu la partie, votre score total est de: ", t)
                #On affiche que le joueur a perdu car il a dépassé 21
                s=="P"#On arrête la boucle while
            else:
                print("Votre score total est de:", t)#On affiche le total des cartes du joueur
                s = input("Voulez vous une carte supplémentaire ?")#On lui demande s'il en veut une encore
        while d < 17: #Si le total des cartes de l'ordinateur est inférieur à 17
            y.append(ajout_carte([])) #On ajoute une nouvelle carte à la liste de liste y
            a=y.pop()#On isole la liste contenant la nouvelle carte
            for i in a:
                v=i #La variable 'v' contient la nouvelle carte sous forme d'int
            o.append(v)#On ajoute la nouvelle carte sous forme d'int à la liste simple 'o'
            d=total(o)#On calcule le nouveau total
        if d>21:#Si le total des cartes de l'ordinateur est supérieur à 21
            print("L'ordinateur a dépassé 21 vous avez gagné")#On affiche que l'ordinateur a perdu car il a dépassé 21
        elif d<t:#si le total des cartes de l'ordinateur est inférieur au total des cartes du joueur
            print("Vous avez gagné la partie, votre score est de:", t ,"Le score de l'ordinateur est de:",d,".")
            #On affiche que le le joueur a gagné
        elif t<d:#si le total des cartes de l'ordinateur est supérieur au total des cartes du joueur
            print("Vous avez perdu, votre score est de:",t ,"Le score de l'ordinateur est de:",d,".")
            #On affiche que l'ordinateur a gagné
        elif t==d:#si le total des cartes de l'ordinateur est égal au total des cartes du joueur
            print("Il y a égalité")#On affiche qu'il y a égalité
jouer()
    
