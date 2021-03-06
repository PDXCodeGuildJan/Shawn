#Create a die function
#returning a random number.

from random import randint

#Random number between 1 & 6

def die():
	
	roll = randint(1, 6)
	print("It's a die---->" + str(roll))




# Custom sized die that takes a range

def custom_die(lower, upper):
	
	roll = randint(lower, upper)
	if roll == lower:
		print("It's a custom sized die---->" + str(roll) + " CRITICAL FAIL!!!")
	elif roll == upper:
		print("It's a custom sized die---->" + str(roll) + " CRITICAL HIT!!!")
	else:
		print("It's a custom sized die---->" + str(roll))


def main():
	print("Welcome to die roller. Enter q to exit")
	entree = ""

	#Wrap the core logic in a while loop
	#
	while entree != "q":
		#Ask how many dice
		entree = input("How many dice you rollin'? ")
		if entree.lower() == "q":						#input sanitized
			exit()
		total_rolls = int(entree)

		#How big the die
		entree = input("How many sides per dice? ")
		if entree.lower() == "q":						#input sanitized
			exit()

		max_num = int(entree)

		#Roll that many dice
		for something in range(1, total_rolls+1):
			custom_die(1, max_num)

main()