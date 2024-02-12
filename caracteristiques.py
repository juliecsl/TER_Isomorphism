import re

filename = "graph1.txt"

def ReadGraph(filename):

    with open(filename, "r") as filin:
        ligne = filin.readline()
        while ligne != "":
            print(ligne)
            graphe = re.split(r"\d\[", ligne)
            ligne = filin.readline()
        
        print(graphe)

ReadGraph(filename)
