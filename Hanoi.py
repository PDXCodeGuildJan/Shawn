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

def main():
	tower1 = [3,2,1]
	tower2 = []
	tower3 = []

#Hard coded solution to a 3 disk tower
	print(tower1)
	print(tower2)
	print(tower3, "\n\n")

	push_top(tower2, pop_top(tower1))
	
	print(tower1)
	print(tower2)
	print(tower3, "\n\n")


	push_top(tower3, pop_top(tower1))

	print(tower1)
	print(tower2)
	print(tower3, "\n\n")

	push_top(tower3, pop_top(tower2))

	print(tower1)
	print(tower2)
	print(tower3, "\n\n")

	push_top(tower2, pop_top(tower1))

	print(tower1)
	print(tower2)
	print(tower3, "\n\n")

	push_top(tower1, pop_top(tower3))

	print(tower1)
	print(tower2)
	print(tower3, "\n\n")

	push_top(tower2, pop_top(tower3))

	print(tower1)
	print(tower2)
	print(tower3, "\n\n")

	push_top(tower2, pop_top(tower1))

	print(tower1)
	print(tower2)
	print(tower3, "\n\n")

main()

