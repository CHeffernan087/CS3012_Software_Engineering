from diGraphNode import diGraphNode

class diGraph:
   
    bag = []

    def __init__(self, bag = None):
		self.bag = []

    def nodesToString(self):
        strForm = ""
        for node in self.bag:
            
            strForm  = strForm + str(node.getKey())+" : "+ str(node.getVal()) + {True: ",", False: ""}[(node!=self.bag[len(self.bag)-1])]
        return strForm

    def addNodeToBag(self,newNode) :
        for node in self.bag:
            if node.getKey() == newNode.getKey():
                node.setVal(newNode.getVal())
                return
        self.bag.append(newNode)

    def addEdge(self,n1,n2):
        n1.pointToNewNode(n2)

    def getNode(self,key):
        for node in self.bag:
            if(node.getKey()==key):
                return node
        return None

    def addMultipleNodes(self, keys, vals):
        i = 0
        for key in keys:
            val = vals[i]
            i = i+1
            newNode = diGraphNode(key,val)
            self.addNodeToBag(newNode)

    def addMultipleEdges(self,edgeSet):
        for edge in edgeSet:
            self.addEdgeByKey(edge[0],edge[1])

    def getNodeByKey(self,key):
        for node in self.bag:
            if node.key == key:
                return node
        return None

    def addEdgeByKey(self, k1,k2):
        node1 = self.getNodeByKey(k1)
        node2 = self.getNodeByKey(k2)
        if(node1!=None and node2!= None and k1!=k2):
            self.addEdge(node1,node2)

    def existsPathFromTo(self,fromKey,toKey):
        node1 = self.getNodeByKey(fromKey)
        if(node1==None):
            return False
        return node1.existsPathTo(toKey)

    def asyclicInsertEdge(self,k1,k2):
        if(self.existsPathFromTo(k2,k1)==False ):
            self.addEdgeByKey(k1,k2)
            return
        return -1  

    def lowestCommonAncestorRecursive(self,node,k1,k2):
        for currentNode in node.nodesPointedTo:
            if(currentNode.getKey()!=k1 and currentNode.getKey()!=k2 and self.existsPathFromTo(currentNode.getKey(),k1) and self.existsPathFromTo(currentNode.getKey(),k2)):
                return self.lowestCommonAncestorRecursive(currentNode,k1,k2)
        return node

    def lowestCommonAncestor(self, root,k1,k2):
        rootNode = self.getNodeByKey(root)
        return self.lowestCommonAncestorRecursive(rootNode,k1,k2).getKey()
        
    