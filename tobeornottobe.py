#practice calling functions by returned function name

import os
def the_called():
	print("or not to be?")

def the_caller():
	print("To be,")
	return the_called

def main():
	the_holder = the_caller()
	the_holder()

	beep = lambda x: os.system("echo -n '\a';sleep .2;" * x)
	beep(3)


	
	
main()