from Version_naive import *

import matplotlib.pyplot as plt
import statistics
import time
import os 

    
def Repertoire(repert):
    """ Fonction qui met tous les fichiers d'un répertoire dans une liste """

    fichiers =  os.listdir(os.path.abspath(repert))
    # on mets les noms de fichiers sous une forme qui sera prise en compte par nos programmes
    for i in range(len(fichiers)):
        fichiers[i] = repert + "/" + fichiers[i]
    
    return fichiers

#### COMPLEXITE VERSION NAIVE ####

def TempsSignatureAlgoNaif():
    """
    Fonction qui retourne dans un dictionnaire le temps moyen de calcul de la signature en fonction du nombre de sommets
    """

    fichiers = Repertoire("FichierTests")
    
    # pour chaque fichier, on note le nombre de sommets avec le temps d'éxécution associé
    res = {}
    for fichier in fichiers:
        graph = ReadGraph(fichier)
        measures = []
        # on calcule le temps que met l'algo naif pour faire une signature 
        start = time.time()
        Signature(graph)
        end = time.time()

        measures = (end - start)
        if len(graph) in res:
            res[len(graph)].append(measures)
        else:
            res[len(graph)] = [measures]
    
    #on calcule maintenant les moyennes
    for key in res:
       res[key] = statistics.mean(res[key])
    
    #ecart_type = statistics.stdev(measures)

    return {key:res[key] for key in sorted(res)}


def AffichageAlgoNaif():
    """
    Fonction qui permet d'afficher le temps de calcul signature algo naif en fontion du nombre de sommets
    """
    
    data = TempsSignatureAlgoNaif().items()
    print(data)
    x, y1 = zip(*data)
    y2 = [((i/x[0])**2)*y1[0] for i in x]
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.xlabel("Nombre de sommets")
    plt.ylabel("Temps moyen de calcul pour la signature")
    plt.title("Algorithme naif")
    plt.show()


def TempsSignatureAlgoNaifARETES():
    """
    Fonction qui retourne dans un dictionnaire le temps moyen de calcul de la signature en fonction du nombre de sommets
    """

    fichiers = Repertoire("FichierTests")
    
    # pour chaque fichier, on note le nombre de sommets avec le temps d'éxécution associé
    res = {}
    for fichier in fichiers:
        graph = ReadGraph(fichier)
        measures = []
        # on calcule le temps que met l'algo naif pour faire une signature 
        start = time.time()
        Signature(graph)
        end = time.time()

        measures = (end - start)
        if len(Edges(graph)) in res:
            res[len(Edges(graph))].append(measures)
        else:
            res[len(Edges(graph))] = [measures]
    
    #on calcule maintenant les moyennes
    for key in res:
       res[key] = statistics.mean(res[key])
    
    #ecart_type = statistics.stdev(measures)

    return {key:res[key] for key in sorted(res)}


def AffichageAlgoNaifARETES():
    """
    Fonction qui permet d'afficher le temps de calcul signature algo naif en fontion du nombre d'aretes'
    """
    
    data = TempsSignatureAlgoNaifARETES().items()
    print(data)
    x, y1 = zip(*data)
    plt.plot(x, y1)
    plt.xlabel("Nombre d'aretes")
    plt.ylabel("Temps moyen de calcul pour la signature")
    plt.title("Algorithme naif")
    plt.show()


AffichageAlgoNaifARETES()