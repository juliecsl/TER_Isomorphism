
# Import à l'interieur des fonctions pour éviter des problemes d'import circulaire

def IsomorphismeNaif(graph1, graph2):
    """
    Fonction qui détermine si deux graphes sont isomorphes en comparant leur signature obtenue par la version naive

    Entrée : deux graphes sous forme de liste
    Sortie : True s'ils sont isomorphes, False sinon
    """
    from SignatureNaive import SignatureParcours

    if SignatureParcours(graph1) == SignatureParcours(graph2):
        return True
    else :
        return False


def IsomorphismePartitionnement(graph1, graph2):
    """
    Fonction qui détermine si deux graphes sont isomorphes en comparant leur signature obtenue par la version VlogV

    Entrée : deux graphes sous forme de liste
    Sortie : True s'ils sont isomorphes, False sinon
    """
    from SignatureVlogV import SignaturePartitionnement

    if SignaturePartitionnement(graph1) == SignaturePartitionnement(graph2):
        return True
    else :
        return False
    

def IsomorphismeNauty(filename1, filename2):
    """
    Fonction qui détermine si deux graphes sont isomorphes en comparant leur signature obtenue par la version Nauty

    Entrée : deux fichiers.txt
    Sortie : True s'ils sont isomorphes, False sinon
    """
    from IsomorphismeNauty import IsoNauty

    return IsoNauty(filename1, filename2)