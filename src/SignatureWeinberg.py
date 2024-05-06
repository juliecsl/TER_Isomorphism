from Utils import *
import pstats
import cProfile
import sys
sys.setrecursionlimit(10000)  # Définit la limite de récursion à 10000

def ParcoursProfondeurRecursifSurAretes(graph, edge, visited_edges, visited_vertex):
    """
    Fonction récursive qui permet de parcourir en profondeur les arêtes non encore vues d'un graphe. A chaque appel, on met à jour
    l'ensemble des arêtes déjà traitées
    
    Entrée : le graphe sous forme de liste, l'arête que l'on traite, l'ensemble des arêtes déjà traitées dans l'ordre
    Sortie : rien - on met à jour la liste des arêtes visitées 
    """

    #on ajoute l'arête à la liste des arêtes visitées
    visited_edges.add(edge)
    visited_vertex.append(edge[0])

    # on regarde les voisins et on les prends dans l'ordre à droite de celle d'où l'on vient
    voisins = graph[edge[1]-1]
    indice = voisins.index(edge[0])
    regarder = voisins[(indice+1):] + voisins[:(indice+1)]

    # cas où la tete a déjà été visitée
    if edge[1] in visited_vertex:

        # si l'arête inverse n'a pas été visitée
        if ((edge[1], edge[0]) not in visited_edges):
            ParcoursProfondeurRecursifSurAretes(graph, (edge[1], edge[0]), visited_edges, visited_vertex)
        
        # sinon on prend celle de droite
        elif (edge[1], edge[0]) in visited_edges :
            # regarder pour chaque voisin de la tête de l'arête, edge[1], si l'arête les reliant a été traité et si non la traiter
            for neighbor in regarder:
                if ((edge[1], neighbor) not in visited_edges):
                    ParcoursProfondeurRecursifSurAretes(graph, (edge[1], neighbor), visited_edges, visited_vertex)

    # si le sommet n'a pas été visité        
    else :
        ParcoursProfondeurRecursifSurAretes(graph, (edge[1], regarder[0]), visited_edges, visited_vertex)



def ParcoursAretes(graph, edge_debut):
    """
    Fonction qui permet de parcourir le graphe en profondeur sur les arêtes depuis une arête donnée

    Entrée : le graphe sous forme de liste
    Sortie : une liste avec tous les sommets dans l'ordre dans lesquelles on les passe 
    """
    
    # ensemble des arêtes dans l'ordre dans lesquelles on les a passée, mis à jour avec ParcoursProfondeurRecursif
    visited_edges = set()
    visited_vertex = list()
    # première instance pour le parcours en profondeur 
    ParcoursProfondeurRecursifSurAretes(graph, edge_debut, visited_edges, visited_vertex)
    visited_vertex.append(visited_vertex[0])
        
    return visited_vertex

def Traduction(graph, parcours):
    """
    Fonction qui renome les sommets de la liste obtenue lors du parcours profondeur en fontion de leur traitement,
    plus on les voit tôt, plus leur numéro est faible

    Entrée : une liste avec tous les sommets dans l'ordre dans lesquelles on les passe
    Sortie : la liste avec les sommets renommés

    Exemple:
        Entrée: [2, 1, 4, 3, 4, 3, 2]
        Sortie: [1, 2, 3, 4, 3, 4, 1]
    """
    
    # initialisation de la liste qui va nous permettre de garder en mémoire les changements de noms 
    traduction =  [-1 for i in range(len(graph))]
    # initialisation du compteur qui nous permettra de renommer les sommets
    k = 1

    res = list()
    
    # pour chaque sommet de la liste d'entrée
    for vertex in parcours:
        # si c'est la première fois que l'on rencontre ce sommet
        if traduction[vertex-1] == -1:
            # on ajoute dans le dictionnaire le sommet avec sa nouvelle traduction (k actuel) et on incrémente k pour le prochain cas
            traduction[vertex-1] = k
            k += 1
        res.append(traduction[vertex-1])
    
    return res


def SignatureParcours(graph):
    """
    Fonction qui permet de générer une signature du graphe en s'appuyant seulement sur sa structure et non pas sur la 
    façon dont il a été nommé. On va générer des sigatures issues de parcours en profondeur depuis chaque arête du graphe et 
    on choisit la plus "petite" (ordre croissant).

    Entrée : le graphe sous forme de liste
    Sortie : la signature
    """
    signatures = list()
    taille = len(graph)

    ### on énumère toutes les arêtes en considérant les deux sens ###
    
    edges = []
    for vertex in range(taille):
        # pour tous les voisins du noeud
        for neighbor in graph[vertex]:
            # on ajoute l'arête (noeud, voisin) à la liste 
            edges.append((vertex+1, neighbor))
        
    ### pour chaque arête, on génère la signature auquelle on applique la traduction (car on ne prend pas compte des noms des sommets) ###

    # on ne traduit que les signatures qui sont de taille plus petite ou égale à celles déjà générées
    taille_parcours_minimum = 10e6                            # initialisation

    for edge in edges:
        parcours = ParcoursAretes(graph, edge)
        taille_parcours = len(parcours)

        if taille_parcours <= taille_parcours_minimum :
            signatures.append(Traduction(graph, parcours))
            taille_parcours_minimum = taille_parcours

    longueur_min = min(len(liste) for liste in signatures)
    signatures_longueur_min = [liste for liste in signatures if len(liste) == longueur_min]

    return min(signatures_longueur_min)


# graph1 = ReadGraph("FichierTests/ex200_1.txt")
# cProfile.run("SignatureParcours(graph1)", "my_func_stats")
# p = pstats.Stats("my_func_stats")
# p.sort_stats("cumulative").print_stats()