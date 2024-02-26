from ReadFile import *
from DefineLambda import *

filename = "FichierTests/graph2.txt"

graph = ReadGraph(filename) 

def FirstPartitioning(graph):
    """
    Fonction qui permet de faire le premier partionnement des aretes. 
    Des aretes ayant le meme lambda (meme nombre de degré entrant/sortant et longueur de face droite/gauche)
    seront mises dans le meme bloc.

    Entrée: Liste représentant les caractéristiques du graphe.
            De la forme: [[n2, n3, n4, n5], [n1, n5, n4, n3], [n1, n2, n4], ....]
    Sortie: Dictionnaire représentant les caractéristiques du bloc suivant des aretes ayant ces propriétés.
            De la forme: {(|face gauche|, |face droite|, degré tail, degré head): [(n1, n2), (n1, n3), (n2, n4)], ...} 
            (avec ni des numéros de noeuds)
    """

    list_edges = []
    # Liste tous les arcs du graphe
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            list_edges.append((i+1, graph[i][j]))

    dico_lambda = dict()

    # On partitionne tous les arcs selon leur lamba
    # Une case de ditionnaire = à un meme lambda
    for edge in list_edges:
        lambda_edge = Lambda(edge)

        if lambda_edge in dico_lambda.keys():
            dico_lambda[lambda_edge].append(edge)
        else:
            dico_lambda[lambda_edge] = [edge]

    return dico_lambda

# print(FirstPartitioning(graph))
