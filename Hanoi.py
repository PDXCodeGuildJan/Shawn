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

def pop_top(list1):
	length = len(list1)
	val = list1.pop(length-1)
	return val

def push_top(list1, val):
	length = len(list1)
	list1.insert(length,  val)

def tower_to_tower(source_tower, destination_tower):
	
	temp = pop_top(source_tower)
	
	if len(destination_tower) < 1:
		push_top(destination_tower, temp)
	elif temp < destination_tower[-1]:
		push_top(destination_tower, temp)
	else:
		print("Can't stack a big plate atop a smaller plate.")
		exit()

def display_towers(tower1,tower2,tower3):
	print(tower1)
	print(tower2)
	print(tower3, "\n\n")



def main():
	tower1 = [3,2,1]
	tower2 = []
	tower3 = []

#Hard coded solution to a 3 disk tower moving from tower1 to end destination tower2.
	display_towers(tower1,tower2,tower3)
	
	tower_to_tower(tower1, tower3)
	
	display_towers(tower1,tower2,tower3)
	
	tower_to_tower(tower1, tower2)
	
	display_towers(tower1,tower2,tower3)
	
	tower_to_tower(tower3, tower2)
	
	display_towers(tower1,tower2,tower3)

	tower_to_tower(tower1, tower3)

	display_towers(tower1,tower2,tower3)
	
	tower_to_tower(tower2, tower1)

	display_towers(tower1,tower2,tower3)

	tower_to_tower(tower2, tower3)

	display_towers(tower1,tower2,tower3)

	tower_to_tower(tower1, tower3)

	display_towers(tower1,tower2,tower3)

	tower1 = [3,2,1]
	tower2 = []
	tower3 = []


main()

