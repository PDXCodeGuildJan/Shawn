##########################
#Let's experiment with string slicing!

a_string = "123456789"

def first(a_string):

	print("String: " + a_string)
	print("2nd char: "+a_string[1])
	print("3rd to last: "+a_string[-3])
	####SLICE
	print("Middle 3: "+a_string[3:6])

#print(a_string[(len(a_string)/2 - 2) : (len(a_string)/2 +1)])

def middle_chars(a_string):
	string_len = len(a_string)
	start_of_middle_triple = string_len // 2 - 1		####IT IS VERY NECESARRY TO USE INTEGER DIVISION WHEN DEALING WITH LISTS, STRINGS (ie arrays)
	end_of_middle_triple = string_len // 2 + 2
	print("String length:" + str(string_len))
	####SLICE
	print("Middle 3 by integer math:" + str(a_string[start_of_middle_triple:end_of_middle_triple]))



def loop_sequence(a_string):
	print(a_string)										
	for x in a_string:
		print(x)										###SO SiMPLE SO DIFFERENT FROM C!!!!!!!!!!!!

def main(a_string):
	first(a_string)
	middle_chars(a_string)
	a_string = input("Give me another string> ")
	middle_chars(a_string)
	a_string = input("OK give me a sequence> ")
	loop_sequence(a_string)

main(a_string)
	