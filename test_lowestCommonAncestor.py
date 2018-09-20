from BST import BST
import unittest

class TestStringMethods(unittest.TestCase):

    def testPutRoot(self):

    	tree = BST()
    	tree.put(11,"Ashbourne")
        self.assertEqual(tree.getRoot().getKey(), 11)


    def testGet(self):
    	tree = BST()
    	tree.put(50,"Newry")
    	tree.put(80,"Azerbijan")
    	tree.put(120,"Navan")
    	tree.put(110,"Napoli")
    	tree.put(11,"Japan")
    	tree.put(5,"Ashbourne")
    	tree.put(18,"cyprus")
    	tree.put(9,"NEW YORK CITY BABY")
    	tree.put(70,"LA Police Department")
    	tree.put(105,"Bermuda")
    	tree.put(79,"bali")
    	tree.put(78,"Atlantis")
    	tree.put(75,"Paris")
    	tree.getPathToNode(75)
    	tree.printVertexPath(tree.getPathsOfNVertices([9]))
        self.assertEqual(tree.get(9).getValue(),"NEW YORK CITY BABY")



if __name__ == '__main__':
    unittest.main()
'''
my_list = BST();
my_list.put(9,"Conor") 
my_list.put(12,"Kate") 
my_list.put(10,"James") 
my_list.put(7,"Fearghal") 
my_list.printInOrder()
'''