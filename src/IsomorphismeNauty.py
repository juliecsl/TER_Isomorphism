from pynauty import *
from Utils import ReadGraph
from complexite import Repertoire
import os
import time
import matplotlib.pyplot as plt
import statistics

# Script uniquement utilisible sous Unix et MacOS.
# Du fait de l'utilisation de la librairie pynauty.

def nautyGraph(filename: str) -> list:
    """
    Fonction qui prend en entrée un fichier de la forme s1[s2 s4] s2[s1] s3 [s4 s1] ...
    Et le tranforme en fichier lisible par le programme nauty.
    """
    # important par convention les sommets sont numérotés à partir de 0
    return [[i-1 for i in ReadGraph(filename)[j] ]for j in range(len(ReadGraph(filename)))]


def IsoNauty(filename1: str, filename2: str) -> bool:
    """
    Fonction qui regarde si deux graphes sont isomorphes en utilisant
    l'algorithme de nauty.

    Entrée: fichiers textes sous la forme s1[s2 s4] s2[s1] s3 [s4 s1] ...
    Sortie: Vrai si les graphes sont isomorphes Faux sinon
    """
    # lecture des fichiers
    g1 = nautyGraph(filename1)
    g2 = nautyGraph(filename2)

    # on initialise les objets graphes 
    # Initialisation de la taille des graphes
    g1_nauty = Graph(len(g1))
    g2_nauty = Graph(len(g2))

    # on mets sous forme de dictionnaire les listes d'adjacence
    dic_g1 = {i:g1[i] for i in range(len(g1))}
    dic_g2 = {i:g2[i] for i in range(len(g2))}

    # Initialisation aretes des graphes
    g1_nauty.set_adjacency_dict(dic_g1)
    g2_nauty.set_adjacency_dict(dic_g2)

    return isomorphic(g1_nauty, g2_nauty)


# print(IsoNauty("FichierTests/ex6_1.txt", "FichierTests/ex6_1ISO.txt"))
# résultat : false et true 
# print(isomorphic(g1_nauty, g2_nauty))
# print(isomorphic(g1_nauty, g1_nauty))


# J'ai pas mis cette fonction dans complexité pour éviter de 
# devoir 'y importer la librairie pynauty
def tempsIsomorphismeNauty() -> dict:
    """
    Fonction qui retourne dans un dictionnaire le temps moyen de calcul 
    de l'isomorphisme de nauty en fonction du nombre de sommets
    """
    fichiers = Repertoire("FichierTests")
    res = {}

    for filename1 in fichiers:
        if "ISO" not in filename1:
            measures = []
            graph = ReadGraph(filename1)
            taille = len(graph)
            # on calcule le temps que met l'algo nauty
            filename2 = filename1[:len(filename1)-4] + "ISO.txt"
            start = time.time()
            IsoNauty(filename1, filename2)
            end = time.time()

            measures = (end - start)
            if taille in res:
                res[taille].append(measures)
            else:
                res[taille] = [measures]
    
    #on calcule maintenant les moyennes
    for key in res:
       res[key] = statistics.mean(res[key])
    
    #ecart_type = statistics.stdev(measures)

    return {key:res[key] for key in sorted(res)}

def AffichageGraphiqueNauty():
    """
    Fonction qui permet d'afficher le temps de calcul del'algo nauty en fontion du nombre de sommets
    """
    
    data = tempsIsomorphismeNauty().items()
    # print(data)
    x, y1 = zip(*data)
    # refaire cette droite
    #y2 = [((i/x[5])**2)*y1[5] for i in x]
    plt.plot(x, y1)
    #plt.plot(x, y2)
    plt.xlabel("Nombre de sommets")
    plt.ylabel("Temps moyen de calcul pour l'isomorphisme (en secondes)")
    plt.title("Algorithme Nauty")

    # plt.show()
    plt.savefig('filename.png')


AffichageGraphiqueNauty()