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

	start = 0
	end = len(aList) - 1

	for i, v in enumerate(aList):
		if  v > aList[i+1]:
			swapper(aList, i, i+1)
			print(i)
			print(v)
			print(aList[i+1])
		elif i < end:
			print(i)
			print(v)
			print(aList[i+1])

		print(aList)

	return aList





def main():
	
	aList= [5,1,73,4,0,2,1,3,8,73,4,6,3,9,3]
	bList = aList[:]
	print(aList)
	print(bList)
	aList = selection_sort(aList)
	print(aList)
	print("Error check with builtin sort:")
	bList.sort()
	if aList == bList:
		print("Match!")
	print(bList)

	print("Before Bubble:")
	aList = [5,1,8,4,0,2,1,3,8,73,4,6,3,0,3]
	print(aList)

	print("During bubble")
	aList = bubble_sort(aList)
	print("After bubble:")
	print(aList)
main()