import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
from ReadFile import *


def Draw(graphe):
    """
    """
    g = nx.Graph()

    edges = [(j+1,i) for j in range(len(graphe)) for i in graphe[j]]
    print(edges)
    print(len(graphe))
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

filename = "FichierTests/graph2.txt"
graph = ReadGraph(filename)
Draw(graph)


filename = "FichierTests/graph1.txt"
graph = ReadGraph(filename)
Draw(graph)