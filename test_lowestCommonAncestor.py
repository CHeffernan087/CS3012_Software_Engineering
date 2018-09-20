from BST import BST
import unittest

class TestStringMethods(unittest.TestCase):

    def testPutRoot(self):

    	tree = BST()
    	tree.put(11,"Ashbourne")
        self.assertEqual(tree.getRoot().getKey(), 11)


    def testGet(self):
    	tree = BST()
    	keys = [100,50,200,25,75,150,250,10,36,63,8,125,175,225,290,20,27,47,55,70,77,90,110,137,163,190,213,230,270,300]
        values = ["Newry","Azerbijan","Navan","Napoli","Japan","Ashbourne","Cyprus","New York City Baby","L.A.P.D","Bermud","Bali","Atlantis","Paris","Memphis","Florida","Summerhill","Castlebar",
        "London","Kent","Gloucester","Verona","Raheny","Vienna","Washington","Zanzibar","Crete","Panama","Miltown","Leopardstown","Cape town","Alkatraz","Diagon-alley","Jellystone Park","Rathoath"]
    	i = 0;
    	for key in keys:
    		tree.put(key,values[i])
    		i = i+1
    	tree.printVertexPath(tree.getPathsOfNVertices([75]))
        self.assertEqual(tree.get(150).getValue(),"Ashbourne")
        self.assertEqual(tree.getLowestCommonAncestor([137,163,213]).getKey(),200)




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