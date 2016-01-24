__author__ = "Shawn Waldow"

"""
A conceptual implementation of the classic recurssion puzzle "Towers of Hanoi"
We shall represent the disks with integers greater than 0. The larger the int 
the larger the disk.

The pegs shall be lists.

We must never stack a larger plate on top of a smaller one.

Given a stack on the left "A" using the midpoint stack "B" move all the disks to "C".

Print each stack at each step and test it for orderlyness to make sure we have not
made an illegal move.

Track number of moves and compare it to the begining number of disks.

"""

# Remove the last value of a list and return it
def pop_top(list1):
	length = len(list1)
	val = list1.pop(length-1)
	return val



# Extend the list from the end with value
def push_top(list1, val):
	length = len(list1)
	list1.insert(length,  val)




# Move the "top" value of a tower to the destination tower IFF the plate size rules of towers of hanoi aren't violated.
def tower_to_tower(source_tower, destination_tower):
	
	temp = pop_top(source_tower)
	
	# Always ok to move into an empty list
	if len(destination_tower) < 1:
		push_top(destination_tower, temp)

	# If the list isn't empty make sure the top plate isn't small than the one we are putting there.
	elif temp < destination_tower[-1]:
		push_top(destination_tower, temp)

	else:
		print("Can't stack a big plate atop a smaller plate.")
		exit()


# Lengthy function to print the towers in order no matter how they are passed into this print function.
# Takes three lists plus a dictionary that lets us assign a name, A, B, C, according to actual adress in memory.
# Makes use of standard Python 3 function id() which returns the memory location we want.
def display_towers(tower1,tower2,tower3, tower_dict):
	print("\n")
	
	# Arguments in A, B, C print A, B, C
	if tower_dict[hex(id(tower1))] == "A" and tower_dict[hex(id(tower2))] == "B" and tower_dict[hex(id(tower3))] =="C":
		print(tower_dict[hex(id(tower1))], tower1)
		print(tower_dict[hex(id(tower2))], tower2)
		print(tower_dict[hex(id(tower3))], tower3)

	# Arguments in B, A, C print A, B, C
	elif tower_dict[hex(id(tower1))] == "B" and tower_dict[hex(id(tower2))] == "A" and tower_dict[hex(id(tower3))] =="C":
		print(tower_dict[hex(id(tower2))], tower2)
		print(tower_dict[hex(id(tower1))], tower1)
		print(tower_dict[hex(id(tower3))], tower3)

	# Arguments in C, A, B print A, B, C
	elif tower_dict[hex(id(tower1))] == "C" and tower_dict[hex(id(tower2))] == "A" and tower_dict[hex(id(tower3))] =="B":
		print(tower_dict[hex(id(tower2))], tower2)
		print(tower_dict[hex(id(tower3))], tower3)
		print(tower_dict[hex(id(tower1))], tower1)

	# Arguments in A, C, B print A, B, C
	elif tower_dict[hex(id(tower1))] == "A" and tower_dict[hex(id(tower2))] == "C" and tower_dict[hex(id(tower3))] =="B":
		print(tower_dict[hex(id(tower1))], tower1)
		print(tower_dict[hex(id(tower3))], tower3)
		print(tower_dict[hex(id(tower2))], tower2)

	# Arguments in B, C, A print A, B, C
	elif tower_dict[hex(id(tower1))] == "B" and tower_dict[hex(id(tower2))] == "C" and tower_dict[hex(id(tower3))] =="A":
		print(tower_dict[hex(id(tower3))], tower3)
		print(tower_dict[hex(id(tower1))], tower1)
		print(tower_dict[hex(id(tower2))], tower2)

	# Arguments in C, B, A print A, B, C
	elif tower_dict[hex(id(tower1))] == "C" and tower_dict[hex(id(tower2))] == "B" and tower_dict[hex(id(tower3))] =="A":
		print(tower_dict[hex(id(tower3))], tower3)
		print(tower_dict[hex(id(tower2))], tower2)
		print(tower_dict[hex(id(tower1))], tower1)
	
	else:

		print("\n!!!!ERROR!!!!\n")





#Recursive solution to the towers of hanoi puzzle. Relies on divide and conquer plus tricky passing list names around. 
def hanoi(n, source_tower, dest_tower, spare_tower, tower_dict):
	"""
	1. Move all disks except the largest to tower b
	2. Move the largest disk from a to c
	3. Move all the disks except the largest (which is already on c) from b to c
	Based on pseudocode from https://www.cs.cmu.edu/~cburch/survey/recurse/hanoiimpl.html
	"""

	# Move largest disk to destination tower
	if n == 0:
		
		# Base Case
		tower_to_tower(source_tower, dest_tower)
		display_towers(source_tower, spare_tower, dest_tower, tower_dict)

	else:

		#  Move all disks except the largest to the spare tower
		hanoi(n-1, source_tower, spare_tower, dest_tower, tower_dict)
		display_towers(source_tower, spare_tower, dest_tower, tower_dict)


		# Move the largest disk to the destination tower
		tower_to_tower(source_tower, dest_tower)
		display_towers(source_tower, spare_tower, dest_tower, tower_dict)


		# Move all the remaining disks to the destination tower.		
		hanoi(n-1, spare_tower, dest_tower, source_tower, tower_dict)
		display_towers(source_tower, spare_tower, dest_tower, tower_dict)


	

def main():
	tower1 = [3,2,1]
	tower2 = []
	tower3 = []


	tower_dict = {hex(id(tower1)): "A", hex(id(tower2)): "B", hex(id(tower3)): "C"}


	#Hard coded solution to a 3 disk tower moving from tower1 to end destination tower2.
	#display_towers(tower1,tower2,tower3)
	
	tower_to_tower(tower1, tower3)
	
	display_towers(tower1, tower2, tower3, tower_dict)
	
	tower_to_tower(tower1, tower2)
	
	display_towers(tower1, tower2, tower3, tower_dict)
	
	tower_to_tower(tower3, tower2)
	
	display_towers(tower1, tower2, tower3, tower_dict)

	tower_to_tower(tower1, tower3)

	display_towers(tower1, tower2, tower3, tower_dict)

	tower_to_tower(tower2, tower1)

	display_towers(tower1, tower2, tower3, tower_dict)

	tower_to_tower(tower2, tower3)

	display_towers(tower1, tower2, tower3, tower_dict)

	tower_to_tower(tower1, tower3)

	display_towers(tower1, tower2, tower3, tower_dict)

	print("\n\n@@@@@@@@@@@@RESET AND RECURSE@@@@@@@@@@@@@@@@@\n\n")
	


	tower1 = [5,4,3,2,1]
	tower2 = []
	tower3 = []

	# Define a dictionary so we can track the three towers by memory location as they are passed around and aliased extensively in the recursive solution.
	tower_dict = {hex(id(tower1)): "A", hex(id(tower2)): "B", hex(id(tower3)): "C"}


	hanoi(int(len(tower1))-1, tower1, tower2, tower3, tower_dict)


main()

