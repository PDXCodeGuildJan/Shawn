#############################################
#SELECTION SORT
#############################################


#####################Swap one value in a list with another
def swapper(aList, zeroPoint, smallest):
	
	temp = aList[zeroPoint]
	aList[zeroPoint] = aList[smallest]
	aList[smallest] = temp
	return aList



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

	##############
	#REPEAT until unsorted list is empty
	return aList



def main():
	
	aList= [5,5,73,4,0,2,1,3,8,73,4,6,3,9,3]
	bList = aList
	print(aList)
	aList = selection_sort(aList)
	print(aList)
	print("Error check with builtin sort:")
	print(bList)
	if aList == bList:
		print("Match!")


	aList= [0]
	bList = aList
	print(aList)
	aList = selection_sort(aList)
	print(aList)
	print("Error check with builtin sort:")
	print(bList)
	if aList == bList:
		print("Match!")




	aList= [0,0,0,0,0,0,0,0,0,0,0,0]
	bList = aList
	print(aList)
	aList = selection_sort(aList)
	print(aList)
	print("Error check with builtin sort:")
	print(bList)
	if aList == bList:
		print("Match!")



	aList= [10,9,8,7,6,5,4,3,2,1]
	bList = aList
	print(aList)
	aList = selection_sort(aList)
	print(aList)
	print("Error check with builtin sort:")
	print(bList)
	if aList == bList:
		print("Match!")



	aList= [33,6666,3,64,66767,65,4664364,54,23,43]
	bList = aList
	print(aList)
	aList = selection_sort(aList)
	print(aList)
	print("Error check with builtin sort:")
	print(bList)
	if aList == bList:
		print("Match!")



main()
