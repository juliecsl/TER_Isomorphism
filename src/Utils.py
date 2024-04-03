# librairies 
import re
import matplotlib.pyplot as plt
import networkx as nx
import copy
import random


### ECRITURE/LECTURE DE GRAPHES ###


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


def GeneratePlanarCode(filename):
    """ 
    Fonction qui permet de séparer des graphes issus d'un fichier binaire générés via le programme Plantri
    dans des fichiers différents

    Entrée: Fichier binaire
    Sortie: Fichier texte (.txt) incluant la représentation Plantri d'un graphe ou web

    Exemple:
        Entrée: un fichier binaire
        Sortie: de nouveaux fichiers, 1 par graphe, format plantri web
    """
    ### LECTURE DU FICHIER ###
    with open(filename, "rb") as filin:
        # les 15 premiers charactères correspondent à la chaîne ">>planar_code<<"
        code = filin.read(15).decode('utf-8')
        # les autres charactères composent le ou les graphes
        data = filin.read()

    # on stocke en mémoire les graphes qu'on lit
    graphs_int = []
    # on a besoin de savoir le nombre de sommets dans les graphes que l'on traite
    taille = data[0]
        
    # on va séparer les grahes entre eux : on sait la taille des graphes (en nbr sommets) ainsi qu'apres un binaire zero on change de sommet (ou de graphe)
    debut = 0
    fin = -1
    conteur_sommets = 0
    for i in range(len(data)) :

        # si on lit un zero binaire, on change de sommet
        if data[i] == 0:
            conteur_sommets += 1
        
        # dans le cas où on a vu n sommets, n taille du graphe, on change de graphe
        if conteur_sommets == taille:
            fin = i
            res = ListBinaryToInt(data[debut:(fin+1)])
            graphs_int.append(res)

            # re-initialisation des variables 
            conteur_sommets = 0
            debut = fin + 1
    
    ### ENREGISTREMENT DES GRAPHES DANS DES FICHIERS ###
    
    # on regarde combien de graphes on a à la base 
    nbr_graphs = len(graphs_int)

    # on se dit que l'on veut 10 graphes au maximum 
    # cas où on en a moins de 10
    if nbr_graphs <= 10 :
        for i in range(nbr_graphs):
            filename = "FichierTests\ex" + str(taille) + '_' + str(i+1) + '.txt'
            WriteGraphInFile(graphs_int[i], filename)
    # cas où on en a plus de 10
    else:
        # contiendra le numéro des graphes deja choisis pour ne pas les reprendre
        hasard = []
        conteur = 1
        while conteur <= 10 :
            val = random.randint(0, (nbr_graphs-1))
            if val not in hasard:
                hasard.append(val)
                filename = "FichierTests\ex" + str(taille) + '_' + str(conteur) + '.txt'
                WriteGraphInFile(graphs_int[val], filename)
                conteur += 1
            

def ListBinaryToInt(content):
    """ 
    Fonction qui permet de passer d'une liste format binaire à une liste d'entiers
    
    Entrée : b'\x02\x03\x04\x05\x00\x01\x05\x04\x03\x00\x01\x02\x04\x00\x01\x03\x02\x05\x00\x01\x04\x02\x00'
    Sortie : [[2, 3, 4, 5], [1, 5, 4, 3], [1, 2, 4], [1, 3, 2, 5], [1, 4, 2]]
    """
    
    # le premier élément ne donne que le nombre de sommets, pas intéressant ici
    liste = content[1:]
    # on sépare chaque noeud (avec ses voisins) de ses voisins
    debut = 0
    graph = []
    for i in range(len(liste)):
        if liste[i] == 0 :
            graph.append(liste[debut:i])
            debut = i+1

    res = []
    # pour chaque noeud
    for vertex in graph :
        vertex = [vertex[i] for i in range(len(vertex))]
        res.append(vertex)

    return res


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



### DESSIN DE GRAPHE ###


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


### CREATION ISOMORPHISME ###


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


### EXECUTION DE COMMANDES ###

#GeneratePlanarCode('FichierTests\graph.100')