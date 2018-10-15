from diGraphNode import diGraphNode

class diGraph:
   
    bag = []

    def nodesToString(self):
        strForm = ""
        for node in self.bag:
            
            strForm  = strForm + str(node.getKey())+" : "+ str(node.getVal()) + {True: ",", False: ""}[(node!=self.bag[len(self.bag)-1])]
        return strForm

    def addNodeToBag(self,node) :
        self.bag.append(node)

    def addEdge(self,n1,n2):
        n1.pointToNewNode(n2)

