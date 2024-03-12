from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from src.Utils import *
from DefineLambda import *

filename = "FichierTests/graph2.txt"

graph = ReadGraphFromWeb(filename) 

def FirstPartitioning(graph: list) -> dict:
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

def f(e: tuple, D: str) -> tuple:
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


def main(graph: list):
    """
    Fonction principale de l'algorithme à appeler pour faire fonctionner le programme.

    Entrée:
    Sortie:
    """

    blocks = FirstPartitioning(graph) # Dictionnaire représentant les blocs de partionnement

    # STATEMENT A
    PROCESS = set()
    # Pour chaque lambda (clé) du dictionnaire
    for i in blocks:
        PROCESS.add((i, 'R'))
        PROCESS.add((i, 'L'))
    
    # Tant que PROCESS est non vide
    while PROCESS:
        # STATEMENT C
        elem = PROCESS.pop() # Récupère un élément de PROCESS et le supprime
        i = elem[0]  # Lambda du bloc selectionné
        D = elem[1]  # Direction L ou R

        # STATEMENT G
        MOVE = set()

        # STATEMENT H
        # Pour chaque arete e du bloc i
        # On ajoute son arc directement à D (droite ou gauche) de lui dans MOVE
        for e in blocks[i]:
            # e est sous la forme d'un tuple (e1, e2)
            MOVE.add(f(e, D))

        # STATEMENT I
        # Pour chaque arete de MOVE
        for e in MOVE:
            j = find_block(blocks, e)  # La clé du bloc de e
            Bj = set(blocks[j])  # set contenant tous les élements du bloc j

            # STATEMENT J
            inter = Bj.intersection(MOVE)

            if inter != Bj:
                pass

main(graph)
# print(graph)

