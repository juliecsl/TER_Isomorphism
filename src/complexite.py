from SignatureNaive import SignatureParcours
from SignatureVlogV import SignaturePartitionnement
from Utils import *


import matplotlib.pyplot as plt
import pandas as pd
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


#### COMPLEXITE ####

def TempsSignature(version):
    """
    Fonction qui retourne dans un dictionnaire le temps moyen de calcul de la signature en fonction du nombre de sommets
    """

    fichiers = Repertoire("FichierTests")
    
    # pour chaque fichier, on note le nombre de sommets avec le temps d'éxécution associé
    res = {}
    for fichier in fichiers:
        graph = ReadGraph(fichier)
        measures = []
        taille = len(graph)
        if taille <= 220 :

            if version == "vlogv" :
                # on calcule le temps que met l'algo vlogv pour faire une signature
                start = time.time()
                SignaturePartitionnement(graph)
                end = time.time()

            elif version == "naive":
                # on calcule le temps que met l'algo naif pour faire une signature
                start = time.time()
                SignatureParcours(graph)
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


def AffichageGraphique(version):
    """
    Fonction qui permet d'afficher le temps de calcul signature algo naif en fontion du nombre de sommets
    """
    
    data = TempsSignature(version).items()
    # print(data)
    x, y1 = zip(*data)
    # refaire cette droite
    #y2 = [((i/x[5])**2)*y1[5] for i in x]
    plt.plot(x, y1)
    #plt.plot(x, y2)
    plt.xlabel("Nombre de sommets")
    plt.ylabel("Temps moyen de calcul pour la signature (en secondes)")
    if version == "vlogv":
        plt.title("Algorithme VlogV")
    elif version == "naive":
        plt.title("Algorithme naif")

    plt.show()


def saveDataComplexite(version):

    # génère la moyenne de temps des graphes
    data = TempsSignature(version).items()

    # Créer un DataFrame pandas à partir des données
    df = pd.DataFrame(data, columns=['Nb Noeuds', 'Moyenne Temps'])

    # Enregistre le Dataframe dans un fichier Excel
    df.to_excel('donnees.xlsx', index=False)
    print("Fichier de données sauvegardé.")

# saveDataComplexite("vlogv")
# AffichageGraphique("vlogv")
# AffichageGraphique("naive")
