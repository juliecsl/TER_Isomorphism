# librairies 
import re
import matplotlib.pyplot as plt
import networkx as nx
import copy

# Fonctions utiles pour notre TER


def WriteGraphInFile(graph, filename):
    """
    Fonction qui permet à partir d'un graphe, de créer un fichier pour le stocker comme ceux lu depuis plantri web.

    Entrée : un graph sous forme de liste, le nom du fichier sous lequel on le stockera.
    Sortie : - 
    """
    # on garde l'ordre des voisins mais on commence par celui le plus petit pour chaque sommet (norme plantri)
    for i in range(len(graph)):
        ind = graph[i].index(min(graph[i]))
        a = graph[i][ind:]
        b = graph[i][:ind]
        graph[i] = a + b
        
    with open(filename, "w") as file:
        for i in range(len(graph)):
            string = str(i+1) + '[' + ' '.join(map(str,graph[i])) + ']' + ' '
            file.write(string)


def ReadGraphFromWeb(content):
    """ 
    Fonction qui permet de mettre un graphe issu d'un fichier texte généré via le programme Plantri version web
    dans une liste où chaque élément de la liste correspond aux arêtes du noeuds dont c'est l'indice. 

    Entrée: chaine de caractère incluant la représentation Plantri d'un graphe
    Sortie: Liste où chaque élément de la liste correspond aux arêtes du noeud dont c'est l'indice 

    Exemple:
        Entrée: "1[2 3 4 5] 2[1 5 4 3] 3[1 2 4] 4[1 3 2 5] 5[1 4 2]"
        Sortie: [[2, 3, 4, 5], [1, 5, 4, 3], [1, 2, 4], [1, 3, 2, 5], [1, 4, 2]]
    """
       
    # Avec une expression régulière on met dans une liste tous les éléments qui sont entre crochets []
    liste = re.findall(r"\[[\d|\s]+\]", content)
    graph = list()

    # pour chaque noeud
    for vertex in liste :
        vertex = vertex.replace("[", "")
        vertex = vertex.replace("]", "")
        vertex = vertex.split(" ")
        graph.append(vertex) # indice de la liste correspond au noeud 

    # Tous les éléments de la liste deviennent de type int
    graph = [[int(i) for i in sub_graph] for sub_graph in graph]
        
    return graph    
    

# on ne peut générer des fichiers de la version programme plantri que sur des machines UNIX
# ./plantri 5 -a test.txt (un graphe planaire à 5 sommets)

def ReadGraphFromPlantriAscii(content):
    """ 
    Fonction qui permet de mettre un graphe issu d'un fichier texte généré via le programme Plantri
    dans une liste où chaque élément de la liste correspond aux arêtes du noeuds dont c'est l'indice. 
    ATTENTION ON NE PEUT GENERER QUE DES GRAPHES DE 30 SOMMETS MAXIMUM AVEC LA METHODE ASCII

    Entrée: Fichier texte (.txt) incluant la représentation Plantri d'un graphe
    Sortie: Liste où chaque élément de la liste correspond aux arêtes du noeud dont c'est l'indice 

    Exemple:
        Entrée: 5 bcde,aedc,abd,acbe,adb
        Sortie: [[2, 3, 4, 5], [1, 5, 4, 3], [1, 2, 4], [1, 3, 2, 5], [1, 4, 2]]
    """

    # on sépare la ligne entre le nombre de noeuds et le reste
    liste = content.split(" ")
    # on sépare chaque noeud (avec ses voisins) de ses voisins
    liste = liste[1].split(",") 
    graph = list()

    # pour chaque noeud
    for vertex in liste :
        # la fonction ord permet de passer d'un caractère ascii à un entier (-96 car on veut des noms de noeuds qui commencent à 1)
        vertex = [ord(vertex[i]) - 96 for i in range(len(vertex))]
        # indice de la liste correspond au nom du noeud 
        graph.append(vertex) 

    return graph


def ReadGraph(filename):
    """ 
    Fonction qui permet de mettre un graphe issu d'un fichier texte généré via le programme Plantri
    dans une liste où chaque élément de la liste correspond aux arêtes du noeuds dont c'est l'indice. 

    Entrée: Fichier texte (.txt) incluant la représentation Plantri d'un graphe ou web
    Sortie: Liste où chaque élément de la liste correspond aux arêtes du noeud dont c'est l'indice 

    Exemple:
        Entrée: 5 bcde,aedc,abd,acbe,adb
        Sortie: [[2, 3, 4, 5], [1, 5, 4, 3], [1, 2, 4], [1, 3, 2, 5], [1, 4, 2]]
    """
    with open(filename, "r") as filin:
        line = filin.readline()
        # cas où on est dans une représentation générée par le programme Plantri
        if "a" in line:
            return ReadGraphFromPlantriAscii(line)
        # cas où on est dans une représentation générée par le web
        else:
            return ReadGraphFromWeb(line)


def Draw(graphe):
    """
    Fonction qui permet d'afficher le graphe sous forme planaire dans une nouvelle fenêtre.

    Entrée : graphe sous forme de liste
    Sortie : -
    """

    g = nx.Graph()
    # génération de toutes les arêtes du graphe
    edges = []
    for vertex in range(len(graphe)):
        for neighbor in graphe[vertex]:
            edges.append((vertex+1, neighbor))
    # on ajoute les arêtes au dessin
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


def create_isomorphism(filename: str, pos: list = [[1, 3]]) -> list:
    """
    Fonction qui créée un graphe isomorphe à celui passé en argument. 
    Par défaut, échange des noms de noeuds 1 et 3. 

    Entrée: chemin du fichier contenant la liste du graphe, liste des positions à échanger:
    Sortie: graphe isomorphe
    """

    graph = ReadGraph(filename)
    iso = []
    # nom du nouveau fichier
    new_filename = filename.split('.')[0] + 'ISO' + '.txt'

    # Inversion des positions de liste dans la liste du graphe
    for position in pos:
        l1 = graph[position[0]-1]
        l2 = graph[position[1]-1]

        graph[position[0]-1] = l2
        graph[position[1]-1] = l1
    
    # initialisation de la liste contenant l'isomorphisme du graphe
    iso = copy.deepcopy(graph)
    for i in range(len(iso)):
        for j in range(len(iso[i])):
            iso[i][j] = 0
    
    # on regarde les élements du graphe 1 à 1
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            # Pour chaque couple de position à échanger 
            for position in pos: 
                # échange de position
                if graph[i][j] == position[0]: 
                    iso[i][j] = position[1]
                # échange de position
                elif graph[i][j] == position[1]:  
                    iso[i][j] = position[0]
            # si le numéro de noeud n'est pas à changer
            if iso[i][j] == 0:  
                iso[i][j] = graph[i][j]
    
    WriteGraphInFile(iso, new_filename)