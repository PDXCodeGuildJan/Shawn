__author__ = "Shawn Waldow"

"""
##################################################################
# WRITTING SORTING ALGORITHMS TO PRACTICE LOOPS, LISTS, RECURSION
##################################################################
"""

#############################################
# SWAPPER
#############################################

def swapper(aList, x, y):
	
	temp = aList[x]
	aList[x] = aList[y]
	aList[y] = temp
	return aList


#############################################
#SELECTION SORT
#############################################
def selection_sort(aList):

	#############################	
	#FIND the start of the list

	zeroPoint = 0
	end = len(aList)-1
	smallest = 0
	
	while zeroPoint < end:
		#############################################
		#FIND SMALLEST in list from zeropoint to end
		smallestSoFar = int(aList[zeroPoint])
		for i, v in enumerate(aList[zeroPoint:]):
				if v < smallestSoFar:
					smallest = i + zeroPoint
					smallestSoFar = int(v)

		#####################################
		#SWAP the smallest with the zeropoint
		swapper(aList, zeroPoint, smallest)
		
		#############################
		#INCREMENT zeropoint
		zeroPoint += 1

	############################
	# REPEAT until unsorted list is empty
	
	return aList



###########################################
# BUBBLE SORT
###########################################

def bubble_sort(aList):

	"""
	START AT THE BEGINING of aList
	INTIALIZED CURRENT END OF UNSORTED (begins as the end of the full list)
	
	LOOP UNTIL CURRENT END == BEGINING

		COMPARE EVERY ADJACENT PAIR to the right LOOP TO CURRENT END OF UNSORTED

			SWAP LARGER TO RIGHT

		DECREMENT CURRENT END OF UNSORTED
	"""

	#START AT THE BEGINING of aList
	start = 0	
	
	#INTIALIZED CURRENT END OF UNSORTED (begins as the end of the full list)
	end = len(aList) - 1

	#LOOP UNTIL CURRENT END == BEGINING	
	while end != start:
		
		#COMPARE EVERY ADJACENT PAIR to the right LOOP TO CURRENT END OF UNSORTED
		i = 0
		while i != end:

			if aList[i] > aList[i+1]:
				#SWAP LARGER TO RIGHT
				swapper(aList, i, i+1)
				i += 1

	
			else:
				i += 1

		#DECREMENT CURRENT END OF UNSORTED
		end -= 1

	
	return aList



###########################################
# INSERTION SORT
###########################################

def insertion_sort(aList):

	"""
	CONSIDER THE FIRST ELEMENT IN A LIST AS A CONCEPTUALLY SEPARATE LIST WHICH IS SORTED
		
		LOOP UNTIL THE LIST SORTED LENGTH IS AS LONG AS THE WHOLE LIST

			LOOK AT THE NEXT VALUE UP FROM THIS 'sorted' LIST AND THEN THERE ARE TWO CASES:
			IF IT IS LARGER THAN THE NEXT SORTED ELEMENT THEN INCREMENT THE 'size'
			OF THE SORTED LIST. EXIT THE LOOP

			OTHERWISE KEEP LOOPING COMPARE DOWN THE SORTED LIST UNITL WE WE FIND ONE SMALLER 
			THEN pop AND insert to the left

		INCREMENT THE LIST SORTED LENGTH

	"""
################OR DO WE???#############################################
	"""
	CONSIDER THE FIRST ELEMENT IN A LIST AS A CONCEPTUALLY SEPARATE LIST WHICH IS SORTED
		
		LOOP UNTIL THE LIST SORTED LENGTH IS AS LONG AS THE WHOLE LIST

			LOOK AT THE 'NEXT VALUE UP' FROM THIS 'sorted' LIST.

				IF 'THE NEXT VALUE UP' IS BIGGER THAN 'THE NEXT VALUE DOWN' THE SORTED LIST THEN EXIT THIS LOOPP

				ELSE SWAP 'NEXT VALUE UP' WITH 'THE NEXT VALUE DOWN' THE SORTED LIST

		INCREMENT THE LIST SORTED LENGTH

	"""
	unsorted = 1
	end = len(aList)

	while unsorted < end:

		next_value_down = unsorted - 1

		if int(aList[unsorted]) >= int(aList[next_value_down]):
				
			next_value_down = -1

		while next_value_down >= 0:


			if int(aList[unsorted]) < int(aList[next_value_down]):
				
				if next_value_down == 0:

					temp = aList.pop(unsorted)
					aList.insert(next_value_down, temp)
					next_value_down = -1


			elif int(aList[unsorted]) >= int(aList[next_value_down]):

				temp = aList.pop(unsorted)
				aList.insert(next_value_down + 1, temp)
				next_value_down = -1

			else:

				print ("Error")


			next_value_down -= 1

		unsorted += 1

	return aList

	
##################################
# SHELL SORT
def shell_sort():
	pass


##################################
# Merge Sort
##################################
def merge_sort(a_list):
	""" Split the list up into two halfs. Recurse merge_sort on the resulting two lists until each list is length 1. 
	Merge the returning values into order. """
	length = len(a_list)
	mid = length // 2
	print("List, length, mid", a_list, length, mid)
	if length > 1:
		left = merge_sort(a_list[:mid])
		right =  merge_sort(a_list[mid:])
		print(left,right)
		return merge(left, right)
	
	else:
		
		return a_list

#################################
# Merge
#################################
def merge(left_list, right_list):
	"""Merges two sorted lists of arbitary length by comparing start values."""
	
	returning_into_list = []
	start_left, start_right, start_into = 0,0,0
	end_left, end_right = len(left_list), len(right_list)

	while start_left < end_left and start_right < end_right:

		if left_list[start_left] < right_list[start_right]:
			returning_into_list.append(left_list[start_left])
			start_left += 1

		else:
			returning_into_list.append(right_list[start_right])
			start_right += 1

	while start_left < end_left:
		returning_into_list.append(left_list[start_left])
		start_left += 1

	while start_right < end_right:
		returning_into_list.append(right_list[start_right])
		start_right += 1

	return returning_into_list

def main():
	
	alist = [1,4,9]
	blist = [2,6,8,10]

	print(merge_sort([2,4,1,2,6,4,7,8,9,4,3]))

	# random_with_repeats = [9,8,7,6,5,45,4,66,7,4,1,4,3,2,1] 
	# python_sorted = random_with_repeats[:]

	# print("Before: ", random_with_repeats)

	# random_with_repeats = insertion_sort(random_with_repeats)
	
	# print("After insert: ", random_with_repeats)

	# print("Before: ", python_sorted)

	# python_sorted.sort()
	
	# print("After insert: ", python_sorted)

	# print("insert sorted == python sorted? ", python_sorted == random_with_repeats)




	# random_with_repeats = [2,2,3,1,2,1,2,2,2,2,3,1,1,1,1,2] 
	# python_sorted = random_with_repeats[:]

	# print("Before: ", random_with_repeats)

	# random_with_repeats = insertion_sort(random_with_repeats)
	
	# print("After insert: ", random_with_repeats)

	# print("Before: ", python_sorted)

	# python_sorted.sort()
	
	# print("After insert: ", python_sorted)

	# print("insert sorted == python sorted? ", python_sorted == random_with_repeats)




	# random_with_repeats = [10,11,12,13,14,15,16,17,18,19,20] 
	# python_sorted = random_with_repeats[:]

	# print("Before: ", random_with_repeats)

	# random_with_repeats = insertion_sort(random_with_repeats)
	
	# print("After insert: ", random_with_repeats)

	# print("Before: ", python_sorted)

	# python_sorted.sort()
	
	# print("After insert: ", python_sorted)

	# print("insert sorted == python sorted? ", python_sorted == random_with_repeats)




	# random_with_repeats = [99,98,97,96,95,94,93,92,91,90,89,88,87] 
	# python_sorted = random_with_repeats[:]

	# print("Before: ", random_with_repeats)

	# random_with_repeats = insertion_sort(random_with_repeats)
	
	# print("After insert: ", random_with_repeats)

	# print("Before: ", python_sorted)

	# python_sorted.sort()
	
	# print("After insert: ", python_sorted)

	# print("insert sorted == python sorted? ", python_sorted == random_with_repeats)








if __name__ == "__main__":
	main()