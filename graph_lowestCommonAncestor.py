class Node:
  def __init__(self, key, value):
	self.key = key
	self.value = value
	
  def printNode(self):
	print(self.key+ " : "+ str(self.value))
		

node = Node("Conor",1)
node.printNode()


