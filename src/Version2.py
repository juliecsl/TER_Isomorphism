# Méthode de test d'isomorphisme entre deux graphes de manière "naive"
# L'algorithme est le suivant : 
# - calcul de signature pour le graphe 1
# - calcul de signature pour le graphe 2
# - comparaison des deux signatures : s'il y a égalité, on a des graphes isomorphes


class Graph(object):

    def __init__(self, graph) :
        self.graph = graph

    def ParcoursProfondeurUtils(self, edge, visited):
        visited.add(edge)
        if edge in self.graph:
            for neighbor in self.graph[v]:
                if (edge, neighbor) not in visited:
                    print(f"Traversing edge: ({edge} -> {neighbor})")
                    self.ParcoursProfondeurUtils(neighbor, visited)

    def ParcoursProfondeurEdge(self, start_vertex):
        visited = set()
        self.ParcoursProfondeurUtils(start_vertex, visited)
    





from ReadFile import *
from ReadFileFromPlantri import *

filename = "FichierTests/graph1.txt"
graph = ReadGraph(filename)

# Calcul de signature d'un graphe : on fait un parcours de graphe en profondeur pour passer par toutes les arêtes, 
# depuis toutes les arêtes du graphe. La signature finale est la plus petite.

def Signature(graphe):
    """
    """

    edges = [(j+1,i) for j in range(len(graphe)) for i in graphe[j]] #liste contenant toutes les arêtes (deux sens) du graphe
    print(edges)
    
    for edge in edges:
        
        # initialisation
        signature = [1, 2] # dans cette liste on mettra les sommets dans l'ordre dans lesquels on les voit en faisant un parcours profondeur
        dico_edges = {edge[0] : 1, edge[1] : 2}

        # parcours en profondeur
        parcours(graphe, edge, [])

        #print(signature)


def parcours(graphe, edge, visited):
    """
    fonction qui fait un parcours en profondeur dans un graphe à partir d'une arête.
    
    entrée : le graphe, l'arête de départ, une liste "visited" dans laquelle on place les arêtes que l'on a visité
    sortie : rien
    """
    visited.append(edge)
    #print(edge)

    for neighbor in graphe[edge[1]-1]:
        if (edge[1],neighbor) not in visited :
            parcours(graphe, (edge[1], neighbor), visited)


Signature(graph)