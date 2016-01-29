__author__="Shawn Waldow"

from random import randint

class Die:
	"""Define a single die's data and methods."""

	def __init__(self):
		
		locked = False
		current_roll = 1

	def __str__(self):
		"""Provide a pretty string for dice face."""
		faces = ["ERROR", ".", ":", ":<",": :",":.:",":::"]
		return faces[self.current_roll]

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
		stage_goals = {}
		player =""

	def start_game():
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

	def roll_dice():
		"""Roll each die"""


	def update_stage():
		"""Change the stage and unlock the dice."""


	def eval_double_grump():
		"""Catch the user rolling double angry faces and reset stage to 0"""


	def prompt_for_lock():
		"""Prompt the user to lock one or both die."""


	def validate_lock():
		"""	Unlock the dice lock if it makes no sense for this round or if it violates the rules. Alert user.
			Move to one of three possible states: One valid lock. Two vaild locks. No valid locks."""


	def win():
		"""Display a pretty message and exits the program."""



