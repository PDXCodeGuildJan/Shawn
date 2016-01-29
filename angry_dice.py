__author__="Shawn Waldow"

from random import randint

class Die:
	"""Define a single die's data and methods."""

	def __init__(self):
		
		locked = False
		current_roll = 1
		faces = ["ERROR 1", ".", ":", ":<",": :",":.:",":::"]


	def __str__(self):
		"""Provide a pretty string for dice face."""
		return self.faces[self.current_roll]

	def roll(self):
		"""Roll a single die while checking for lock."""
		if locked:
			return current_roll
		else:
			current_roll = randint(1,6)
			return current_roll

class Game:
	"""OO'd game logic to allow us to run several particular instances of our game."""

	def __init__(self):
		stage = 0
		die1 = Die()
		die2 = Die()
		stage_goals = {1:(1,2), 2:(3,4), 3:(5,6)}
		player ="John Doe"
		turns = 0

	def start_game(self):
		"""Welcome our player."""
		print("""Welcome to an authorized implementation of Angry Dice!\n
			## The Battle
			Players roll their dice at the **same time**, trying to get from 1 to 6 the
			fastest. The first to do so wins!

			## The Details
			Each player needs two Angry Dice. Players roll their dice, looking to complete
			Stage 1, then Stage 2, then Stage 3. When each Stage is complete, the player
			must declare it out loud.

			### Stage 1
			One die showing 1 pip, another showing 2 pips.

			### Stage 2
			One die showing the Angry face (which represents a 3), another showing 4 pips.

			### Stage 3
			One die showing 5 pips, another showing 6 pips.

			Players do not have to perfectly roll each Stage; if a die shows one face in a
			set, that die is locked (left aside) and the player now rolls the other die
			to complete the set. EXCEPTION: The 6 die face may never be locked!

			## The Anger
			If the dice ever show both Angry Faces, the player must START OVER from **Stage 1**.

			## The Victory
			The first player to race through all Stages to reach Stage 3 and announces
			"GET ANGRY!" is declared the victor!""")
		
		while True:
			self.roll_dice()
			self.evaluate_double_grump()
			self.prompt_for_lock()
			self.validate_lock()
			
			if die1.locked and die2.locked:
				if self.stage == 1:
					update_stage(2)
					print("Whohoo you matched {0}! Go on to stage {3} and match {1}".format(self.stage_goals[self.stage], self.stage_goals[self.stage + 1], str(self.stage)))
					self.turns += 1
				elif self.stage == 2:
					update_stage(3)
					print("Whohoo you matched {0}! Go on to stage {3} and match {1}".format(self.stage_goals[self.stage], self.stage_goals[self.stage + 1], str(self.stage))
					self.turns += 1
				elif self.stage == 3:
					self.turns += 1
					self.win()
				else:
					print("ERROR 2")
					exit()

	def roll_dice(self):
		"""Roll each die"""
		if self.die1.locked == False:
			self.die1.roll()
		if self.die2.locked == False:
			self.die2.roll()

	def update_stage(self, stage_to_advance_to):
		"""Change the stage and unlock the dice."""
		self.stage = stage_to_advance_to
		die1.locked, die2.locked = False

	def eval_double_grump(self):
		"""Catch the user rolling double angry faces and reset stage to 0"""
		if die1.current_roll == die2.current_roll and die1.current_roll:
		print("Die 1[{0}], Die 2[{1} ! ANGRY DICE !\n".format(self.die1, self.die2))
			self.update_stage(1)

	def prompt_for_lock(self):
		"""Prompt the user to lock one or both die."""
		print("Die 1[{0}], Die 2[{1}\n".format(self.die1, self.die2))
		choice = input("Hit (0) to reroll without locking in any dice.\nHit (1) to proceed with die 1 locked and reroll die 2.\nHit (2) to proceed with die 2 locked and reroll die 1.\nHit (3) to lock in both die. You have a match right?")
		if choice == 0:
			break
		elif choice == 1:
			die1.locked = True
		elif choice == 2:
			die2.locked = True
		elif choice == 3:
			die1, die2 = True
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

