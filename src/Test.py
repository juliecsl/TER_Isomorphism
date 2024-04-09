import unittest

from Utils import *
from Isomorphisme import *
from SignatureVlogV import *

# Tests du module Utils

class TestUtils(unittest.TestCase):

    def setUp(self):
        self.filename1 = "FichierTests/graph5_1.txt"
        self.filename2 = "FichierTests/graph5_1ISO.txt"

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

        filename1 = "FichierTests/ex100_9.txt"
        self.graph1 = ReadGraph(filename1)

        filename1bis = "FichierTests/ex100_8.txt"
        self.graph1bis = ReadGraph(filename1bis)

        create_isomorphism(filename1)
        filename1ter = "FichierTests/ex100_9ISO.txt"
        self.graph1ter = ReadGraph(filename1ter)


    def test1_isomorphisme(self):
        
        self.assertEqual(IsomorphismeNaif(self.graph1, self.graph1ter), True, 'graphes isomorphes')
        
    def test2_isomorphisme(self):
        
        self.assertEqual(IsomorphismeNaif(self.graph1, self.graph1bis), False, 'graphes non isomorphes')


class TestVersionVlogV(unittest.TestCase):
    
    def setUp(self):

        filename1 = "FichierTests/ex50_1.txt"
        self.graph1 = ReadGraph(filename1)

        filename1bis = "FichierTests/ex50_8.txt"
        self.graph1bis = ReadGraph(filename1bis)

        create_isomorphism(filename1)
        filename1ter = "FichierTests/ex50_1ISO.txt"
        self.graph1ter = ReadGraph(filename1ter)


    def test1_isomorphisme(self):
        
        self.assertEqual(IsomorphismePartitionnement(self.graph1, self.graph1ter), True,
                         'graphes isomorphes')
        
    def test2_isomorphisme(self):
    
        self.assertEqual(IsomorphismePartitionnement(self.graph1, self.graph1bis), False, 'graphes non isomorphes')


if __name__ == '__main__':
    unittest.main()