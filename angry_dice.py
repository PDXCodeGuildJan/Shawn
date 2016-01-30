__author__="Shawn Waldow"

from random import randint

class Die:
	"""Define a single die's data and methods."""

	def __init__(self):
		
		self.locked = False
		self.current_roll = 1
		self.faces = ["ERROR 1", ".", ":", ":<",": :",":.:",":::"]


	def __str__(self):
		"""Provide a pretty string for dice face."""
		return self.faces[self.current_roll]

	def roll(self):
		"""Roll a single die while checking for lock."""
		if self.locked:
			self.current_roll = self.current_roll
		else:
			self.current_roll = randint(1,6)

class Game:
	"""OO'd game logic to allow us to run several particular instances of our game."""

	def __init__(self):
		self.stage = 1
		self.die1 = Die()
		self.die2 = Die()
		self.stage_goals = {1:(1,2), 2:(3,4), 3:(5,6)}
		self.player ="John Doe"
		self.turns = 0

	def start_game(self):
		"""Welcome our player."""
		print("Welcome to an authorized implementation of Angry Dice!\n")
		
		while True:
			self.roll_dice()
			self.eval_double_grump()
			self.prompt_for_lock()
			self.validate_lock()
			
			#Both die locked
			if self.die1.locked and self.die2.locked:
				if self.stage == 1:
					self.update_stage(2)
					print("Whohoo you matched {} {}! Go on to stage {} and match {}".format(self.die1, self.die2, str(self.stage), self.stage_goals[self.stage]))
					self.turns += 1
				elif self.stage == 2:
					self.update_stage(3)
					print("Whohoo you matched {} {}! Go on to stage {} and match {}".format(self.die1, self.die2, str(self.stage), self.stage_goals[self.stage]))
					self.turns += 1
				elif self.stage == 3:
					self.turns += 1
					self.win()
				else:
					print("ERROR 2")
					exit()

			elif self.die2.locked:
				pass

			elif self.die1.locked:
				pass

			else:
				pass

	def roll_dice(self):
		"""Roll each die"""
		if self.die1.locked == False:
			self.die1.roll()
		if self.die2.locked == False:
			self.die2.roll()

	def update_stage(self, stage_to_advance_to):
		"""Change the stage and unlock the dice."""
		self.stage = stage_to_advance_to
		self.die1.locked = False 
		self.die2.locked = False

	def eval_double_grump(self):
		"""Catch the user rolling double angry faces and reset stage to 0"""
		if self.die1.current_roll == self.die2.current_roll and self.die1.current_roll == 3:
			print("Die 1[{0}], Die 2[{1}] ! ANGRY DICE !\n".format(self.die1, self.die2))
			self.update_stage(1)

	def prompt_for_lock(self):
		"""Prompt the user to lock one or both die."""
		print("Die 1[{0}], Die 2[{1}]\n".format(self.die1, self.die2))
		choice = int(input("Hit (0) to reroll without locking in any dice.\nHit (1) to proceed with die 1 locked and reroll die 2.\nHit (2) to proceed with die 2 locked and reroll die 1.\nHit (3) to lock in both die. You have a match right?"))
		if choice == 0:
			print("Nothing locked")
		elif choice == 1:
			self.die1.locked = True
		elif choice == 2:
			self.die2.locked = True
		elif choice == 3:
			self.die1.locked = True
			self.die2.locked = True
		else:
			print("Error 3")
			exit()

	def validate_lock(self):
		"""	Unlock the dice lock if it makes no sense for this round or if it violates the rules. Alert user.
			Move to one of three possible states: One valid lock. Two vaild locks. No valid locks."""
		print("No Validation YET?!!?")



	def win(self):
		"""Display a pretty message and exits the program."""
		print("You Win")
		exit()

def main():

	this_game = Game()

	this_game.start_game()

if __name__ == '__main__':
	main()