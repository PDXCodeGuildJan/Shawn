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
# Takes a single list of comparable values.
# Returns an ordered list.
##################################

def merge_sort(a_list):
	""" Split the list up into two halfs. Recurse merge_sort on the resulting two lists until each list is length 1. 
	Merge the returning values into order. """
	
	length = len(a_list)
	mid = length // 2	#Midpoint

	if length > 1:		#Keep splitting the list, unless it is down to one element lists.

		left = merge_sort(a_list[:mid])		#Recurse the left half.
		right =  merge_sort(a_list[mid:])	#Recurse the right half.

		return merge(left, right)	#Catched the sorted lists on their way back up.
	
	else:
		
		return a_list	#Return the one element list when we get down there. No need to sort since a 1 element list is already in order.

#################################
# Merge
# Takes two lists of arbitrary lengths comprised of ordered, comparable values as agruments.
# Returns a single merged list in order
#################################

def merge(left_list, right_list):
	"""Merges two sorted lists of arbitary length by comparing start values."""
	
	returning_into_list = [] #Init a list to merge into
	start_left, start_right, start_into = 0,0,0 #Init indexes to track the parts of the lists which are merged
	end_left, end_right = len(left_list), len(right_list)

	while start_left < end_left and start_right < end_right:	#Both lists still have values to compare

		if left_list[start_left] < right_list[start_right]:		#Left list has next smallest value to merge
	
			returning_into_list.append(left_list[start_left])	
			start_left += 1			

		else:
	
			returning_into_list.append(right_list[start_right])	#Right list has next smallest value to merge
			start_right += 1

	

	#One of the two lists has been exhasted of values to merge

	while start_left < end_left:	#The left half has a value to merge
	
		returning_into_list.append(left_list[start_left])
		start_left += 1

	while start_right < end_right:	#The right half has a value to merge
	
		returning_into_list.append(right_list[start_right])
		start_right += 1

	return returning_into_list	#Return the merged list ordered back out!


def main():
	

	alist = [2,4,1,2,6,33,244,500,500,4,7,8,9,4,3]
	blist = [2,4,1,2,6,33,244,500,500,4,7,8,9,4,3]	#To test

	blist.sort() #To test
	print(merge_sort(alist))
	print(blist)









if __name__ == "__main__":
	main()