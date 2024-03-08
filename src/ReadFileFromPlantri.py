# on ne peut générer des fichiers de la version programme plantri que sur des machines UNIX
# ./plantri 5 -a test.txt (un graphe planaire à 5 sommets)

filename = "FichierTests/graph6.txt"

def ReadGraph2(filename):
    """ 
    Fonction qui permet de mettre un graphe issu d'un fichier texte généré via le programme Plantri
    dans une liste où chaque élément de la liste correspond aux arêtes du noeuds dont c'est l'indice. 

    Entrée: Fichier texte (.txt) incluant la représentation Plantri d'un graphe
    Sortie: Liste où chaque élément de la liste correspond aux arêtes du noeud dont c'est l'indice 

    Exemple:
        Entrée: 5 bcde,aedc,abd,acbe,adb
        Sortie: [[2, 3, 4, 5], [1, 5, 4, 3], [1, 2, 4], [1, 3, 2, 5], [1, 4, 2]]
    """

    with open(filename, "r") as filin:
        line = filin.readline() # lecture de la 1ère ligne du fichier

        liste = line.split(" ") # on sépare la ligne entre le nombre de noeuds et le reste
        nbr_vertex = liste[0] # nombre de noeuds du graphe
        liste = liste[1].split(",") # chaque élément de la liste correspond aux noeuds voisins du noeud indice

        graph = list()

        for vertex in liste :
            vertex = [ord(vertex[i]) - 96 for i in range(len(vertex))] # la fonction ord permet de passer d'un caractère ascii à un entier
            graph.append(vertex) # indice de la liste correspond au noeud 


        return graph
    
#print(ReadGraph2(filename))