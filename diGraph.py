from diGraphNode import diGraphNode

class diGraph:
   
    bag = []

    def __init__(self):
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

    def addMultipleEdges(self, keys, vals):
        i = 0
        for key in keys:
            val = vals[i++]
            newNode = diGraphNode(key,val)
            self.addNodeToBag(node)

    def getNodeByKey(self,key):
        for node in self.bag:
            if node.key == key:
                return node
        return None

    def addEdgeByKey(self, k1,k2):
        node1 = self.getNodeByKey(k1)
        node2 = self.getNodeByKey(k2)
        if(node1!=None and node2!= None):
            self.addEdge(node1,node2)
    