from ReadFile import *

filename = "FichierTests/graph2.txt"

graph = ReadGraph(filename)  # Remarque: pas une var globale mais est quand meme connu par les fonctions ci dessous ???
# print(graph)
 

def VertexDegrees(vertex):
    """ 
    Fonction qui renvoie le degré d'un sommet.
    Entrée: Sommet (int)
    Sortie: Degré du sommet (int)
    """
    return len(graph[vertex-1])


def RightFaceCardinality(edge):
    """ 
    Fonction qui donne le nombre arêtes sur la face immédiatement à droite d'un arc. 
    (i.e. donne la taille de la face) 

    Entrée: Arc sous forme de tuple (queue, tete)
    Sortie: Taille de la face immédiatement à droite de "arete" (int)
    """
    
    tail = edge[0]
    head = edge[1]
    count = 1

    while head != edge[0]:
        indice = graph[head-1].index(tail) # on met dans une variable la place de l'arête (head, tail)
        tail = head 
        head = graph[head-1][(indice+1)%len(graph[head-1])] # la nouvelle valeur du sommet qui est la tête est à droite (+)
        count += 1
    
    return count

# print(RightFaceCardinality((1,2)))


def LeftFaceCardinality(edge):
    """ 
    Fonction qui donne le nombre arêtes sur la face immédiatement à gauche d'un arc. 
    (i.e. donne la taille de la face) 

    Entrée: Arc sous forme de tuple (queue, tete)
    Sortie: Taille de la face immédiatement à gauche de "arete" (int)
    """
    
    tail = edge[0]
    head = edge[1]
    count = 1

    while head != edge[0]:
        indice = graph[head-1].index(tail) # on met dans une variable la place de l'arête (head, tail)
        tail = head 
        head = graph[head-1][(indice-1)%len(graph[head-1])] # la nouvelle valeur du sommet qui est la tête est à gauche (-)
        count += 1
    
    return count

# print(LeftFaceCardinality((1,2)))

def Lambda(edge):
    """
    
    Fonction qui renvoie un tuple unique de la forme (face gauche, face droite, degré tail, degré head)
    
    Entrée: Arc sous forme de tuple (queue, tete)
    Sortie : tuple (face gauche, face droite, degré tail, degré head) 
    
    """

    lambda_res = (LeftFaceCardinality(edge), RightFaceCardinality(edge), VertexDegrees(edge[0]), VertexDegrees(edge[1]))
    
    return lambda_res


def SameLambda(edge1, edge2):
    """
    
    Fonction qui renvoie True si les arêtes sont indiscernables et False sinon
    
    Entrée : Deux arcs edge1 et edge2 sous la forme de tuple (queue, tete)
    Sortie : True su les arêtes sont indiscernables, False sinon
    
    """

    return True if Lambda(edge1) == Lambda(edge2) else False

# print(SameLambda((2,3), (4,5)))
# print(SameLambda((1,2), (4,5)))