class Node:
	"""	Define a single node that holds a value and that can point to another 
		node."""
	
	def __init__(self):
		self.value = None
		self.next_node = None


class LinkedList:

	def __str__(self):
		"""	Traverses a linked list and makes a string out of the values in each
			node."""
		
		a_string = str(self.head.value)
		
		#Get ready to traverse the list while we have a non-empty next node
		current_node = self.head.next_node
		while current_node:

			a_string = a_string + str(current_node.value)
			#Move the pointer ahead
			current_node = current_node.next_node

		return a_string

	def __init__(self):

		self.head = Node()

	def search(self, a_value):
		""" Return the first node in the list with a_value."""
		
		#Base case is the value in the head?
		if self.head.value == a_value:
			return self.head

		#Get ready to traverse the list & return the first node with the value.
		examined_node = self.head.next_node
		while examined_node:

			if examined_node.value == a_value:
				
				return examined_node

			else: 
				#We didn't find the value so move on to next pointer
				examined_node = examined_node.next_node

		#We didn't find the value anywhere. So return none.
		return None

	def add(self, a_value):
		
		# If the head has a value move on
		if self.head.value:

			# If even though the head has a value but no other nodes
			if self.head.next_node == None:
				
				# Make a new node to put the value in.
				self.head.next_node = Node()
				self.head.next_node.value = a_value

		
			#The head has a value and it points to other non-empty nodes.
			else:
				
				#Begin looping through the linked list to the end
				examined_node = self.head.next_node
				while examined_node.next_node != None:
					#Move the pointer to the next node.
					examined_node = examined_node.next_node

				#Make a new node at the end
				examined_node.next_node = Node() 
				examined_node.next_node.value = a_value
		else:
			# The head didn't have a value yet so it gets the value.
			self.head.value = a_value	
			 


def remove(self, a_value):
		pass


def main():

	y = LinkedList()
	y.add('a')
	y.add('b')
	y.add('c')
	print(y.head.value)
	print(y)


main()