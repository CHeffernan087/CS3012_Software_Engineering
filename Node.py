
class Node:
	left = None
	right = None
  	def __init__(self, key, value):
		self.key = key
		self.value = value
	def printNode(self):
		print(str(self.key)+" : "+self.value)

	def getKey(self):
		return self.key


	def toString(self):
		return str(self.key)+" : "+str(self.value)

	def getValue(self):
		return self.value

	def getLeft(self):
		return self.left

	def getRight(self):
		return self.right