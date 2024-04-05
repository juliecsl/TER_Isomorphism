from SignatureNaive import SignatureParcours
from SignatureVlogV import SignaturePartitionnement

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