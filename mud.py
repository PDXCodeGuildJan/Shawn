#Pseudocode for program loop
#room we are in
#opening room statement
#cue to look or go
#look
#go
#room statement
#loop

#Global variable for how the character feels
Feel = "capricious and impatient"


#Room "The barn floor."
def barn_floor():
	
	lol = "" #l.ook o.r l.eap variable initialed
	direction ="" #Direction of travel variable.
	
	print("The musty dirt under your goat hooves smells familiar,\nbut that's all you recognize.\nYou feel {}.".format(Feel))
	
	#Lets offer some options and get input
	while lol == "":
		
		lol = input("Look or leap? ")
		
		if lol.lower() == "look":
			print("Behind you is a staircase to an empty loft.\nRight is a pen filled with restless pigs.\nAhead is an open door.\nLeft is a warm stall.")
			direction = input("Ahead, behind, left, or right? ")
			print("You move {}.".format(direction))
			exit()

		elif lol.lower() == "leap":
			print("You leap into a pig pen.")
			return pigs

		elif lol.lower() == "q":
			exit()	
		
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
	print("\n\nYou are lucky. You don't use punctuation. You are a goat.\nYou know your 'q' to quit.")
	print( """	                         //  
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



def main():
	intro()
	function_next = barn_floor()
	function_next()

main()