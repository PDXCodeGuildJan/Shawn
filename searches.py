"""SEARCH FUNCTIONS INCLUDING BINARY"""

from sort import bubble_sort

def main():

	# Make a list to look for the target value in.
	unsorted_list = ["E", "Z", "L", "O", "B", "F"]
	target_value = "F"

	sorted_list, target_index = binary_search(unsorted_list, target_value)

	#Print our solutions
	print(sorted_list)
	print("I found ", target_value, "It's at: ", target_index)
	binary_search(unsorted_list, "B")



def binary_search(the_list, target_value):
	"""Implements binary search algorithm."""

	#Sort the list
	sorted_list = bubble_sort(the_list)
	
	# Search the target value
	
	# Find length of current segment, 
	length = len(sorted_list)

	# Initialize start and end vars
	start = 0
	end = length


	# If len >= 1, look for target
	while length >= 1:

		#Find mid point of the segment 
		mid = start + (length // 2)

		# Determine if the middle value is greater or less than, or equal,
		#If equal, we've found it return middle
		if sorted_list[mid] == target_value:
			return(sorted_list, mid)

		#If greater, reduce the segment to the left half, repeat loop
		elif sorted_list[mid] > target_value:
			length = len(sorted_list[start:mid])
			end = mid

		#If less, reduce the segment to the right half, repeat loop
		elif sorted_list[mid] < target_value:
			start = mid + 1

		# Reeval length before loop runs
		length = len(sorted_list[start:end])

	#IF we can't find the index, return  -1
	return (sorted_list, -1)
	

if __name__ == "__main__":
	main()