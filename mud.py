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


#Global variable for how the character feels
Feel = "capricious and impatient"
exit_message = "\nLater lazy goat!"


	
####################################################################################
#ROOM
#"The barn floor."
####################################################################################
def barn_floor():
	
	lol = "" #l.ook o.r l.eap variable initialed
	direction ="" #Direction of travel variable.
	leap_direction = "right"
	location = "barn"

	print("\n\nThe musty dirt under your goat hooves smells familiar,\nbut nothing else in this old barn do you remember.\nYou feel {}.".format(Feel))
	
	#Lets offer some options and get input
	while lol == "":
		
		lol = input("\n\t>Look or leap? ")
		
		
		#LOOK#########################
		if lol.lower() == "look":
			
			print("\n\nBehind you is a staircase to an empty loft.\nRight is a pen filled with restless pigs.\nforwards is an open door.\nLeft is a dark stall.")
			direction = input("\n\t>Which way to move? forwards, backwards, left, or right? ")
				
			if direction.lower() == "forwards":
				print("\nYou leap {}.".format(direction))
				beep_medium(3)
				return pasture
			elif direction.lower() == "backwards":
				print("\nYou leap {}.".format(direction))
				beep_medium(3)
				return loft
			elif direction.lower() == "right":
				print("\nYou leap {}.".format(direction))
				beep_medium(3)
				return pigs
			elif direction.lower() == "left":
				print("\nYou leap {}.".format(direction))
				beep_medium(3)
				return warm_stall
			elif direction.lower() == "q":
				print(exit_message)
				exit()
			elif direction.lower() == "p":
				print("\nAhhh. This is my {} now.".format(location))
				beep_slow(1)
				return barn_floor
			else:
				print("\nThat makes no sense. One to many headbutts maybe, eh?")
				beep_slow(1)
				return barn_floor
				

		#LEAP########################
		elif lol.lower() == "leap":
			beep_fast(5)
			print("\n\nYou leap bodly!!!")
			return pigs

		#QUIT#######################
		elif lol.lower() == "q":
			print(exit_message)
			exit()
		
		#PEE#######################
		elif lol.lower() == "p":
			print(exit_message)
			print("\nAhhh. This is my {} now.".format(location))
			beep_slow(1)
			return barn_floor		
		
		#GIBBERISH HANDLING#########
		else:
			lol = ""
			print("What? Remember you have two choices:")
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
		
		lol = input("\n\t>Look or leap? ")

		#LOOK#########################
		if lol.lower() == "look":
				
			print("\n\nWhile you were looking around with your pea brain the pigs drag you down to your death.\n")
			return death
					
		#LEAP########################
		elif lol.lower() == "leap":
			beep_fast(5)
			print("\n\nYou leap bodly!!!")
			return barn_floor

		#QUIT#######################
		elif lol.lower() == "q":
			print(exit_message)
			exit()
		
		#PEE#######################
		elif lol.lower() == "p":
			print(exit_message)
			print("\nWhile you pee the pigs drag you down to your death.".format(location))
			beep_slow(1)
			return death		
		
		#GIBBERISH HANDLING#########
		else:
			lol = ""
			print("What? Remember you have two choices:")
			#End of Pigs#



####################################################################################
#ROOM
#Ravine
####################################################################################

def ravine():
	print("\n\nRavine!")
	return death
	#End of Ravine#



####################################################################################
#ROOM
#Play Hill
####################################################################################
def play_hill():
	print("\n\nplay_hill")
	return win
	#End of Play Hill#



####################################################################################
#ROOM
#Pasture
####################################################################################
def pasture():
	print("\n\nPasture")
	return barn_floor
	#End of Pasture#



####################################################################################
#ROOM
#Warm Stall
####################################################################################
def warm_stall():
	lol = "" #l.ook o.r l.eap variable initialed
	direction ="" #Direction of travel variable.
	leap_direction = "right"
	location = "stall"

	print("\n\nThe stall is pretty dark, but warm.")
	
	#Lets offer some options and get input
	while lol == "":
		
		lol = input("\n\t>Look or leap? ")
		
		
		#LOOK#########################
		if lol.lower() == "look":
			
			print("\n\nThere's not much here except the door back behind you. \nIt looks like a good place to sleep.")
			direction = input("\n\t>Which way to move? forwards, backwards, left, or right? ")
				
			if direction.lower() == "forwards":
				print("\nYou leap {} and bash your head into the tin wall. That was silly.".format(direction))
				beep_medium(1)
				return warm_stall
			elif direction.lower() == "backwards":
				print("\nYou leap {}".format(direction))
				beep_medium(3)
				return barn_floor
			elif direction.lower() == "right":
				print("\nYou leap {} and bash your head into the tin wall. That was silly.".format(direction))
				beep_medium(1)
				return warm_stall
			elif direction.lower() == "left":
				print("\nYou leap {} and bash your head into the tin wall. That was silly.".format(direction))
				beep_medium(1)
				return warm_stall
			elif direction.lower() == "q":
				print(exit_message)
				exit()
			elif direction.lower() == "p":
				print("\nAhhh. This is my {} now.".format(location))
				beep_slow(1)
				return warm_stall
			elif direction.lower() == "sleep":
				print("\n...zzzzzzzzzzz...".format(location))
				return warm_stall
			else:
				print("\nThat makes no sense. One to many headbutts maybe, eh?")
				beep_slow(1)
				return warm_stall
				

		#LEAP########################
		elif lol.lower() == "leap":
			beep_fast(5)
			print("\n\nYou leap bodly!!!")
			return barn_floor

		#QUIT#######################
		elif lol.lower() == "q":
			print(exit_message)
			exit()
		
		#PEE#######################
		elif lol.lower() == "p":
			print(exit_message)
			print("\nAhhh. This is my {} now.".format(location))
			beep_slow(1)
			return warm_stall		
		
		#GIBBERISH HANDLING#########
		else:
			lol = ""
			print("What? Remember you have two choices:")
			
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

	print("\n\nUp! Up! Up!\nClimbing stairs is good goat fun,\n but up here this loft looks scary and there's no hay?\n")
	
	#Lets offer some options and get input
	while lol == "":
		
		lol = input("\n\t>Look or leap? ")

		#LOOK#########################
		if lol.lower() == "look":
			
			print("\n\nLeft there is a dangerous drop to the barn floor far below.\nBackwards is the staircase back down.\nOn the right is a wall.\nForwards: another wall.")
			direction = input("\n\t>Which way to move? forwards, backwards, left, or right? ")
				
			if direction.lower() == "forwards":
				print("\n\nYou leap {} and bash your head into the tin wall. That was silly.".format(direction))
				beep_medium(1)
				return loft
			elif direction.lower() == "backwards":
				print("\nYou go {}.".format(direction))
				beep_medium(3)
				return barn_floor
			elif direction.lower() == "right":
				print("\n\nYou leap {} and bash your head into the tin wall. That was silly.".format(direction))
				beep_medium(1)
				return loft
			elif direction.lower() == "left":
				print("\nYou leap {} to your death!?!".format(direction))
				beep_fast(5)
				return death
			elif direction.lower() == "q":
				print(exit_message)
				exit()
			elif direction.lower() == "p":
				print("\nAhhh. This is my {} now.".format(location))
				beep_slow(1)
				return loft
			else:
				print("\nThat makes no sense. One to many headbutts maybe, eh?")
				return loft
			
		#LEAP########################
		elif lol.lower() == "leap":
			beep_fast(5)
			print("\n\nYou leap bodly!!!\nTo your death?!?")
			return death

		#QUIT#######################
		elif lol.lower() == "q":
			print(exit_message)
			exit()
		
		#PEE#######################
		elif lol.lower() == "p":
			print("\nAhhh. This is my {} now.".format(location))
			beep_slow(1)
			return loft		
		
		#GIBBERISH HANDLING#########
		else:
			lol = ""
			print("What? Remember you have two choices:")
	#End of Loft#



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

	while 1 == 1:
		function_next = function_next()



main()