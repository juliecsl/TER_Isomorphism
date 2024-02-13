import re

filename = "graph2.txt"


def ReadGraph(filename):
    """ fonction qui permet de mettre un graphe sous forme de fichier texte dans une liste où chaque \
         élément de la liste correspond aux arêtes du noeuds dont c'est l'indice """

    with open(filename, "r") as filin:
        ligne = filin.readline() # on a une ligne par fichier
        liste = re.findall(r"\[[\d|\s]+\]", ligne) # avec une expression régulière on met dans une liste tous les éléments entre crochets
        graph = list()
        for noeud in liste :
            noeud = noeud.replace("[", "")
            noeud = noeud.replace("]", "")
            noeud = noeud.split(" ")
            graph.append(noeud) # indice de la liste correspond au noeud 

        graph = [[int(i) for i in sous_graph] for sous_graph in graph]
        
        return graph

graphe = ReadGraph(filename)
print(graphe)

# comment faire pour l'orientation ? Dans notre fichier, elle est mauvaise 

def Degreesnoeuds(noeuds):
    """ fonction qui renvoie le nombre d'arêtes relié à un noeud """
    return len(graphe[noeuds-1])


def NombreAretesFaceDroite(arete):
    """ fonction qui donne le nombre arêtes sur la face droite d'une arête  : arête (queue, tête) """
    
    tail = arete[0]
    head = arete[1]
    count = 1

    while head != arete[0]:
        indice = graphe[head-1].index(tail) # on met dans une variable la place de l'arête (head, tail)
        tail = head 
        head = graphe[head-1][(indice+1)%len(graphe[head-1])] # la nouvelle valeur du sommet qui est la tête est à droite (+)
        count += 1
    
    return count

print(NombreAretesFaceDroite((1,2)))


def NombreAretesFaceGauche(arete):
    """ fonction qui donne le nombre arêtes sur la face gauche d'une arête """
    
    tail = arete[0]
    head = arete[1]
    count = 1

    while head != arete[0]:
        indice = graphe[head-1].index(tail) # on met dans une variable la place de l'arête (head, tail)
        tail = head 
        head = graphe[head-1][(indice-1)%len(graphe[head-1])] # la nouvelle valeur du sommet qui est la tête est à gauche (-)
        count += 1
    
    return count

print(NombreAretesFaceDroite((1,2)))