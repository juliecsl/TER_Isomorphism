from pynauty import *
from Utils import ReadGraph
import os

# important par convention les sommets sont numérotés à partir de 0
g1 = [[i-1 for i in ReadGraph("FichierTests/ex5_1.txt")[j] ]for j in range(len(ReadGraph("FichierTests/ex5_1.txt")))]
g2 = [[i-1 for i in ReadGraph("FichierTests/ex5_1.txt")[j] ]for j in range(len(ReadGraph("FichierTests/ex5_2.txt")))]

# on initialise les objects graphes 
g1_nauty = Graph(len(g1))
g2_nauty = Graph(len(g2))

# on mets sous forme de dictionnaire les listes d'adjacence
dic_g1 = {i:g1[i] for i in range(len(g1))}
dic_g2 = {i:g1[2] for i in range(len(g2))}

g1_nauty.set_adjacency_dict(dic_g1)
g2_nauty.set_adjacency_dict(dic_g2)

# résultat : false et true 
print(isomorphic(g1_nauty, g2_nauty))
print(isomorphic(g1_nauty, g1_nauty))