from BST import BST
from Node import Node
import unittest

class TestStringMethods(unittest.TestCase):

    
    '''
        put => tested
        getRoot => tested
        get => tested
        printInOrder => tested 
        findMin =>
        getPathToNode =>
        getPathToNVertices =>
        printVertexPath =>
        getLowestCommonAncestor => 
        
    '''


    def testNodeCreation(self):
        testNode = Node("Conor",21)
        self.assertEqual(testNode.getKey(),"Conor")
        self.assertEqual(testNode.getValue(),21)
        self.assertEqual(testNode.toString(),"Conor : 21")




    def testPutRoot(self):

    	tree = BST()
    	tree.put(11,"Ashbourne")
        self.assertEqual(tree.getRoot().getKey(), 11)


    def testPutRight(self):
        tree = BST()
        tree.put(1,"a")
        tree.put(2,"b")
        tree.put(3,"c")
        tree.put(4,"d")
        tree.put(5,"e")
        tree.put(6,"f")
        tree.put(7,"g")

        self.assertEqual(tree.getRoot().getValue(), "a")
        self.assertEqual(tree.getRoot().getRight().getValue(), "b")
        self.assertEqual(tree.getRoot().getRight().getRight().getValue(), "c")
        self.assertEqual(tree.getRoot().getRight().getRight().getRight().getValue(), "d")
        self.assertEqual(tree.getRoot().getRight().getRight().getRight().getRight().getValue(), "e")
        self.assertEqual(tree.getRoot().getRight().getRight().getRight().getRight().getRight().getValue(), "f")
        self.assertEqual(tree.getRoot().getRight().getRight().getRight().getRight().getRight().getRight().getValue(), "g")

        tree.put(2,"z")
        self.assertEqual(tree.getRoot().getRight().getValue(), "z")
        self.assertEqual(tree.getRoot().getRight().getRight().getValue(), "c")


    def testPutLeft(self):
        tree = BST()
        tree.put(7,"a")
        tree.put(6,"b")
        tree.put(5,"c")
        tree.put(4,"d")
        tree.put(3,"e")
        tree.put(2,"f")
        tree.put(1,"g")

        self.assertEqual(tree.getRoot().getValue(), "a")
        self.assertEqual(tree.getRoot().getLeft().getValue(), "b")
        self.assertEqual(tree.getRoot().getLeft().getLeft().getValue(), "c")
        self.assertEqual(tree.getRoot().getLeft().getLeft().getLeft().getValue(), "d")
        self.assertEqual(tree.getRoot().getLeft().getLeft().getLeft().getLeft().getValue(), "e")
        self.assertEqual(tree.getRoot().getLeft().getLeft().getLeft().getLeft().getLeft().getValue(), "f")
        self.assertEqual(tree.getRoot().getLeft().getLeft().getLeft().getLeft().getLeft().getLeft().getValue(), "g")

    def testPut(self):
        tree = BST()
        keys = [10,5,15,2,7,12,20]
        vals = ["a","b","c","d","e","f","g","h","i"]
        tree.makeBST(keys,vals)
        self.assertEqual(tree.getRoot().getKey(), 10)
        self.assertEqual(tree.getRoot().getLeft().getKey(), 5)
        self.assertEqual(tree.getRoot().getLeft().getLeft().getKey(), 2)
        self.assertEqual(tree.getRoot().getLeft().getRight().getKey(), 7)
        self.assertEqual(tree.getRoot().getRight().getKey(),15)
        self.assertEqual(tree.getRoot().getRight().getLeft().getKey(),12)
        self.assertEqual(tree.getRoot().getRight().getRight().getKey(),20)



    def testGet(self):
    	
        tree = BST()
        keys = [10,5,15,2,7,12,20]
        vals = ["a","b","c","d","e","f","g","h","i"]
        tree.makeBST(keys,vals)
        self.assertEqual(tree.get(5).getValue(),"b")
        self.assertEqual(tree.get(15).getValue(),"c")
        self.assertEqual(tree.get(2).getValue(),"d")
        self.assertEqual(tree.get(7).getValue(),"e")
        self.assertEqual(tree.get(12).getValue(),"f")
        self.assertEqual(tree.get(18),None)

        #self.assertEqual(tree.get(150).getValue(),"Ashbourne")
        #self.assertEqual(tree.getLowestCommonAncestor([137,163,213]).getKey(),200)


    def testPrintInOrder(self):
        keys = [10,5,15,2,7,12,20]
        vals = ["a","b","c","d","e","f","g","h","i"]
        tree = BST()
        self.assertEqual(tree.printInOrder(),"")
        tree.makeBST(keys,vals)
        expectedOutPut = "2 : d\n5 : b\n7 : e\n10 : a\n12 : f\n15 : c\n20 : g\n"
        self.assertEqual(tree.printInOrder(),expectedOutPut)


    def testFindMinNode(self):
        tree = BST()
        self.assertEqual(tree.findMinNode(),None)
        keys = [10,5,15,2,7,12,20]
        vals = ["a","b","c","d","e","f","g","h","i"]
        tree.makeBST(keys,vals)
        self.assertEqual(tree.findMinNode().getKey(),2)

        tree = BST()
        keys = [100,50,200,25,75,150,250,10,36,63,8,125,175,225,290,20,27,47,55,70,77,90,110,137,163,190,213,230,270,300]
        values = ["Newry","Azerbijan","Navan","Napoli","Japan","Ashbourne","Cyprus","New York City Baby","L.A.P.D","Bermud","Bali","Atlantis","Paris","Memphis","Florida","Summerhill","Castlebar",
        "London","Kent","Gloucester","Verona","Raheny","Vienna","Washington","Zanzibar","Crete","Panama","Miltown","Leopardstown","Cape town","Alkatraz","Diagon-alley","Jellystone Park","Rathoath"]
        tree.makeBST(keys,values)
        self.assertEqual(tree.findMinNode().getKey(),8)




if __name__ == '__main__':
    unittest.main()
