from graph_lowestCommonAncestor import Node
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

	


my_list = BST();
my_list.put(9,"Conor") 
my_list.put(12,"Kate") 
my_list.put(10,"James") 
my_list.put(7,"Fearghal") 
my_list.printInOrder()