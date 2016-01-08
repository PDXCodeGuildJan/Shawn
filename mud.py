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
	
	lol = "" #l.ook o.r l.eap
	
	print("The musty dirt under your goat hooves smells familiar,\nbut that's all you recognize.\nYou feel {}.".format(Feel))
	
	#Lets offer some options and get input
	while lol == "":
		lol = input("Look or leap? ")
		if lol.lower() == "look":
			print("Wow!")
		elif lol.lower == "leap":
			print("Ouch!")
		elif lol.lower == "q":
			exit()	
		else:
			lol = ""
			print("What?")
	


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
	barn_floor()

main()