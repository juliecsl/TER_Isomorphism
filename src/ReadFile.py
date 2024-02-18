import re

def ReadGraph(filename):
    """ 
    Fonction qui permet de mettre un graphe issu d'un fichier texte généré via le programme Plantri
    dans une liste où chaque élément de la liste correspond aux arêtes du noeuds dont c'est l'indice. 

    Entrée: Fichier texte (.txt) incluant la représentation Plantri d'un graphe
    Sortie: Liste où chaque élément de la liste correspond aux arêtes du noeud dont c'est l'indice 

    Exemple:
        Entrée: 1[2 3 4 5] 2[1 5 4 3] 3[1 2 4] 4[1 3 2 5] 5[1 4 2]
        Sortie: [[2, 3, 4, 5], [1, 5, 4, 3], [1, 2, 4], [1, 3, 2, 5], [1, 4, 2]]
    """

    with open(filename, "r") as filin:
        line = filin.readline() # Lecture de la 1ère ligne du fichier
        # Avec une expression régulière on met dans une liste tous les éléments qui sont entre crochets []
        liste = re.findall(r"\[[\d|\s]+\]", line)
        graph = list()

        for vertex in liste :
            vertex = vertex.replace("[", "")
            vertex = vertex.replace("]", "")
            vertex = vertex.split(" ")
            graph.append(vertex) # indice de la liste correspond au noeud 

        # Tous les éléments de la liste deviennent de type int
        graph = [[int(i) for i in sub_graph] for sub_graph in graph]
        
        return graph
