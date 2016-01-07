#Create a die function
#returning a random number.

from random import randint

def die():
	
	roll = randint(1, 6)
	print("It's a die---->" + str(roll))


die()

# Custom sized die that takes a range

def custom_die(lower, upper):
	
	roll = randint(lower, upper)
	print("It's a custom sized die---->" + str(roll))


custom_die(1, 20)