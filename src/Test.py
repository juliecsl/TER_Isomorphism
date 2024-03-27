import unittest
from Utils import *
from Version_naive import *

# Tests du module Utils

class TestUtils(unittest.TestCase):

    def setUp(self):
        self.filename1 = "FichierTests/graph2.txt"
        self.filename2 = "FichierTests/graph2ISO.txt"

    def test1_create_isomorphism(self):

        create_isomorphism(self.filename1, [[2,5],[1,3]])
        res = [[3, 5, 4], [3, 4, 5], [1, 4, 2, 5], [1, 5, 2, 3], [1, 3, 2, 4]]
        
        self.assertEqual(ReadGraph(self.filename2), res)

    def test2_create_isomorphism(self):

        create_isomorphism(self.filename1, [[1,3],[2,5]])
        res = [[3, 5, 4], [3, 4, 5], [1, 4, 2, 5], [1, 5, 2, 3], [1, 3, 2, 4]]
        
        self.assertEqual(ReadGraph(self.filename2), res)

# Tests de la version naïve
    
class TestVersionNaive(unittest.TestCase):
    
    def setUp(self):

        filename1 = "FichierTests/graph1.txt"
        self.graph1 = Graph(ReadGraph(filename1))

        filename1bis = "FichierTests/graph1PASISO.txt"
        self.graph1bis = Graph(ReadGraph(filename1bis))
        
        filename2 = "FichierTests/graph2.txt"
        self.graph2 = Graph(ReadGraph(filename2))

        filename2bis = "FichierTests/graph2bis.txt"
        self.graph2bis = Graph(ReadGraph(filename2bis))


    def test1_isomorphisme(self):
        
        self.assertEqual(Isomorphisme1(self.graph2, self.graph2bis), True,
                         'graphes isomorphes')
        
    def test2_isomorphisme(self):
        
        self.assertEqual(Isomorphisme1(self.graph1, self.graph1bis), False, 'graphes non isomorphes')
        


if __name__ == '__main__':
    unittest.main()