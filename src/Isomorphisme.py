
# Import à l'interieur des fonctions pour éviter des problemes d'import circulaire

def IsomorphismeNaif(graph1, graph2):
    """
    Fonction qui détermine si deux graphes sont isomorphes en comparant leur signature obtenue par la version naive

    Entrée : deux graphes sous forme de liste
    Sortie : True s'ils sont isomorphes, False sinon
    """
    from SignatureNaive import SignatureParcours

    return SignatureParcours(graph1) == SignatureParcours(graph2)


def IsomorphismeWeinberg(graph1, graph2):
    """
    Fonction qui détermine si deux graphes sont isomorphes en comparant leur signature obtenue par la version naive

    Entrée : deux graphes sous forme de liste
    Sortie : True s'ils sont isomorphes, False sinon
    """
    from SignatureWeinberg import SignatureParcours

    return SignatureParcours(graph1) == SignatureParcours(graph2)



def IsomorphismePartitionnement(graph1, graph2):
    """
    Fonction qui détermine si deux graphes sont isomorphes en comparant leur signature obtenue par la version VlogV

    Entrée : deux graphes sous forme de liste
    Sortie : True s'ils sont isomorphes, False sinon
    """
    from SignatureVlogV import SignaturePartitionnement

    return SignaturePartitionnement(graph1) == SignaturePartitionnement(graph2)

    

def IsomorphismeNauty(filename1, filename2):
    """
    Fonction qui détermine si deux graphes sont isomorphes en comparant leur signature obtenue par la version Nauty

    Entrée : deux fichiers.txt
    Sortie : True s'ils sont isomorphes, False sinon
    """
    from Nauty import IsoNauty

    return IsoNauty(filename1, filename2)