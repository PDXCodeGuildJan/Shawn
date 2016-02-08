#Pseudocode for program loop
#room we are in
#opening room statement
#cue to look or leap without looking
#look
#	cue for diection
#	go requested direction
#	update feeling and hitpoints
#	room statement
#leap
#	go random direction
#	update feeling and hitpoints
#	room statement
#loop back to look or leap
#


#################### MAP of GOAT MUD############################################
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMM.......................................................MMMMM
#MMMMMMMMMMMMMMMMMMMM.......................................................MMMMM
#MMMMMMMMMMMMMMMMMMMM............... Ravine (Leap or die)...................MMMMM
#MMMMMMMMMMMMMMMMMMMM.......................................................MMMMM
#MMMMMMMMMMMMMMMMMMMM.......................................................MMMMM
#MMMMMMMMMMMMMMMMMMMM$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$MMMMM
#MMMMMMMMMMMMMMMMMMMMZ.........................................OOOOOOOOOOOOOMMMMM
#MMMMMMMMMMMMMMMMMMMMZ.........................................OOOO  Play  OMMMMM
#MMMMMMMMMMMMMMMMMMMMZ........... Pasture .....................OOOO  Hill  OMMMMM
#MMMMMMMMMMMMMMMMMMMMZ.........................................OOOO  (Win) OMMMMM
#MMMMMMMMMMMMMMMMMMMMZ.........................................OOOOOOOOOOOOOMMMMM
#MMMMMMMMMMMMMMMMMMMM$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$OOOOOOOOOOOOOMMMMM
#MMMMMMMMMMMMMMMMMMMMO..........................MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMO..........................MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMO..........................MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMO..........................MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMO..........................MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMO..........................MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMNZZZZZZZZZZZZZO..........................ZZZZZZZZZZZZMMMMMMMMMMMMMMMMMMMMM
#MMMMMMNZZZ warm ZZZZO.......Barn Floor.........ZZZ pigs ZZZMMMMMMMMMMMMMMMMMMMMM
#MMMMMMNZZZ stall ZZZO..........................ZZZZZZZZZZZZMMMMMMMMMMMMMMMMMMMMM
#MMMMMMNZZZZZZZZZZZZZO..........................ZZZZZZZZZZZZMMMMMMMMMMMMMMMMMMMMM
#MMMMMMNZZZZZZZZZZZZZO..........................ZZZZZZZZZZZZMMMMMMMMMMMMMMMMMMMMM
#MMMMMMNZZZZZZZZZZZZZO..........................ZZZZZZZZZZZZMMMMMMMMMMMMMMMMMMMMM
#MMMMMMNZZZZZZZZZZZZZO..........................ZZZZZZZZZZZZMMMMMMMMMMMMMMMMMMMMM
#MMMMMMNZZZZZZZZZZZZZO..........................ZZZZZZZZZZZZMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMO..........................MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMO..........................MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMZZZZZZZZZZZZZZZZZZZZZZZZZZZMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMZZZZZZZZZZ loft ZZZZZZZZZZZMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMZZZZZZZZZZZZZZZZZZZZZZZZZZZMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMZZZZZZZZZZZZZZZZZZZZZZZZZZZMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM

from random import randint
import os


####################################################################################
#Some sound effects
####################################################################################

beep_slow = lambda x: os.system("echo -n '\a';sleep .4;" * x)
beep_medium = lambda x: os.system("echo -n '\a';sleep .2;" * x)
beep_fast = lambda x: os.system("echo -n '\a';sleep .05;" * x)


class Character:

	def __init__(self, hp_int, describe_string, feel_dict, human_player_bool):
		"""Attributes"""
		self.feelings = feel_dict
		self.hp = hp_int
		self.describe = describe_string
		self.human_player = human_player_bool
	
	def __str__(self):
		self.feelings[self.hp]

class Goat(Character):

	def __init__(self, hp_int, describe_string, feel_dict, human_player_bool):

		super().__init__(hp_int, describe_string, feel_dict, human_player_bool)


class Place:

	def __init__(	a, name_str, leap_direction="right", bold_leap_messg_str, 
					location_str, opening_desc_str, direction_action_dict, 
					look_messg_str, 
					what_lol_str = "What? Remember you have two choices:",
					wordy1_str="", wordy2_str =""):
	"""	Using the letter z instead of the usual convention self for object self-
		reference. Some of these argument names are self explanitory, yes? 
		Direction_action_dict is a dictionary that has direction as a key gving
		the value of a function name to be called when going to direction."""

		z.leap_direction = leap_direction 
		z.bold_leap_messg = bold_leap_messg_str 
		z.location = location_str 
		z.opening_desc = opening_desc_str 
		z.direction_action = direction_action_dict 
		z.look_messg = look_messg_str
		z.what_lol = what_lol_str
		z.wordy1 = wordy1_str 
		z.wordy2 = wordy2_str
		z.name = name_str

	def leap(z):
	"""Leap boldly specialized for this place."""

	def entry(z):
	"""Enter the place."""

	def look(z):
	"""Look around the place."""

	def pee(z):
	"""Pee on this place."""

	def get(z, character_input):
	"""Takes from character prompt for direction to go/action to take."""

	def go(z):
	"""Go in user specified direction."""

	def barrier_return(z):

class Game:

	def __init__(self, start_place):

		z.current_place = start_place
		z.path_taken = []
		z.turn = 0


	def game_housekeeping(self):

		pass

	def update_path_taken(self):

		pass



#Global strings to simplify passing and changing dialogue
Feel = "capricious and impatient"
exit_message = "\nLater lazy goat!"
look_or_leap = "\n\t>Look or leap? "
leap_boldly_message = "\n\nYou leap boldly "
which_way = "\n\t>Which way to move: forwards, backwards, left, or right? "
come_again = "\nThat makes no sense. One to many headbutts maybe, eh?"
what_lol = "What? Remember you have two choices:"
pee = "\nAhhh. This is my {} now."
path_taken = []
	
####################################################################################
#ROOM
#"The barn floor."
####################################################################################
def barn_floor():
	
	global path_taken
	lol = "" #l.ook o.r l.eap variable initialed
	direction ="" #Direction of travel variable.
	leap_direction = "right"
	location = "barn"

	print("\n\nThe musty dirt under your goat hooves smells familiar,\nbut nothing else in this old barn do you remember.\nYou feel {}.".format(Feel))
	
	#Lets offer some options and get input
	while lol == "":
		
		lol = input(look_or_leap)
		
		
		#LOOK#########################
		if lol.lower() == "look":
			
			print("\n\nBehind you is a staircase to an empty loft.\nRight is a pen filled with restless pigs.\nForwards is an open door.\nLeft is a dark stall.")
			direction = input(which_way)
				
			if direction.lower() == "forwards":
				print("\nYou leap {}.".format(direction))
				beep_medium(3)
				path_taken.extend(["look", "forwards", "pasture"])
				return pasture
			elif direction.lower() == "backwards":
				print("\nYou leap {}.".format(direction))
				path_taken.extend(["look", "backwards", "loft"])
				beep_medium(3)
				return loft
			elif direction.lower() == "right":
				print("\nYou leap {}.".format(direction))
				path_taken.extend(["look", "right", "pigs"])
				beep_medium(3)
				return pigs
			elif direction.lower() == "left":
				print("\nYou leap {}.".format(direction))
				path_taken.extend(["look", "left", "warm stall"])
				beep_medium(3)
				return warm_stall
			elif direction.lower() == "q":
				print(exit_message)
				exit()
			elif direction.lower() == "p":
				print(pee.format(location))
				beep_slow(1)
				return barn_floor
			else:
				print(come_again)
				beep_slow(1)
				return barn_floor
				

		#LEAP########################
		elif lol.lower() == "leap":
			path_taken.extend(["leap boldly", "pigs"])
			beep_fast(5)
			print(leap_boldly_message + "{}.".format(leap_direction))
			return pigs

		#QUIT#######################
		elif lol.lower() == "q":
			print(exit_message)
			exit()
		
		#PEE#######################
		elif lol.lower() == "p":
			print(pee.format(location))
			beep_slow(1)
			return barn_floor		
		
		#GIBBERISH HANDLING#########
		else:
			lol = ""
			print(what_lol)
			#End of barn function#



####################################################################################
#ROOM
#Pig Pen
####################################################################################
def pigs():
	
	lol = "" #l.ook o.r l.eap variable initialed
	direction ="" #Direction of travel variable.
	leap_direction = "backwards"
	location = "pig pen"

	print("\n\nPigs! They are biting your legs. Ga-a-a-a-a-a-a!!! What do we do?")
	
	#Lets offer some options and get input
	while lol == "":
		
		lol = input(look_or_leap)

		#LOOK#########################
		if lol.lower() == "look":
				
			print("\n\nWhile you were looking around with your pea brain the pigs drag you down to your death.\n")
			path_taken.extend(["look", "death by pig"])
			return death
					
		#LEAP########################
		elif lol.lower() == "leap":
			beep_fast(5)
			print(leap_boldly_message + "{}.".format(leap_direction))
			path_taken.extend(["leap", "backwards", "barn floor"])
			return barn_floor

		#QUIT#######################
		elif lol.lower() == "q":
			print(exit_message)
			exit()
		
		#PEE#######################
		elif lol.lower() == "p":
			print(exit_message)
			print("\nWhile you pee the pigs drag you down to your death.".format(location))
			path_taken.extend(["p","death by pig"])
			beep_slow(1)
			return death		
		
		#GIBBERISH HANDLING#########
		else:
			lol = ""
			print(what_lol)
			#End of Pigs#



####################################################################################
#ROOM
#Ravine
####################################################################################

def ravine():
	###
	lol = "" #l.ook o.r l.eap variable initialed
	direction ="" #Direction of travel variable.
	leap_direction = "backwards"
	location = "ravine"
	coyotes = "\n\nYou get stuck in ouchy thorns.\nYou hear yipping.\nStruggling to get free.\nOuch my neck! My ass! Coyotes are attacking me!\n\n"

	print("\n\nNo Sun. No wind,\nbut you smell meat eaters.\nNot many leaves out on all this brush now.\n")

	#Lets offer some options and get input
	while lol == "":
		
		lol = input(look_or_leap)

		#LOOK#########################
		if lol.lower() == "look":
			
			print("\n\nLeft, right,and forwards is a maze of tunnels through the thick, thorny brush.\nYou would have to knell and crawl they are a little smaller than you.\nDelicious in summer probably.\nYou hear water.\nBackwards is that good graze grass.\n")
			direction = input(which_way)
				
			if direction.lower() == "forwards":
				print(coyotes)
				beep_fast(5)
				path_taken.extend(["look", "forwards", "death by coyotes"])
				return death
			elif direction.lower() == "backwards":
				print("\nYou leap {}.".format(direction))
				beep_medium(3)
				path_taken.extend(["look", "backwards", "pasture"])
				return pasture
			elif direction.lower() == "right":
				print(coyotes)
				path_taken.extend(["look", "right", "death by coyotes"])
				beep_fast(5)
				return death
			elif direction.lower() == "left":
				print(coyotes)
				path_taken.extend(["look", "left", "death by coyotes"])
				beep_fast(5)
				return death
			elif direction.lower() == "q":
				print(exit_message)
				exit()
			elif direction.lower() == "p":
				print(pee.format(location))
				beep_slow(1)
				path_taken.extend(["p", "ravine"])
				return ravine
			else:
				print(come_again)
				return ravine
			
		#LEAP########################
		elif lol.lower() == "leap":
			beep_fast(5)
			print("\n\nYou leap boldly {}".format(leap_direction))
			path_taken.extend(["leap", leap_direction, "pasture"])
			return pasture

		#QUIT#######################
		elif lol.lower() == "q":
			print(exit_message)
			exit()
		
		#PEE#######################
		elif lol.lower() == "p":
			print(pee.format(location))
			beep_slow(1)
			path_taken.extend(["p", "ravine"])
			return ravine		
		
		#GIBBERISH HANDLING#########
		else:
			lol = ""
			print(what_lol)

	##End of Ravine#



####################################################################################
#ROOM
#Play Hill
####################################################################################
def play_hill():
	print("\n\nWhat a nice pile of rocks and dirt!\nUp! Up! Up!\nScamper, caper, scamper.")
	lol = "" #l.ook o.r l.eap variable intialized
	direction =""#Direction of travel variable.
	leap_direction = "right"
	location = "lil' hill"

	#Lets offer some options and get input
	while lol == "":

		lol = input(look_or_leap)

		#LOOK######################
		if lol.lower() == "look":

			print("\n\nDown the hill left is that nice pasture.\nLook the sun's setting over there.\nNorth forwards is a ravine.\nSouth is the barn.\nWhat a nice farm house on the right!\n\n")
			direction = input(which_way)
			print("\n\nNaw, to hell with going {} now.\nThis hill's fine.\nIt's great to be a goat.\n\n".format(direction))
			path_taken.extend(["look", "win"])
			return win

		#LEAP#########################
		elif lol.lower() == "leap":
			beep_fast(5)
			print("\n\nYippee! It's great to be a goat.\nGood hill. Good farm.\n\n")
			path_taken.extend(["leap", "win"])
			return win

		#QUIT########################
		elif lol.lower() == "q":
			print(exit_message)
			exit()

		#PEE#########################
		elif lol.lower() == "p":
			print(pee.format(location))
			beep_slow(1)
			path_taken.extend(["p", "play hill"])
			return play_hill

		#GIBBERISH HANDLING##########
		else:
			lol = ""
			print(what_lol)

	#End of Play Hill#



####################################################################################
#ROOM
#Pasture
####################################################################################
def pasture():
	lol = "" #l.ook o.r l.eap variable intialized
	direction =""#Direction of travel variable.
	leap_direction = "right"
	location = "pasture"

	print("\n\nA beautiful green glowing pasture. It's a little foggy.")

	#Lets offer some options and get input
	while lol == "":

		lol = input(look_or_leap)

		print("\n\nNum-num-num. Not now. Eating.")  #The goat gets stubborn

		lol = input(look_or_leap)

		print("\n\nNum-num-num. Not now. Eating.")	#The goat gets stubborn

		lol = input(look_or_leap)


		#LOOK######################
		if lol.lower() == "look":

			print("\n\nSweet succulent grass all around.\nLeft is a damn tough looking fence.\nAhead is a dark ravine.\nThat barn's behind,\nand to the right is a little rocky hill!")
			direction = input(which_way)

			if direction.lower() == "forwards":
				print("\nYou leap {} into the dark ravine.".format(direction))
				path_taken.extend(["look", "forwards", "ravine"])
				beep_medium(3)
				return ravine
			elif direction.lower() == "backwards":
				print("You leap {}".format(direction) + " to the barn. How adventerous.")
				path_taken.extend(["look", "backwards", "barn floor"])
				beep_slow(3)
				return barn_floor
				###.###
			elif direction.lower() == "right":
				print("Okay! \nYou leap {}".format(direction) + " to the lil' hill.")
				beep_medium(3)
				beep_fast(3)
				path_taken.extend(["look", "right", "play hill"])
				return play_hill
			elif direction.lower() == "left":
				print("\nYou leap {}".format(direction) + " into the fence.")
				print("ZZZZZZAAAAAAAAAAAA-P!!! ")
				path_taken.extend(["look", "left", "pasture"])
				beep_fast(1)
				return pasture
			elif direction.lower() == "q":
				print(exit_message)
				exit()
			elif direction.lower() == "p":
				print(pee.format(location))
				beep_slow(1)
				path_taken.extend(["p", "pasture"])				
				return pasture
			elif direction.lower() == "eat":
				print("\nNum, num, num.")
				return  pasture
			else:
				print(come_again)
				return pasture

		#LEAP#########################
		elif lol.lower() == "leap":
			beep_fast(5)
			print(leap_boldly_message + "{}.".format(leap_direction))
			path_taken.extend(["look", leap_direction, "play hill"])
			return play_hill

		#QUIT########################
		elif lol.lower() == "q":
			print(exit_message)
			exit()

		#PEE#########################
		elif lol.lower() == "p":
			print(pee.format(location))
			path_taken.extend(["p", "pasture"])
			beep_slow(1)

		#GIBBERISH HANDLING##########
		else:
			lol = ""
			print(what_lol)

	#End of Pasture#



####################################################################################
#ROOM
#Warm Stall
####################################################################################
def warm_stall():
	lol = "" #l.ook o.r l.eap variable initialed
	direction ="" #Direction of travel variable.
	leap_direction = "backwards"
	location = "stall"

	print("\n\nThe stall is pretty dark, but warm.")
	
	#Lets offer some options and get input
	while lol == "":
		
		lol = input(look_or_leap)
		
		
		#LOOK#########################
		if lol.lower() == "look":
			
			print("\n\nThere's not much here except the door back behind you. \nIt looks like a good place to sleep.")
			direction = input(which_way)
				
			if direction.lower() == "forwards":
				print("\nYou leap {} and bash your head into the tin wall. That was silly.".format(direction))
				beep_medium(1)
				path_taken.extend(["look", "forwards", "warm stall"])
				return warm_stall
			elif direction.lower() == "backwards":
				print("\nYou leap {}".format(direction) + " to the barn floor.")
				beep_medium(3)
				path_taken.extend(["look", "backwards", "barn floor"])
				return barn_floor
			elif direction.lower() == "right":
				print("\nYou leap {} and bash your head into the tin wall. That was silly.".format(direction))
				path_taken.extend(["look", "right", "warm stall"])
				beep_medium(1)
				return warm_stall
			elif direction.lower() == "left":
				print("\nYou leap {} and bash your head into the tin wall. That was silly.".format(direction))
				path_taken.extend(["look", "left", "warm stall"])
				beep_medium(1)
				return warm_stall
			elif direction.lower() == "q":
				print(exit_message)
				exit()
			elif direction.lower() == "p":
				print(pee.format(location))
				beep_slow(1)
				path_taken.extend(["p", "warm stall"])
				return warm_stall
			elif direction.lower() == "sleep":
				print("\n...zzzzzzzzzzz...".format(location))
				return warm_stall
			else:
				print(come_again)
				beep_slow(1)
				return warm_stall
				

		#LEAP########################
		elif lol.lower() == "leap":
			beep_fast(5)
			print(leap_boldly_message + "{}.".format(leap_direction))
			path_taken.extend(["leap", leap_direction, "barn floor"])
			return barn_floor

		#QUIT#######################
		elif lol.lower() == "q":
			print(exit_message)
			exit()
		
		#PEE#######################
		elif lol.lower() == "p":
			print(pee.format(location))
			beep_slow(1)
			path_taken.extend(["p", "warm stall"])
			return warm_stall		
		
		#GIBBERISH HANDLING#########
		else:
			lol = ""
			print(what_lol)
			
	#End of Warm Stall#



####################################################################################
#ROOM
#Loft
####################################################################################
def loft():
	lol = "" #l.ook o.r l.eap variable initialed
	direction ="" #Direction of travel variable.
	leap_direction = "backwards"
	location = "loft"

	print("\n\nUp! Up! Up!\nClimbing stairs is good goat fun,\nbut up here this loft looks scary and there's no hay?\n")
	
	#Lets offer some options and get input
	while lol == "":
		
		lol = input(look_or_leap)

		#LOOK#########################
		if lol.lower() == "look":
			
			print("\n\nLeft there is a dangerous drop to the barn floor far below.\nBackwards is the staircase back down.\nOn the right is a wall.\nForwards: another wall.")
			direction = input(which_way)
				
			if direction.lower() == "forwards":
				print("\n\nYou leap {} and bash your head into the tin wall. That was silly.".format(direction))
				beep_medium(1)
				path_taken.extend(["look", "forwards", "loft"])
				return loft
			elif direction.lower() == "backwards":
				print("\nYou go {}.".format(direction))
				beep_medium(3)
				path_taken.extend(["look", "backwards", "barn floor"])
				return barn_floor
			elif direction.lower() == "right":
				print("\n\nYou leap {} and bash your head into the tin wall. That was silly.".format(direction))
				path_taken.extend(["look", "right", "loft"])
				beep_medium(1)
				return loft
			elif direction.lower() == "left":
				print("\nYou leap {} to your death!?!".format(direction))
				path_taken.extend(["look", "left", "Jump to your death"])
				beep_fast(5)
				return death
			elif direction.lower() == "q":
				print(exit_message)
				exit()
			elif direction.lower() == "p":
				print(pee.format(location))
				beep_slow(1)
				path_taken.extend(["p", "loft"])
				return loft
			else:
				print(come_again)
				return loft
			
		#LEAP########################
		elif lol.lower() == "leap":
			beep_fast(5)
			print("\n\nYou leap boldly!!!\nTo your death?!?")
			path_taken.extend(["leap", "left", "Jump to your death"])
			return death

		#QUIT#######################
		elif lol.lower() == "q":
			print(exit_message)
			exit()
		
		#PEE#######################
		elif lol.lower() == "p":
			print(pee.format(location))
			beep_slow(1)
			path_taken.extend(["p", "loft"])
			return loft		
		
		#GIBBERISH HANDLING#########
		else:
			lol = ""
			print(what_lol)
	#End of Loft#

def win():
	print("""                                      ........                                                            
                                   ~:IZ::D$$$$$$$$$$$$$$7:~                                          
                               ~$$$$$$Z::::D$$$$$::$$$::$$$Z$$=                                    
       YOU                 7$$$$$$$$$ZZ::::::$:$:::::::$$$$$$:::$                                  
       WIN!              $$$$$$$$$7?III?I:::::::::::::::::$$:::::$$$$                               
                      Z$$$$$$$?IIIIIIIIII?7::::::::::::::::::::::$$$$Z$$                            
                   ,$$$$$Z$?I?IIIIIII?==+++++:::::::::::::::::::II?Z$$$$7$       :::               
                  $$$$$$$IIIIIII?=+=++++=+++:::::::::::::::::::IIIIIIIZ$$$$$    ,:::::              
                I$$$$$II?IIII?=++==+++=++=?I::::::::::::::::::::ZIIIIIII$$$$Z7  ::::::             
               $$$$$IIIIIII++=+++===$$$Z$$Z$Z::::::::::::::::::::::IIIII?7$$$$Z :::::::             
             $Z$$$7IIIII?++=++++$$ZZ$$$$$$ZZZ::::::::::::::::::::::::I?IIIII$$$$:::::::             
            $$$$$?IIII?++====I$Z$$$$$$$I77777:::::::::::::::::::::::::+?III??ZZ::::::::            
          ,$$$$$IIIII==++++$$$Z$$Z$7777777777:::::::::::::::::::::::::::::::::::::::::::            
         :$$$$7??I??==++=I$Z$$$$77777777777$Z:::::::::::::::::::::::::::::::::::::::::::            
        ,$$$$?I?II==++++O$Z$$$77777777OOOOOOO::::::::::::::::::::::::::::::::::::::::::            
       :$$$$?IIII+=+++Z$$$$7777777OOOOOOOOOOON:::::::::::::::::::::::::::::::::::::::::,            
       $$$$?IIII=++==Z$$$$7777778OOOOOOO$$$$$$ZZN::::::::::::::::::::::::::::::::::::::             
      Z$$$?IIII===+=$$$$$77777OOOOOOZ$$$$$$''     :::::::::::::::::::::::::::::::::::::::            
     ?$$$$I?II==++=Z$Z$77777$OOO88$$$$$'          :::::::::::::::::::::::::::::::::::::::::           
    $$$$I?II=++=$$$$$7777OOOOZ$$Z$$''           :::::::::::::::::::::::::::::::::::::::::::::       
   +$$$II?I++++=Z$$$7777ZOOOO$$$$,              :::::::::::::::::::::::::::::::::::::::::::::      
   $$$$IIII=+++$$$ZI777$OOOO$$Z$,               ::::::::::::::::::::::::::::::::::::::::::::::
   $$$$III?++++Z$$$7777OOO8$$$$?               :::::  ::::::          ~::   :::::: :::::::::::::  
  ,$$$IIII++++=$$$77777OOOO$$$Z                :::::::::::::                ::::::  :::::::::::::
  ?$$$?III==+=7$$$7777ZOOOZZ$$                 :::::::::::::                 :::::        ::::::::  
                                                :::::::::::                 ,:::::        :::::::  
                                                 :::   :::                  :::::          ::::::  
                                                                           ::::::::         ::::::  
                                                                            ::::::          :::::  
                                                                            :::::::         ::::::  
                                                                             :::::          :::::  
                                                                              :::           ::::::  
                                                                                             ::::""")
	#put in a pause
	print(exit_message) #add a path print
	print(path_taken) #add to death
	exit()

####################################################################################
#DEATH
#Function
####################################################################################
def death():
	print("""
	

                 uuuuuuu
             uu$$$$$$$$$$$uu
          uu$$$$$$$$$$$$$$$$$uu
         u$$$$$$$$$$$$$$$$$$$$$u
        u$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$^   ^$$$^   ^$$$$$$u
       ^$$$$^      u$u       $$$$^
        $$$u       u$u       u$$$
        $$$u      u$$$u      u$$$
         ^$$$$uu$$$   $$$uu$$$$^
          ^$$$$$$$^   ^$$$$$$$^
            u$$$$$$$u$$$$$$$u
             u$^$^$^$^$^$^$u
  uuu        $$u$ $ $ $ $u$$       uuu
 u$$$$        $$$$$u$u$u$$$       u$$$$
  $$$$$uu      ^$$$$$$$$$^     uu$$$$$$
u$$$$$$$$$$$uu    ^^^^^    uuuu$$$$$$$$$$
$$$$^^^$$$$$$$$$$uuu   uu$$$$$$$$$^^^$$$^
 ^^^      ^^$$$$$$$$$$$uu ^^$^^^
           uuuu ^^$$$$$$$$$$uuu
  u$$$uuu$$$$$$$$$uu ^^$$$$$$$$$$$uuu$$$
  $$$$$$$$$$^^^^           ^^$$$$$$$$$$$^
   ^$$$$$^                      ^^$$$$^^
     $$$^                         $$$$^"""+"\n\n\n")
	beep_slow(5)
	print(path_taken)
	exit()



def intro():
	
	print( """                                                                                                                                            
                     =DMM7                  NM    ,MMM+                          nm                                   
                  $MMMMMM.                 MM    MMMMMMM                         NM:                                  
              . MMO    ~   NMMM   MMMMM  8MMMMM MM?  .MM  MM   MM.  MMMN   $MMMM.NMMMMZ                               
             .MM7       ,MMNMMM  N8=ZMM  MMMMM DMN    MM, MM+  MM  MMM:MM7 OMO:$M ZMMMMM                              
           .MM?  OMMM ,MM  .MM    ..OMM  MM?  .MM     MM+ MMM  MM+ MM= .MMD MM8.    ?MM                               
          OMM. .MMMM MMM   MM, NMMMMMM  ,MM   NMM    ,MM. MMM  DMM NMMMMMMM$ MMMMMM  ,MM                              
        ,MM8   .MM. MMO  =MM.,MM: .MM   MM.   MMM    MMM  MMM  ?MM  MM777777   ?NMMM~ :MM:                            
       DMMM   MMM .MMI  NMM ZMM   MMO  MMM    MMM   ,MMM  8MM  DMMD $MM     .      MMD .MM=                           
      NMMMMMMMM$  MMM7NMMO :MMO.NMMM   MMMMM  MMMMMMMMM   ,MMMMMMMM  MMMI =DM  MN~ IMM~  MMMMM                        
    .IMMMMMMMM   MMMMMMM   MMMMMNMM . +MMMM   ,MMMMMMM,    MMMMMZMM   MMMMMMMD  MMMMMMM   OMMMM.                      
    .ZMMMMO.    .DMMMI     MMM:,MM~    DMMM    .MMMMM       MMM, MM?    MMMMM+   NMMMMO     =NMMI                     
                                                 . MMM                                                              
                                                    MMM:                                                               
                                                      ~MMM 

		                 //  
	                        ((   
	                         \\__,
	                        /6 (%)\,
	                       (__/:";,;\--____----_
	                        ;; :';,:';`;,';,;';`,`
	                          ;:,;;';';,;':,';';,-Y
	                           ;,;,;';';,;':;';'; Z/
	                           / ;,';';,;';,;';;'
	                          / / |';/~~~~~\';;'
	                         ( K  | |      || |
	                          \_\ | |      || |    
	                           \Z | |      || |
	                              L_|      LL_|
	                              LW/      LLW/"""+"\n")

print("\n\nYou are lucky. You don't use punctuation, since you are a goat.\nYou know 'q' quits and 'p' pees. Mind your q's and p's!")



def main():
	
	intro()
	function_next = barn_floor()

	while 1 == 1:			###########MODIFY THIS INFINITE LOOP by moving the win and death functions out here as exit condition!!!
		function_next = function_next()



main()