

class diGraphNode :
	
	nodesPointedTo = []
	key = 0
	value = ""

	def __init__(self,key,value):
		self.key = key
		self.value = value

	def pointToNewNode(self,newNode):
		self.nodesPointedTo.append(newNode)

	def traverseNodes(self):
		for node in self.nodesPointedTo:
			print(node.getKey)

	def getKey(self):
		return self.key

	def getVal(self):
		return self.value

	def setVal(self,val):
		self.value = val

	def printAdjacentNodes(self):
		for node in self.nodesPointedTo:
			print node.getKey
	
	def existsPathTo(self,key):
		if(self.getKey==key):
			return True
		for node in self.nodesPointedTo:
			if(node.existsPathTo(key)==True):
				return True
		return False
	
	def hasEdgeTo(self, key):
		for node in self.nodesPointedTo:
			if(node.getKey()==key):
				return True;
		return False

	
