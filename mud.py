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

from random import randint



#Global variable for how the character feels
Feel = "capricious and impatient"
exit_message = "\nLater lazy goat!"

#Room "The barn floor."
def barn_floor():
	
	lol = "" #l.ook o.r l.eap variable initialed
	direction ="" #Direction of travel variable.
	leap_direction = "right"
	location = "barn"

	print("The musty dirt under your goat hooves smells familiar,\nbut that's all you recognize in this old barn.\nYou feel {}.".format(Feel))
	
	#Lets offer some options and get input
	while lol == "":
		
		lol = input("Look or leap? ")
		
		#LOOK#########################
		if lol.lower() == "look":
			print("Behind you is a staircase to an empty loft.\nRight is a pen filled with restless pigs.\nforwards is an open door.\nLeft is a warm stall.")
			direction = input("Which way to move? forwards, backwards, left, or right? ")
				
			if direction.lower() == "forwards":
				print("\nYou leap {}.".format(direction))
				return pasture
			elif direction.lower() == "backwards":
				print("\nYou leap {}.".format(direction))
				return loft
			elif direction.lower() == "right":
				print("\nYou leap {}.".format(direction))
				return pigs
			elif direction.lower() == "left":
				print("\nYou leap {}.".format(direction))
				return warm_stall
			elif direction.lower() == "q":
				print(exit_message)
				exit()
			elif direction.lower() == "p":
				print("\nAhhh. This is my {}".format(location))
				return barn_floor
			else:
				print("\nThat makes no sense. One to many headbutts maybe, eh?")
				return barn_floor
				



		#LEAP########################
		elif lol.lower() == "leap":
			print("You leap into a pig pen.")
			return pigs

		#QUIT#######################
		elif lol.lower() == "q":
			print(exit_message)
			exit()	
		
		#GIBBERISH HANDLING#########
		else:
			lol = ""
			print("What?")
	

def pigs():
	print("Pigs!")

def ravine():
	print("Ravine!")

def play_hill():
	print("play_hill")

def pasture():
	print("Pasture")

def warm_stall():
	print("A warm stall")

def loft():
	print("A loft")

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
	function_next()

main()