####################################
#Extra text animation for dice roll
####################################

import time

repeat = 10

#Not working. Intended to be a die that bounces in one place
def animate_roll_1(repeat):
	print("[:]", end="")
	while repeat > 1:
		print("[:]", end="")
		time.sleep(.25)
		print("|.|", end="")
		repeat -= 1

#Lets try to hardcode a die that bounces in one place. Not working.
def animate_roll_1b():
	print("[:]", end="")
	time.sleep(.25)
	print("[x]", end="")
	time.sleep(.25)
	print("|.|", end="")
	

#Dice bounce down the terminal. Unfortuneatly hardcoded.
def animate_roll_2():
	print("[:]")
	time.sleep(.5)
	print("|.|")
	time.sleep(.25)
	print("[:]")
	time.sleep(.125)
	print("|.|")
	time.sleep(.11)
	print("[:]")
	time.sleep(.1)
	print("|.|")
	time.sleep(.09)

animate_roll_2()
print("\n")
animate_roll_1(repeat)
print("\n")
animate_roll_1b()
print("\n")

