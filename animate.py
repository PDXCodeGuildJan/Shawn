import time

repeat = 10

def animate_roll_1():
	print("[:]")
	while repeat > 1:
		print("\b\b\b[:]", end="")
		time.sleep(.25)
		print("\b\b\b|.|", end="")
		repeat -= 1

def animate_roll_2():
	print("[:]", end="")
	time.sleep(1)
	print("|.|", end="")
	time.sleep(1)
	print("[:]", end="")
	time.sleep(1)
	print("|.|", end="")
	time.sleep(1)
	print("[:]", end="")
	time.sleep(1)
	print("|.|", end="")


animate_roll_2()



