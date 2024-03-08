import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
from ReadFile import *

# Méthode de test d'isomorphisme entre deux graphes de manière "naive"
# L'algorithme est le suivant : 
# - calcul de signature pour le graphe 1
# - calcul de signature pour le graphe 2
# - comparaison des deux signatures : s'il y a égalité, on a des graphes isomorphes


class Graph(object):

    def __init__(self, graph) :
        self.graph = graph
    

    def Edges(self):
        """
        fonction qui retourne toutes les arêtes du graphe (on considère qu'il est non orienté)

        entrée : le graphe sous forme d'une liste
        sortie : liste des arêtes
        """
        res = []
        for vertex in range(len(self.graph)):
            for neighbor in self.graph[vertex]:
                res.append((vertex+1, neighbor))
        
        return res
    
    def Draw(self):
        """
        fonction qui permet d'afficher le graphe sous forme planaire dans une fenêtre

        entrée : le graphe
        sortie : -
        """

        g = nx.Graph()
        edges = self.Edges()
        g.add_edges_from(edges)
        
        # on veut quelque chose de planaire (on a une erreur si impossible)
        try:
            pos = nx.planar_layout(g)
        except ValueError as err:
            print(err.args)
            
        # dessiner le graph en affichant les labels des noeuds
        nx.draw(g, pos=pos, with_labels=True)
        # afficher
        plt.show()


    def ParcoursProfondeurUtils(self, edge, visited):
        """
        """
        
        #on liste toutes les arêtes du graphe
        edges = self.Edges()
        #on ajoute l'arête à la liste des arêtes visitées
        visited.append(edge)

        if edge in edges:
            # pour chaque voisin de la tête, edge[1], de notre arête faire :
            for neighbor in self.graph[edge[1]-1]:
                if (edge[1], neighbor) not in visited:
                    self.ParcoursProfondeurUtils((edge[1], neighbor), visited)


    def ParcoursProfondeurEdge(self, edge_debut):
        """
        Fonction qui permet de parcourir le graphe en profondeur sur les arêtes 

        entrée : le graphe
        sortie : une liste avec tous les sommets dans l'ordre dans lesquelles on les passe
        """
        visited = list()
        self.ParcoursProfondeurUtils(edge_debut, visited)

        res = [edge_debut[0]]
        for edge in visited :
            if res[-1] != edge[0]:
                res.append(edge[0])
            res.append(edge[1])
        
        return res

    def Signature(self):
        """
        """

        edges = self.Edges()
        for edge in edges :
            parcours = self.ParcoursProfondeurEdge(edge)
            print(parcours)
        


filename = "FichierTests/graph2bis.txt"
graph = ReadGraph(filename)
print(graph)

graph = Graph(graph)
#print(graph.Signature())
graph.Draw()