from SignatureNaive import SignatureParcours
from SignatureVlogV import SignaturePartitionnement
from IsomorphismeNauty import IsoNauty

def IsomorphismeNaif(graph1, graph2):
    """
    Fonction qui détermine si deux graphes sont isomorphes en comparant leur signature obtenue par la version naive

    Entrée : deux graphes sous forme de liste
    Sortie : True s'ils sont isomorphes, False sinon
    """

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

    return IsoNauty(filename1, filename2)