class Node:
	def __init__(self):
		self.value = 0
		self.next_node = None


class LinkedList:

	def __str__(self):

		a_string = str(self.head.value)
		current_node = self.head.next_node
		while current_node:

			a_string = a_string + str(current_node.value)
			current_node = current_node.next_node

		return a_string

	def __init__(self):

		self.head = Node()

	def search(self, a_value):
		
		if self.head.value == a_value:
			return self.head

		examined_node = self.head.next_node


		while examined_node:

			if examined_node.value == a_value:
				
				return examined_node

			else: 

				examined_node = examined_node.next_node

		return None

	def add(self, a_value):
		


		if self.head.next_node == None:
			
			self.head.next_node = Node()

			self.head.next_node.value = a_value

			print(a_value)
	
		else:
			
			examined_node = self.head.next_node

			while examined_node.next_node != None:

				examined_node = examined_node.next_node

			examined_node.next_node = Node() 
			examined_node.next_node.value = a_value


			 


def remove(self, a_value):
		pass


def main():

	y = LinkedList()
	y.add('a')
	print(y.head.next_node.value)
	y.add('b')
	print(y.head.next_node.value)
	y.add('c')
	print(y.head.next_node.value)
	print(y.search('a'),y.search('b'),y.search('c'),y.search('d'))
	print(y)

main()