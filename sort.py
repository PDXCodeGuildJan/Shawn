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
	print (zeroPoint)
	end = len(aList)-1
	smallest = 0
	
	while zeroPoint < end:
		##############################
		#FIND SMALLEST in list from zeropoint to end
		smallestSoFar = int(aList[zeroPoint])
		for i, v in enumerate(aList[zeroPoint:]):
				if v < smallestSoFar:
					smallest = i + zeroPoint
					smallestSoFar = int(v)

		##############################
		#SWAP the smallest with the zeropoint
		swapper(aList, zeroPoint, smallest)
		print(aList)
		#############################
		#INCREMENT zeropoint
		zeroPoint += 1
		print(zeroPoint)

	##############
	#REPEAT until unsorted list is empty
	return aList



def main():
	
	aList= [5,5,73,4,0,2,1,3,8,73,4,6,3,9,3]
	bList = aList
	print(aList)
	aList = selection_sort(aList)
	print("Error check with builtin sort:")
	print(bList)




main()
