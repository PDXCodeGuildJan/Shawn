from random import randint


class Die:

	def __init__(self, faces_list):

		self.current_index = 0
		self.possible_values = faces_list

	def __str__(self):

		return self.possible_values[self.current_index]
	
	def roll(self):
		
		last = len(self.possible_values)-1
		self.current_index = randint(0, last)


def main():

	i = 0
	while i < 20:
		adie = Die(["a","b","c","d"])
		print(adie)
		adie.roll()
		print(adie)
		adie.roll()
		print(adie)
		i += 1

main()