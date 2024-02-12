import re

filename = "graph1.txt"

def ReadGraph(filename):

    with open(filename, "r") as filin:
        ligne = filin.readline()
        while ligne != "":
            print(ligne)
            liste = re.findall(r"\[[\d|\s]+\]", ligne)
            graph = list()
            for noeud in liste :
                noeud = noeud.replace("[", "")
                noeud = noeud.replace("]", "")
                noeud = noeud.split(" ")
                graph.append(noeud)
            ligne = filin.readline()
        print(graph)
        graph = [[int(i) for i in sous_graph] for sous_graph in graph]
        print(graph)

ReadGraph(filename)
