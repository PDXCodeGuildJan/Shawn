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

def main():
	tower1 = [1,2,3]
	tower2 = []
	tower3 = []

	top = len(tower1)

	print(tower1)
	print(tower2)
	print(tower3, "\n\n")

	tower2.insert(top,tower1.pop(top))
	
	print(tower1)
	print(tower2)
	print(tower3, "\n\n")


	tower2.insert(top,tower1.pop(top))

	print(tower1)
	print(tower2)
	print(tower3, "\n\n")


main()

