from Utils import *


# Méthode de test d'isomorphismes entre deux graphes de manière "naive"
# L'algorithme est le suivant : 
# - calcul de la signature pour le graphe 1
# - calcul de la signature pour le graphe 2
# - comparaison des deux signatures : s'il y a égalité, on a des graphes qui sont isomorphes


class Graph(object):
    """ Cette classe va nous fournir des caractéristiques des graphes """

    def __init__(self, graph) :

        self.graph = graph
    

    def get(self):
        
        return self.graph
    
    def len(self):
        
        return len(self.graph)

    
    def Edges(self):
        """
        Fonction qui retourne toutes les arêtes du graphe (on considère qu'il est non orienté) dans une liste.

        Entrée : le graphe sous forme de liste
        sortie : liste des arêtes
        """
        res = []
        # pour tous les noeuds
        for vertex in range(len(self.graph)):
            # pour tous les voisins du noeud
            for neighbor in self.graph[vertex]:
                # on ajoute l'arête (noeud, voisin) à la liste
                res.append((vertex+1, neighbor))
        
        return res
    

    def ParcoursProfondeurRecursifSurAretes(self, edge, visited):
        """
        Fonction récursive qui permet de parcourir en profondeur les arêtes non encore vues d'un graphe. A chaque appel, on met à jour
        l'ensemble des arêtes déjà traitées

        Entrée : le graphe sous forme de liste, l'arête que l'on traite, l'ensemble des arêtes déjà traitées dans l'ordre
        Sortie : rien - on met à jour la liste des arêtes visitées 
        """
        
        #on liste toutes les arêtes du graphe
        edges = self.Edges()
        #on ajoute l'arête à la liste des arêtes visitées
        visited.append(edge)

        # si l'arête est dans le graphe (vérification)
        if edge in edges:
            # regarder pour chaque voisin de la tête de l'arête, edge[1], si l'arête les reliant a été traité et si non la traiter
            for neighbor in self.graph[edge[1]-1]:
                if (edge[1], neighbor) not in visited:
                    self.ParcoursProfondeurRecursifSurAretes((edge[1], neighbor), visited)


    def ParcoursAretes(self, edge_debut):
        """
        Fonction qui permet de parcourir le graphe en profondeur sur les arêtes depuis une arête donnée

        Entrée : le graphe sous forme de liste
        Sortie : une liste avec tous les sommets dans l'ordre dans lesquelles on les passe 
        """
        # ensemble des arêtes dans l'ordre dans lesquelles on les a passée, mis à jour avec ParcoursProfondeurRecursif
        visited = list()
        # première instance pour le parcours en profondeur 
        self.ParcoursProfondeurRecursifSurAretes(edge_debut, visited)

        # initialisation de la liste avec le nom des sommets dans l'ordre que l'on voit dans le parcours
        res = [edge_debut[0]]
        # pour chaque arête visitée lors du parcours
        for edge in visited :
            # dans le cas où on voit une arête qui ne suit pas directement la dernière on ajoute sa queue à la liste
            if res[-1] != edge[0]:
                res.append(edge[0])
            # on ajoute la tête d'arête (nouveau sommet) à la liste
            res.append(edge[1])
        
        return res
    

    def Traduction(self, parcours):
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
        traduction =  [-1 for i in range(len(self.graph))]
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
    

    def Signature(self):
        """
        Fonction qui permet de générer une signature du graphe en s'appuyant seulement sur sa structure et non pas sur la 
        façon dont il a été nommé. On va générer des listes issues des parcours profondeur depuis chaque arête du graphe et 
        on choisit la plus "petite" (ordre croissant).

        Entrée : le graphe sous forme de liste
        Sortie : la signature
        """
        
        signatures = list()

        # on met dans une liste toutes les arêtes du graphe
        edges = self.Edges()
        # pour chaque arête, on génère la liste issue du parcours profondeur auquelle on applique la traduction
        for edge in edges :
            parcours = self.ParcoursAretes(edge)
            signatures.append(self.Traduction(parcours))
            
        return min(signatures)
        

def Isomorphisme1(graph1, graph2):
    """
    Fonction qui détermine si deux graphes sont isomorphes en comparant leur signature

    Entrée : deux graphes sous forme de liste
    Sortie : True s'ils sont isomorphes, False sinon
    """

    if graph1.Signature() == graph2.Signature():
        return True
    else :
        return False 


