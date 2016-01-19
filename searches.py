"""SEARCH FUNCTIONS INCLUDING BINARY"""

from sort import bubble_sort

def main():

	# Make a list to look for the target value in.
	unsorted_list = ["E", "Z", "L", "O", "B", "F"]
	target_value = "B"

	sorted_list, target_index = binary_search(unsorted_list, target_value)

	#Print our solutions
	print("I found ", target_value, "It's at: ", target_index)
	binary_search(unsorted_list, "B")



def binary_search(the_list, target_value):
	"""Implements binary search algorithm."""

	sorted_list = bubble_sort(the_list)
	

	#IF we can't find the index, return  -1
	return (sorted_list, -1)
	

if __name__ == "__main__":
	main()