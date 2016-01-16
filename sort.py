########################################################
# WRITTING SORTING ALGORITHMS TO PRACTICE LOOPS N LISTS
########################################################


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

			if int(aList[i]) > int(aList[i+1]):
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
	end = len(aList)-1

	while unsorted != end:

		next_value_down = unsorted - 1

		while next_value_down != -1:
		
			if aList[unsorted] > aList[next_value_down]:
				
				next_value_down = -1

			elif aList[unsorted] < aList[next_value_down]:
				temp = aList.pop(unsorted)
				aList.insert(next_value_down-1, temp)
				next_value_down = -1
				

			else:
				next_value_down -= 1

		unsorted += 1

	return aList

	
#################################3
# SHELL SORT

def main():
	
	aList = [5,1]
	
	print(aList)

	print("During insert")
	aList = insertion_sort(aList)
	print("After insert:")
	print(aList)

main()