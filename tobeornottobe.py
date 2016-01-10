#practice calling functions by returned function name

def the_called():
	print("or not to be?")

def the_caller():
	print("To be,")
	return the_called

def main():
	the_holder = the_caller()
	the_holder()
main()