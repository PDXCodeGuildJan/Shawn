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
	print("It's a custom sized die---->" + str(roll))


def main():
	#Ask how many dice
	total_rolls = input("How many dice you rollin'? ")
	total_rolls = int(total_rolls)

	#How big the die
	max_num = input("How many sides per dice? ")
	max_num = int(max_num)

	#Roll that many dice
	for something in range(1, total_rolls+1):
		custom_die(1, max_num)

main()