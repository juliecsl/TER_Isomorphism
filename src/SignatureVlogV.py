from Utils import *
from DefineLambda import *
import time
import pstats
import cProfile
import sys

# Algorithme inspiré de l'article:
# J. E. HOPCROFT AND R. E. TARJAN, "A V log V Algorithm for Isomorphism 
# of Triconnected Planar Graphs," Computer Science Department, Cornell University, 
# Ithaca, NY, 1972

def FirstPartitioning(graph: list) -> dict:
    """
    Fonction qui permet de faire le premier partionnement des aretes. 
    Des aretes ayant le meme lambda (i.e meme nombre de degré entrant/sortant 
    et longueur de face droite/gauche) seront mises dans le meme bloc.

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
        lambda_edge = Lambda(edge, graph)

        if lambda_edge in dico_lambda.keys():
            dico_lambda[lambda_edge].append(edge)
        else:
            dico_lambda[lambda_edge] = [edge]

    return dico_lambda



def f(e: tuple, D: str, graph: list) -> tuple:
    """
    Fonction qui permet de trouver l'arc directement à droite ou à gauche de l'arc e.

    Entrée: e un tuple représentant un arc de la forme (tail, head)
            D un string prenant la valeur R ou L. 
                L pour trouver l'arc directement à gauche (Left)
                R pour trouver l'arc directement à droite (Right)
    Sortie: tuple de la forme (tail, head)
    """
    tail = e[0]  # n° de la queue de l'arc e
    head = e[1]  # n° de la tete l'arc e

    if D == 'L':
        i = graph[head-1].index(tail) # on met dans une variable la place de l'arête (head, tail)
        new_head = graph[head-1][(i-1)%len(graph[head-1])] # la nouvelle valeur du sommet qui est la tête est à gauche (-)
    elif D == 'R':
        i = graph[head-1].index(tail) # on met dans une variable la place de l'arête (head, tail)
        new_head = graph[head-1][(i+1)%len(graph[head-1])]
    
    e = (head, new_head)

    return e


def intersection(l1: list, l2: list) -> list:
    """
    Fonction qui retourne l'intersection des éléments de 2 listes.

    Utilisation de set dans la fonction pour améliorer la complexité en temps.

    Entrée: l1 et l2 des listes
    Sortie: une liste du resultat de (l1 ∩ l2)
    """

    # Passage sous forme de sets pour améliorer la complexité en temps.
    set_l1 = set(l1)
    set_l2 = set(l2)

    return list(set_l1.intersection(set_l2))


def find_block(dico: dict, e: tuple) -> tuple:
    """
    Fonction qui retrouve dans quel bloc (clé du dictionnaire) se trouve une arete e.

    Entrée: dico représentant le partionnement en blocs (dict)
            e une arete de la forme (tail, head) (tuple)
    Sortie: la clé du bloc où se trouve e (tuple)
    """

    # Parcours du dictionnaire
    for cle, valeurs in dico.items():
        if e in valeurs:
            return(cle)


def SignaturePartitionnement(graph: list) -> dict:
    """
    Fonction mimant le fonctionnement de l'algorithme proposé dans l'article:
    J. E. HOPCROFTANDR. E. TAaJAN,"A V log V AIgorithm for Isomorphism 
    of Triconnected Planar Graphs," Computer Science Department, Cornell University, 
    Ithaca, NY, 1972

    Les noms des variables et constantes proposées dans l'article ont été gardés.

    Entrée: Liste représentant les caractéristiques du graphe.
            De la forme: [[n2, n3, n4, n5], [n1, n5, n4, n3], [n1, n2, n4], ....]
    Sortie: Dictionnaire représentant la signature du graphe.
            De la forme {(caractéritique1): nb d'arcs, (caractéristique2): nb d'arcs, ...}
    """

    blocks = FirstPartitioning(graph) # Dictionnaire représentant les blocs de partionnement
    # Tri du dictionnaire dans l'ordre croissant
    # Pour que l'algo s'execute tjr dans le meme ordre de partitions
    blocks = dict(sorted(blocks.items()))

    # STATEMENT A
    PROCESS = list()
    # Pour chaque lambda (clé) du dictionnaire
    for i in blocks:
        PROCESS.append((i, 'R'))
        PROCESS.append((i, 'L'))
    
    # Tant que PROCESS est non vide
    while PROCESS:
        # STATEMENT C
        # Récupère un élément de PROCESS puis le supprime
        i = PROCESS[0][0]  # Lambda du bloc selectionné
        D = PROCESS[0][1]  # Direction L ou R
        del PROCESS[0]  # Suppression élément

        # STATEMENT G
        MOVE = list()

        # STATEMENT H
        # Pour chaque arete e du bloc i
        # On ajoute son arc directement à D (droite ou gauche) de lui dans MOVE
        for e in blocks[i]:
            # e est sous la forme d'un tuple (e1, e2)
            MOVE.append(f(e, D, graph))

        # initialisation de la liste qui retient quels blocs ont été crées dans le STATEMENT I
        blocks_created = list()

        # STATEMENT I
        # Pour chaque arete de MOVE
        for e in MOVE:
            j = find_block(blocks, e)  # La clé du bloc de e
            Bj = list(blocks[j])  # liste contenant tous les élements du bloc j

            # STATEMENT J
            inter = intersection(Bj, MOVE)
            inter.sort()
            Bj.sort()

            if inter != Bj:
                # Si le bloc B(j) contient plus d'une arete
                # (i.e. Si on peut split des éléments)
                if len(blocks[j]) > 1:
                    # Création du nom du nouveau bloc B(j')
                    j_prime = (j, i, D)  # nom de la forme (bloc découpé, bloc parent, direction)

                    # Si B(j') n'est pas encore crée
                    if j_prime not in blocks:
                        # Création de B(j') et insertion de e
                        blocks[j_prime] = [e]
                        blocks_created.append((j, j_prime))
                    else:
                        # Insertion de e si le bloque était déjà existant
                        blocks[j_prime].append(e)
                    # Suppression de e du bloc B(j)
                    blocks[j].remove(e)
        
        # STATEMENT K
        for elem in blocks_created:
            j = elem[0]
            j_prime = elem[1]
            for D in ("L", "R"):
                if (j, D) in PROCESS:
                    PROCESS.append((j_prime, D))
                elif len(blocks[j_prime]) <= len(blocks[j]):
                    PROCESS.append((j_prime, D))
                else:
                    PROCESS.append((j, D))

    # Standardise la signature pour qu'elle n'est pas de numéro d'arc.
    for key in blocks:
        blocks[key] = len(blocks[key])
        
    return blocks





    
### COMMANDES TESTS ###

# filename1 = "FichierTests/ex6_1.txt"
# graph1 = ReadGraph(filename1)
# print(FirstPartitioning(graph1))
# print("")
# # # before_memory = sys.getallocatedblocks()
# s1 = SignaturePartitionnement(graph1)
# print(s1)

# Draw(graph1)

# filename2 = "FichierTests/ex220_1.txt"
# graph2 = ReadGraph(filename2)
# print(est_iso(graph1, graph2))


# print(s1)
# diff_memory = sys.getallocatedblocks() - before_memory
# print(f'{diff_memory} blocs supplémentaires alloués')
# print("Taille signature:", sys.getsizeof(s1), "octets.")

# Pour regarder le temps que prennent les lignes de code:
# cProfile.run("main(graph1)", "my_func_stats")
# p = pstats.Stats("my_func_stats")
# p.sort_stats("cumulative").print_stats()


# execution_time = timeit.timeit("main(graph1)", globals=globals(), number=10)
# print("Temps d'exécution:", execution_time, "secondes")
# start = time.time()
# signature1 = main(graph1)


