def swap(the_list, index_a, index_b):

	"""Swaps two items in a list."""
	the_list[index_a], the_list[index_b] = the_list[index_b], the_list[index_a]
	return the_list

def insertion_sort(the_list):
	 
	for start_index, value in enumerate(the_list):
		lost_index = start_index
		lost_value = value


	 	#Look for where lost index value belongs
		while (lost_value < the_list[lost_index - 1]
	 			and lost_index > 0):
	 		
	 		#swap lost value with adjacent index
	 		the_list = swap(the_list, lost_index, lost_index-1)

	 		#Decrement
	 		lost_index -= 1

	return the_list


def main():
	sorted_list = insertion_sort(["e","z","l","o","b","f"])
	print(sorted_list)

main()