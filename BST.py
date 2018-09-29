from Node import Node
class BST:
	root = None
	

	def put_recursive(self,n, key, val):

		if(n.getKey() > key):
			if(n.left==None):
				n.left = Node(key,val)
			else:
				self.put_recursive(n.left,key,val)
		elif(n.getKey() < key):
			if(n.right==None):
				n.right = Node(key,val)
			else:
				self.put_recursive(n.right,key,val)
		else:
			n.val = val


	def put(self,key, value):
		if(self.root== None):
			self.root = Node(key,value)
			self.left=None
			self.right = None

		else:
			self.put_recursive(self.root,key,value)



	def printInOrder(self):
		if(self.root!=None):
			self.printInOrderRecursive(self.root)
			
	def printInOrderRecursive(self,n):

		if(n==None):
			return
		self.printInOrderRecursive(n.left)
		n.printNode()
		self.printInOrderRecursive(n.right)


	def findLeftMostBranch(self,n):
		if(n.left == None):
			return n
		findLeftMostBranch(n.left)

	def getRoot(self):
		return self.root


	def get(self, key):
		return self.get_recursive(self.root,key)

	def get_recursive(self, n,key):
		if(n==None):
			return 

		if(key <n.key):
			return self.get_recursive(n.left,key)
		elif(key > n.key):
			return self.get_recursive(n.right,key)	
		else:
			return n

	def getPathToNode(self, key):
		array = []
		self.recursiveGetPath(self.root,key,array)
		return array

	def recursiveGetPath(self, n, key, array):
		if(n==None):
			return 
		array.append(n)
		if(key <n.key):
			return self.recursiveGetPath(n.left,key,array)
		elif(key > n.key):
			return self.recursiveGetPath(n.right,key,array)	
		else:
			return n

	def getPathsOfNVertices(self,array):
		allPaths = []
		for key in array:
			path = self.getPathToNode(key)
			if(path==None):
				return None
			allPaths.insert(0,path)
		return allPaths


	def printVertexPath(self,array):
			for n in array:
				n.printNode()

	def getLowestCommonAncestor(self,array):
		allPaths = self.getPathsOfNVertices(array)
		previousNode = None
		n = allPaths[0][0]
		i=0
		
		while i<len(allPaths[0]):

			for pathList in allPaths:
				if(pathList[i]!= n):
					return previousNode
			previousNode = n
			i = i+1
			n = allPaths[0][i]
			
		return n;



	def makeBST(self,emptyBST,keys,vals):
		i = 0;
    	for key in keys:
    		emptyBST.put(key,values[i])
    		i = i+1

			






	


