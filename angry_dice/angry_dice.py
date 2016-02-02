__author__="Shawn Waldow"

from random import randint



################################
#For sound effects
################################
import os
"""To make these terminal sounds eg: beep_slow(5) would beep 5x with long pauses."""
beep_slow = lambda x: os.system("echo -n '\a';sleep .4;" * x)
beep_medium = lambda x: os.system("echo -n '\a';sleep .2;" * x)
beep_fast = lambda x: os.system("echo -n '\a';sleep .05;" * x)



class Die:
	"""Define a single die's data and methods."""

	def __init__(self):
		
		self.locked = False
		self.current_roll = 1
		self.faces = ["Error", """
			+-------+
			|       |
			|   o   |
			|       |
			+-------+""",

			"""
			+-------+
			|     o |
			|       |
			| o     |
			+-------+""",
			"""
			+-------+
			| \   / |
			| ^   ^ |
			| ----- |
			+-------+""",
			"""
			+-------+
			| o   o |
			|       |
			| o   o |
			+-------+""",
			"""
			+-------+
			| o   o |
			|   o   |
			| o   o |
			+-------+""",
			"""
			+-------+
			| o   o |
			| o   o |
			| o   o |
			+-------+"""]	


		self.most_recently_locked = -1
		self.locked_or_rolling = "Rolling..."


	def __str__(self):
		"""Provide a pretty string for dice face."""
		return self.faces[self.current_roll]

	def roll(self):
		"""Roll a single die while checking for lock."""
		if self.locked:
			self.current_roll = self.current_roll
		else:
			self.current_roll = randint(1,6)
			beep_fast(5)

	def lock(self, what_turn_is_it_int):
		"""Lock the die. Keep track which turn we locked the die. Prepare a statement of lockedness."""
		self.locked = True
		self.most_recently_locked = what_turn_is_it_int
		self.locked_or_rolling = "Locked..."

	def unlock(self):
		"""Unlock the die. Prepare a statement of unlockedness."""
		self.locked = False
		self.locked_or_rolling = "Rolling..."

class Game:
	"""OO'd game logic to allow us to run several particular instances of our game."""

	def __init__(self):
		self.stage = 1
		self.die1 = Die()
		self.die2 = Die()
		#In each tuple in stage_goals we must enter the values in order. 
		#Improve this later by having the init function order them for us. 
		self.stage_goals = {1:(1,2), 2:(3,4), 3:(5,6)}
		self.player ="John Doe"
		self.turns = 0

	def start_game(self):
		"""Welcome our player."""
		print(	"\n\n\nWelcome to an authorized implementation of Angry Dice!",
				"You advance through 3 stages but rolling", self.die1.faces[3], self.die2.faces[3], 
				"\nThat's the anger that resets you to stage 1.\nYour goal for stage 1 is to roll a 1 and a 2. Let's roll!")
		
		while True:
			self.roll_dice()
			self.eval_double_grump()
			self.prompt_for_lock()
			self.validate_lock()

			#Both die locked
			if self.die1.locked and self.die2.locked:

				if self.stage == 1 or self.stage == 2:
					self.update_stage(self.stage + 1)
					print("Whohoo you matched {} {} \nGo on to stage {}".format(self.die1, self.die2, str(self.stage)))
					advanceing_tuple = self.stage_goals[self.stage]
					print("Now match: ", self.die1.faces[advanceing_tuple[0]], self.die2.faces[advanceing_tuple[1]])
				elif self.stage == 3:
					self.win()
				else:
					print("ERROR 2")
					exit()

			#One or none die locked
			else:
				pass

	def roll_dice(self):
		"""Roll each die"""
		if self.die1.locked == False:
			self.die1.roll()
		if self.die2.locked == False:
			self.die2.roll()
		self.turns += 1

	def update_stage(self, stage_to_advance_to):
		"""Change the stage and unlock the dice."""
		self.stage = stage_to_advance_to
		self.die1.unlock()
		self.die2.unlock()

	def eval_double_grump(self):
		"""Catch the user rolling double angry faces and reset stage to 0."""
		if self.die1.current_roll == self.die2.current_roll and self.die1.current_roll == 3:
			print("Die 1 {0} , Die 2 {1}  ! ANGRY DICE !\n".format(self.die1, self.die2))
			beep_slow(5)
			self.update_stage(1)

	def prompt_for_lock(self):
		"""Prompt the user to lock one or both die."""

		print("\n{} die 1: {}, \n{} die 2: {} \n".format(self.die1.locked_or_rolling, self.die1, self.die2.locked_or_rolling, self.die2))
		
		#Loop to get valid user input
		temp_input_valid = False
		while not temp_input_valid:
			try:
				choice = int(input("Current stage: {}  Match: {}\nNow enter a number to do one of the following: \n(9) quits.\n(0) rerolls without toggling lock on any dice."\
					"\n(1) toggles lock on die 1. \n(2) toggles lock on die 2 "\
					".\n(3) locks in both die (You have a match?).\n>>> ".format(self.stage,
					 self.stage_goals[self.stage])))
				if choice == 1 or choice == 2 or choice == 3 or choice == 0 or choice == 9:
					temp_input_valid = True
				else:
					print("BAD INPUT. TRY AGAIN.")
					beep_slow(1)
			except:
				print("BAD INPUT. TRY AGAIN.")
				beep_slow(1)		
		
		#dial 9 to quit
		if choice == 9:
			print("GOODBYE QUITTER!")
			exit()

		#Toggle no die
		if choice == 0:
			pass
		
		#Toggle lock die 1
		elif choice == 1:
			self.die1.unlock() if self.die1.locked else self.die1.lock(self.turns)
		
		#Lock die 2
		elif choice == 2:
			self.die2.unlock() if self.die2.locked else self.die2.lock(self.turns)

		#Allow user to lock both die. Improve by refining most_recently_locked.
		elif choice == 3:
			self.die1.lock(self.turns)
			self.die2.lock(self.turns)
			
		else:
			print("Error 3")
			exit()

	def validate_lock(self):
		"""	Unlock the dice lock if it makes no sense for this round or if it violates the rules. Alert user.
			Move to one of three possible states: One valid lock. Two vaild locks. No valid locks."""
		
		#Make a sorted temporary tuple of the dice current values to compare to matching dict.
		temp_tuple = tuple(sorted((self.die1.current_roll, self.die2.current_roll)))
		#print("Stage: ",self.stage, "Temp tuple :", temp_tuple, "Current stage goals: ", self.stage_goals[self.stage] )
		
		#User has a double lock so they think they have a stage match...
		if self.die1.locked and self.die2.locked:
			if temp_tuple != self.stage_goals[self.stage]:
				print("You can't lock both those die this stage!")
				if self.die1.most_recently_locked == self.turns:
					self.die1.unlock()

				if self.die2.most_recently_locked == self.turns:
					self.die2.unlock()

			#Now we know there was an incorrect lock of some kind.	
			#See if die1 had the incorrect lock
			elif self.die1.most_recently_locked == self.turns:
				if self.die1.current_roll in self.stage_goals[self.stage]:
					pass
				else:
					self.die1.unlock()
					print("You cant lock a {} in stage {}".format(self.die1, str(self.stage)))

			#Remember we know there was an incorrect lock of some kind.	
			#See if die2 had the incorrect lock
			elif self.die2.most_recently_locked == self.turns:
				if self.die2.current_roll in self.stage_goals[self.stage]:
					pass
				else:
					self.die2.unlock()
					print("You cant lock a {} in stage {}".format(self.die2, str(self.stage)))

		#We just locked die1? Check it for this stage
		elif self.die1.most_recently_locked == self.turns:
			if self.die1.current_roll in self.stage_goals[self.stage]:
				if self.stage == 3 and self.die1.current_roll == 6:
					self.die1.unlock()
					print("You can't lock a 6 first in this stage!")
			else:
				self.die1.unlock()
				print("You cant lock a {} in stage {}".format(self.die1, str(self.stage)))

		#We just locked die2? Check it for this stage
		elif self.die2.most_recently_locked == self.turns:
			if self.die2.current_roll in self.stage_goals[self.stage]:
				if self.stage == 3 and self.die2.current_roll == 6:
					self.die2.unlock()
					print("You can't lock a 6 first in this stage!")

			else:
				self.die2.unlock()
				print("You can't lock a {} in stage {}".format(self.die2, str(self.stage)))



		
	def win(self):
		"""Display a pretty message and exits the program."""
		print("""
         ƇHƐƐƦS !!
         °           °
         o °       ° o
        ╔║░░║      ║░░║╗
        ╚║░░║      ║░░║╝
         ▔▔▔▔      ▔▔▔▔
          You Win!

         """)
		exit()

def main():

	this_game = Game()

	this_game.start_game()

if __name__ == '__main__':
	main()