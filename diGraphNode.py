

class diGraphNode :
	
	nodesPointedTo = []
	key = 0
	value = ""

	def __init__(self,key,value):
		self.key = key
		self.value = value

	def pointToNewNode(self,newNode):
		nodesPointedTo.append(pointToNewNode)

	def traverseNodes(self):
		for node in nodesPointedTo:
			print(node.getKey)

	def getKey(self):
		return self.key

	def getVal(self):
		return self.value

	def printAdjacentNodes(self):
		for node in nodesPointedTo:
			print node.getKey
	
	def existsPathTo(self,key):
		if(self.getKey==key):
			return True
		for node in nodesPointedTo:
			if(node.existsPathTo(key)==True):
				return True
		return False
