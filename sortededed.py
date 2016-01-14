

def swap_smallest(listIn, LastStartPosition): #takes a postion in a list and swaps it with the smallest element beyond that position
	



#	listOut =[]
#	equals = True

	PositionWhereSmallestFound = LastStartPosition
	count = 0
	x = listIn[count]

#################Find Smallest in list
	print (listIn)
	for i, v in enumerate(listIn[LastStartPosition:]):
		if v < x:
			x = v
			print("index:")
			PositionWhereSmallestFound = i
	
################
################SWAP

	temp = listIn[LastStartPosition+1]
	listIn[LastStartPosition+1] = listIn[PositionWhereSmallestFound]
	listIn[PositionWhereSmallestFound] = temp



	print("Smallest:")
	print(x)
	
	#print(count)
	return listIn

def selection_sort(listIn):

	listLen = len(listIn)
	LastStartPosition = 0
	#################LOOP THROUGH THE WHOLE LIST WITH SWAP SMALLEST
	while LastStartPosition < listLen -1:
		listIn = swap_smallest(listIn, LastStartPosition-1)
		LastStartPosition += 1
	return listIn

def main():
	list1 = [488, 22, 9, 10, 78, 9, 4, 55, 33, 66, 3, 5]
	print(list1)
	#list1 = selection_sort(list1)
	#print(swap_smallest(list1, -1))
	print(selection_sort(list1))

main()


