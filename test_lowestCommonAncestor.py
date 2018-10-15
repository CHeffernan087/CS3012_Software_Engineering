from BST import BST
from Node import Node
from diGraphNode import diGraphNode
from diGraph import diGraph
import unittest

class TestStringMethods(unittest.TestCase):

    
    '''
        put => tested
        getRoot => tested
        get => tested
        printInOrder => tested 
        findMin => tested 
        getPathToNode => tested 
        getPathToNVertices => tested
        printVertexPath => tested
        getLowestCommonAncestor => 
        
    '''


    def testNodeCreation(self):
        #check node constructor is working okay
        testNode = Node("Conor",21)
        self.assertEqual(testNode.getKey(),"Conor")
        self.assertEqual(testNode.getValue(),21)
        self.assertEqual(testNode.toString(),"Conor : 21")




    def testPutRoot(self):
        #check if adding one node to the tree will in fact have the root pointer pointed to it
    	tree = BST()
    	tree.put(11,"Ashbourne")
        self.assertEqual(tree.getRoot().getKey(), 11)


    def testPutRight(self):
        #check the put to the right by making a linear tree to the right
        tree = BST()
        tree.put(1,"a")
        tree.put(2,"b")
        tree.put(3,"c")
        tree.put(4,"d")
        tree.put(5,"e")
        tree.put(6,"f")
        tree.put(7,"g")
        #check manually if all heys have been put in right place by manully traversinf left pointers
        self.assertEqual(tree.getRoot().getValue(), "a")
        self.assertEqual(tree.getRoot().getRight().getValue(), "b")
        self.assertEqual(tree.getRoot().getRight().getRight().getValue(), "c")
        self.assertEqual(tree.getRoot().getRight().getRight().getRight().getValue(), "d")
        self.assertEqual(tree.getRoot().getRight().getRight().getRight().getRight().getValue(), "e")
        self.assertEqual(tree.getRoot().getRight().getRight().getRight().getRight().getRight().getValue(), "f")
        self.assertEqual(tree.getRoot().getRight().getRight().getRight().getRight().getRight().getRight().getValue(), "g")
        #check if inserting a key again will update the associated value
        tree.put(2,"z")
        self.assertEqual(tree.getRoot().getRight().getValue(), "z")
        self.assertEqual(tree.getRoot().getRight().getRight().getValue(), "c")


    def testPutLeft(self):
        #check the put to the left by making a linear tree to the left
        tree = BST()
        tree.put(7,"a")
        tree.put(6,"b")
        tree.put(5,"c")
        tree.put(4,"d")
        tree.put(3,"e")
        tree.put(2,"f")
        tree.put(1,"g")
        #check manually if all heys have been put in right place by manully traversinf left pointers
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
        #function that calls put continually on  set of keys/vals
        tree.makeBST(keys,vals)
        #check manually if all heys have been put in right place by manully traversinf left/ right pointers
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
        #get vals for a number of keys we have just placed in the binary tree
        self.assertEqual(tree.get(5).getValue(),"b")
        self.assertEqual(tree.get(15).getValue(),"c")
        self.assertEqual(tree.get(2).getValue(),"d")
        self.assertEqual(tree.get(7).getValue(),"e")
        self.assertEqual(tree.get(12).getValue(),"f")
        #check if getting a value not in the tree returns none
        self.assertEqual(tree.get(18),None)



    def testPrintInOrder(self):
        keys = [10,5,15,2,7,12,20]
        vals = ["a","b","c","d","e","f","g","h","i"]
        #check that printing an empty tree just prints an empty string
        tree = BST()
        self.assertEqual(tree.printInOrder(),"")
        #check that printing balanced BST returns right result in right order
        tree.makeBST(keys,vals)
        expectedOutPut = "2 : d\n5 : b\n7 : e\n10 : a\n12 : f\n15 : c\n20 : g\n"
        self.assertEqual(tree.printInOrder(),expectedOutPut)


    def testFindMinNode(self):
        #check that min node of empty tree is None
        tree = BST()
        self.assertEqual(tree.findMinNode(),None)
        #check min of small balanced BST
        keys = [10,5,15,2,7,12,20]
        vals = ["a","b","c","d","e","f","g","h","i"]
        tree.makeBST(keys,vals)
        self.assertEqual(tree.findMinNode().getKey(),2)
        #check min node of non-balanced, large BST
        tree = BST()
        keys = [100,50,200,25,75,150,250,10,36,63,8,125,175,225,290,20,27,47,55,70,77,90,110,137,163,190,213,230,270,300]
        values = ["Newry","Azerbijan","Navan","Napoli","Japan","Ashbourne","Cyprus","New York City Baby","L.A.P.D","Bermuda","Bali","Atlantis","Paris","Memphis","Florida","Summerhill","Castlebar",
        "London","Kent","Gloucester","Verona","Raheny","Vienna","Washington","Zanzibar","Crete","Panama","Miltown","Leopardstown","Cape town","Alkatraz","Diagon-alley","Jellystone Park","Rathoath"]
        tree.makeBST(keys,values)
        self.assertEqual(tree.findMinNode().getKey(),8)

   

    def testGetPathToVertex(self):
        #test linear tree
        tree = BST();
        keys = [1,2,3,4,5,6,7,8]
        vals = ['a','b','c','d','e','f','g','h']
        tree.makeBST(keys,vals)
        pathToNode = tree.getPathToNode(5)
        self.assertEqual(pathToNode[0].getKey(),1)
        self.assertEqual(pathToNode[1].getKey(),2)
        self.assertEqual(pathToNode[2].getKey(),3)
        self.assertEqual(pathToNode[3].getKey(),4)
        self.assertEqual(pathToNode[4].getKey(),5)

        #test for node not in tree
        pathToNode = tree.getPathToNode(1000)
        self.assertEqual(pathToNode,None)

        #test balanced tree
        keys = [10,5,15,2,7,12,20]
        vals = ["a","b","c","d","e","f","g","h","i"]
        tree = BST()
        tree.makeBST(keys,vals)
        pathToNode = tree.getPathToNode(7)
        self.assertEqual(pathToNode[0].getKey(),10)
        self.assertEqual(pathToNode[1].getKey(),5)
        self.assertEqual(pathToNode[2].getKey(),7)

        #test large non-balanced BST
        tree = BST()
        keys = [100,50,200,25,75,150,250,10,36,63,8,125,175,225,290,20,27,47,55,70,77,90,110,137,163,190,213,230,270,300]
        values = ["Newry","Azerbijan","Navan","Napoli","Japan","Ashbourne","Cyprus","New York City Baby","L.A.P.D","Bermuda","Bali","Atlantis","Paris","Memphis","Florida","Summerhill","Castlebar",
        "London","Kent","Gloucester","Verona","Raheny","Vienna","Washington","Zanzibar","Crete","Panama","Miltown","Leopardstown","Cape town","Alkatraz","Diagon-alley","Jellystone Park","Rathoath"]
        tree.makeBST(keys,values)
        pathToNode = tree.getPathToNode(55)
        self.assertEqual(pathToNode[0].getKey(),100)
        self.assertEqual(pathToNode[1].getKey(),50)
        self.assertEqual(pathToNode[2].getKey(),75)
        self.assertEqual(pathToNode[3].getKey(),63)
        self.assertEqual(pathToNode[4].getKey(),55)

    def testGetPathOfNVertices(self):

        #test balanced tree
        keys = [10,5,15,2,7,12,20]
        vals = ["a","b","c","d","e","f","g","h","i"]
        tree = BST()
        tree.makeBST(keys,vals)
        paths = tree.getPathsOfNVertices([7,15,12,390])
        #check that indeed four paths were returned by function
        self.assertEqual(len(paths),4)
        #check that first path is a path to 7
        self.assertEqual(paths[0][0].getKey(),10)
        self.assertEqual(paths[0][1].getKey(),5)
        self.assertEqual(paths[0][2].getKey(),7)
        #check that second path is a path to 15
        self.assertEqual(paths[1][0].getKey(),10)
        self.assertEqual(paths[1][1].getKey(),15)
        #check that third path is a path to 12
        self.assertEqual(paths[2][0].getKey(),10)
        self.assertEqual(paths[2][1].getKey(),15)
        self.assertEqual(paths[2][2].getKey(),12)
        #check that fourth path is null as the node wasnt in the tree
        self.assertEqual(paths[3],None)

    def testLowestCommonAncestor(self):
        tree = BST()
        keys = [100,50,200,25,75,150,250,10,36,63,8,125,175,225,290,20,27,47,55,70,77,90,110,137,163,190,213,230,270,300]
        values = ["Newry","Azerbijan","Navan","Napoli","Japan","Ashbourne","Cyprus","New York City Baby","L.A.P.D","Bermuda","Bali","Atlantis","Paris","Memphis","Florida","Summerhill","Castlebar",
        "London","Kent","Gloucester","Verona","Raheny","Vienna","Washington","Zanzibar","Crete","Panama","Miltown","Leopardstown","Cape town","Alkatraz","Diagon-alley","Jellystone Park","Rathoath"]
        tree.makeBST(keys,values)
        #check edge case that None is returned when one or more nodes arent in the tree
        self.assertEqual(tree.getLowestCommonAncestor([1,2,3]),None)
        #check four instances where all Nodes are in the tree, insure the correct Lowest Common Ancestor is returned 
        self.assertEqual(tree.getLowestCommonAncestor([8,20,300]).getKey(),100)
        self.assertEqual(tree.getLowestCommonAncestor([55,70,90]).getKey(),75)
        self.assertEqual(tree.getLowestCommonAncestor([213,190,110]).getKey(),200)
        self.assertEqual(tree.getLowestCommonAncestor([163,190,110]).getKey(),150)


    def testdiGraphNodeCreation(self):
        node = diGraphNode(4,"Conor")
        self.assertEqual(node.getVal(),"Conor")
        self.assertEqual(node.getKey(),4)
    
    def testAddNodeToBag(self):
        tree = diGraph()
        node = diGraphNode(10,"Conor")
        tree.addNodeToBag(node)
        self.assertEqual(tree.nodesToString(),"10 : Conor")
        node2 = diGraphNode(20,"Ruan")
        tree.addNodeToBag(node2)
        self.assertEqual(tree.nodesToString(),"10 : Conor,20 : Ruan")
        node3 = diGraphNode(30,"Cuan")
        tree.addNodeToBag(node3)
        self.assertEqual(tree.nodesToString(),"10 : Conor,20 : Ruan,30 : Cuan")

    def testAddEdge(self):
        testTree = diGraph()
        node = diGraphNode(10,"Conor")
        testTree .addNodeToBag(node)
        node2 = diGraphNode(20,"Ruan")
        testTree .addNodeToBag(node2)
        testTree .addEdge(node,node2)
        self.assertEqual(node.hasEdgeTo(node2.getKey()),True)
        self.assertEqual(node2.hasEdgeTo(node.getKey()),False)


    def testExistsPathBetween(self):
        keySet = [1,2,3,4,5,6,7,8,9,10]
        valSet = ["a","b","c","d","e","f","g","h","i","j"]
        tree = diGraph()
        print("Set Of Nodes In Order  :\n")
        tree.addMultipleNodes(keySet,valSet)
        print(tree.nodesToString())
        edgeSet= [[1,5],[1,6],[1,2],[2,10],[3,2],[3,10],[3,9],[3,4],[3,7],[4,7],[5,3],[5,6],[7,8]]
        tree.addMultipleEdges(edgeSet)
        self.assertEqual(tree.existsPathFromTo(1,5),True)
        self.assertEqual(tree.existsPathFromTo(1,10),True)
        self.assertEqual(tree.existsPathFromTo(1,9),True)
        self.assertEqual(tree.existsPathFromTo(1,9),True)
        self.assertEqual(tree.existsPathFromTo(2,3),False)
        self.assertEqual(tree.existsPathFromTo(2,11),False)
        self.assertEqual(tree.existsPathFromTo(11,2),False)
        self.assertEqual(tree.existsPathFromTo(4,8),True)

        



if __name__ == '__main__':
    unittest.main()
