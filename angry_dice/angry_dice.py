__author__="Shawn Waldow"

from random import randint



################################
#For sound effects
################################
import os
"""	To make these terminal sounds 
	eg: beep_slow(5) would beep 5x with long pauses."""

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
		"""Roll a single die if it isn't locked."""
		if self.locked:
			self.current_roll = self.current_roll
		else:
			self.current_roll = randint(1,6)
			beep_fast(5)

	def lock(self, what_turn_is_it_int):
		"""	Lock the die. Keep track which turn we locked the die. 
			Prepare a statement of lockedness."""
		
		self.locked = True
		self.most_recently_locked = what_turn_is_it_int
		self.locked_or_rolling = "Locked..."

	def unlock(self):
		"""Unlock the die. Prepare a statement of unlockedness."""
		self.locked = False
		self.locked_or_rolling = "Rolling..."

class Game:
	"""	OO'd game logic to allow us to run several particular instances 
		of our game."""

	def __init__(self):
		self.stage = 1
		self.die1 = Die()
		self.die2 = Die()
		
		#In each tuple in stage_goals we must enter the values in order. 
		#Improve this later by having the init function order them for us. 
		self.stage_goals = {1:(1,2), 2:(3,4), 3:(5,6)}
		
		#Orphaned. Later we can prompt user for their name...
		self.player ="John Doe" 
		
		#...and track a high score based on number of turns to win.
		# For now we still use this turn counter to back out invalid locks
		# where 1 of 2 values locked are valid.
		self.turns = 0

	def start_game(self):
		"""Welcome our player."""
		print(	"\n\n\nWelcome to an authorized implementation of Angry Dice!",
				"You advance through 3 stages but rolling", self.die1.faces[3], 
				self.die2.faces[3], 
				"\nThat's the anger that resets you to stage 1."\
				"\nYour goal for stage 1 is to roll a 1 and a 2. Let's roll!")
		
		while True:
			self.roll_dice()
			self.eval_double_grump()
			# Allow user to lock or unlock one or both die
			self.prompt_for_lock()
			# Back out invalid locks and display correction to user.
			self.validate_lock()

			# At this point we are assured all existing locks valid. Therefore
			# if both die are locked we have matched stage criteria and need
			# to advance...
			# ...Are both die locked?
			if self.die1.locked and self.die2.locked:

				# Stage 1 and stage 2 have the same housekeeping, but different
				# criteria for matching.
				if self.stage == 1 or self.stage == 2:
					self.update_stage(self.stage + 1)
					print(	"Whohoo you matched {} {} \nGo on to stage {}"\
							.format(self.die1, self.die2, str(self.stage)))
					
					# Some extra formating to show pretty ASCII die faces for
					# the matching goal instead of the ints in the tuple.
					advanceing_tuple = self.stage_goals[self.stage]

					print(	"Now match: ", self.die1.faces[advanceing_tuple[0]], 
							self.die2.faces[advanceing_tuple[1]])
				
				# A valid match while in stage 3 means user won!
				elif self.stage == 3:
					self.win()
				
				# Just to be stupid safe.		
				else:
					print("ERROR 2")
					exit()

			# One or none die locked. We know they are valid so let the game 
			# logic "roll" on. Put this here just to be explicit and readable.
			else:
				pass

	
	def roll_dice(self):
		"""Roll each die"""
		
		# Only roll them if they are unlocked
		if not self.die1.locked:
			self.die1.roll()
		
		if not self.die2.locked:
			self.die2.roll()
		
		# Mark that we have begun a turn
		self.turns += 1

	
	def update_stage(self, stage_to_advance_to):
		"""Change the stage and unlock the dice."""
		#Advance the stage
		self.stage = stage_to_advance_to
		
		#Unlock the dice
		self.die1.unlock()
		self.die2.unlock()

	

	def eval_double_grump(self):
		"""Catch the user rolling double angry faces and reset stage to 0."""
		
		# If we have double angry 3s.
		if self.die1.current_roll == 3 and self.die2.current_roll == 3:
			print(	"\nDie 1\n{0}\nDie 2\n{1}\n!!!ANGRY DICE!!!\n"\
					.format(self.die1, self.die2))
			beep_slow(5)
			
			# Send user back to stage 1.
			self.update_stage(1)



	def prompt_for_lock(self):
		"""Prompt the user to lock one or both die."""

		# Display pretty dice faces and show if each is locked or rollable.
		print("\n{} die 1: {}, \n{} die 2: {} \n".format(
			self.die1.locked_or_rolling, self.die1, self.die2.locked_or_rolling,
			self.die2))
		
		# Loop to get valid user input
		temp_input_valid = False
		while not temp_input_valid:
			try:
				
				#temp_for_menu_display_matches = self.stage_goals[:]
				#temp_for_menu_display_matches[2] = (':<', '4') 

				choice = int(input("Current stage: {}  Match: {}\nNow enter a"\
					"number to do one of the following: \n(9) quits.\n(0)"\
					" rerolls without toggling lock on any dice."\
					"\n(1) toggles lock on die 1. \n(2) toggles lock on die 2 "\
					".\n(3) locks in both die (You have a match?)."\
					"\n>>> ".format(self.stage, self.stage_goals[self.stage]	 
					if self.stage != 2 else (':<',4)))) 
					#^^^THIS WEIRD BIT AT THE END WOULD REALLY TRIP US UP IF 
					#WE CHANGED THE STAGE GOALS BEWARE!!!!
				
				# If valid input
				if -1 < choice < 4 or choice == 9:
					# Then leave the while loop
					temp_input_valid = True
				else:
					print("BAD INPUT. TRY AGAIN.")
					beep_slow(1)

			# A belt AND suspenders. My pants shall'na fall. Nosiree.
			except:
				print("BAD INPUT. TRY AGAIN.")
				beep_slow(1)		
		
		# OKAY! What a long winded way to get a 0,1,2,3, or 9!
		# Now execute the user's choice...
		
		# Dial 9 to quit
		if choice == 9:
			print("GOODBYE QUITTER!")
			exit()

		#Toggle no die
		if choice == 0:
			#From here the game's logic just goes to roll 'em.'
			pass
		
		#Toggle lock die 1
		elif choice == 1:
			self.die1.unlock() if self.die1.locked else \
				self.die1.lock(self.turns)
		
		#Lock die 2
		elif choice == 2:
			self.die2.unlock() if self.die2.locked else \
				self.die2.lock(self.turns)

		#Allow user to lock both die.
		elif choice == 3:
			# We are careful to only lock unlocked die to preserve
			# History of when locked.
			if not self.die1.locked:
				self.die1.lock(self.turns)
			if not self.die2.locked:
				self.die2.lock(self.turns)
			
		else:
			print("Error 3")
			exit()

	def validate_lock(self):
		"""	Unlock the dice lock if it makes no sense for this round or if it 
			violates the rules. Alert user. Move to one of three possible 
			states: One valid lock. Two vaild locks. No valid locks."""
		

		# Make a sorted temporary tuple of the dice current values 
		# to compare to the tuple in the matching dict.
		temp_tuple = tuple(
			sorted((self.die1.current_roll, self.die2.current_roll)))

		
		# In the game loop we have already checked for angry dice at this point.
		#
		# Now lets consider the case where two dice are locked.
		# User has a double lock so they think they have a stage match...
		if self.die1.locked and self.die2.locked:
			if temp_tuple != self.stage_goals[self.stage]:
				print("You can't lock both those die this stage!")
				beep_slow(2)

				# It could be the user selected (3) lock both when they already 
				# had one valid lock. If that's the case let us only back off 
				# the most recent lock.

				# Die1 was just locked
				if self.die1.most_recently_locked == self.turns:
					self.die1.unlock()

				# Die2 was just locked
				if self.die2.most_recently_locked == self.turns:
					self.die2.unlock()


		# Now here in the overall flow of the game we have checked for double 
		# grump and for invalid double locks of all kinds. Now lets handle 
		# single locks which are invalid (per each stage).
		
		# If die1 was the most recently locked:
		elif self.die1.most_recently_locked == self.turns:
			
			#Does die1 have a number we are seeking in this stage?
			if self.die1.current_roll in self.stage_goals[self.stage]:
				
				#If we are in stage 3 do not allow a 6 to be locked alone.
				if self.stage == 3 and self.die1.current_roll == 6:
					self.die1.unlock()
					print("You can't lock a\n{}\nfirst in this stage!"\
						.format(self.die1.faces[6]))
			
			#If die1 wasn't found in current goals it should be unlocked. 
			else:
				self.die1.unlock()
				print("You cant lock a {} in stage {}".format(
					self.die1, str(self.stage)))

		#We just locked die2? Check it for this stage:
		elif self.die2.most_recently_locked == self.turns:

			#Does die2 have a number we are seeking in this stage?
			if self.die2.current_roll in self.stage_goals[self.stage]:

				#If we are in stage 3 do not allow a 6 to be locked alone.
				if self.stage == 3 and self.die2.current_roll == 6:
					self.die2.unlock()
					print("You can't lock a\n{}\nfirst in this stage!"\
						.format(self.die2.faces[6]))

			#If die2 wasn't found in current goals it should be unlocked. 
			else:
				self.die2.unlock()
				print("You can't lock a {} in stage {}".format(
					self.die2, str(self.stage)))



		
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

	#Create an instance of the class Game
	this_game = Game()

	#Start it up!
	this_game.start_game()

if __name__ == '__main__':
	main()