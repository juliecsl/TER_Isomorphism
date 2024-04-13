from pynauty import *
from Utils import ReadGraph
import os

# Script uniquement utilisible sous Unix et MacOS.
# Du fait de l'utilisation de la librairie pynauty.

def nautyGraph(filename):
    """
    Fonction qui prend en entrée un fichier de la forme s1[s2 s4] s2[s1] s3 [s4 s1] ...
    Et le tranforme en fichier lisible par le programme nauty.
    """
    # important par convention les sommets sont numérotés à partir de 0
    return [[i-1 for i in ReadGraph(filename)[j] ]for j in range(len(ReadGraph(filename)))]

# g2 = [[i-1 for i in ReadGraph("FichierTests/ex5_1.txt")[j] ]for j in range(len(ReadGraph("FichierTests/ex5_2.txt")))]

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