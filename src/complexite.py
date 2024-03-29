from Version_naive import *
import matplotlib.pyplot as plt
import pandas as pd
import statistics
import time
import os 

#### COMPLEXITE VERSION NAIVE ####
    
def Repertoire(repert):
    """ Fonction qui met tous les fichiers d'un répertoire dans une liste """

    fichiers =  os.listdir(os.path.abspath(repert))
    # on mets les noms de fichiers sous une forme qui sera prise en compte par nos programmes
    for i in range(len(fichiers)):
        fichiers[i] = "FichierTests/" + fichiers[i]
    
    return fichiers


def TempsSignature():

    #fichiers = Repertoire("FichierTests")
    fichiers = ["FichierTests\graph30_1.txt"]
    
    # pour chaque fichier, on note le nombre de sommets avec le temps d'éxécution associé
    res = []
    for fichier in fichiers:
        sous_res = []
        graph = Graph(ReadGraph(fichier))
        
        sous_res.append(graph.len())
        measures = []
        for _ in range(100):
            start = time.time()
    
            graph.Signature()
    
            end = time.time()
            measures.append(end - start)

        moyenne = statistics.mean(measures)
        sous_res.append(moyenne)
        ecart_type = statistics.stdev(measures)
        sous_res.append(ecart_type)

        res.append(sous_res)

    return res

print(TempsSignature())