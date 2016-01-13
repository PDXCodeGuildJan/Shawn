#hangman.py
# A program about hanging people if you don't spell things correctly.

from random import randint

words = ["oplopanax", "club", "unctuous", "ragnorok", "piste", "sambucus", "amanita"]
numWrong = 0
listedWord = [None]

# A function that starts and plays the hangperson game.
# Users can be wrong a maximum of 5 times before they lose,
# the 6th wrong guess triggering Game Over.
def hangperson():
   global listedWord


   # Greet the user
   print("Howdy! We gonna hang us some 50 cent words!")

   # Randomly select a word from the list of words
   random_word_index = randint(0, len(words)-1)

   # Make the randomly selected word into a list object
   a_string = words[random_word_index]
   listedWord = list(a_string)
   currentState = ""
   len_listedWord = len(listedWord)
   
   # Make another list the same length as the word, but with
   # '_' instead of letters. This will track the user's progress.
   # Use the variable name currentState
   
   currentState = "_" * len_listedWord
   currentState = list(currentState)

   #Initialize var to store incorrect guesses. 
   incorrect = []
   len_currentState = len(currentState)
   
   # Print the initial state of the game
   printHangperson(currentState, incorrect)

   # Start the game! Loop until the user either wins or loses
   while currentState != listedWord and numWrong < 6:

      bundled_list = updateState(userGuess(), currentState, incorrect)
      currentState = bundled_list[0]
      incorrect = bundled_list[1]

      printHangperson(currentState, incorrect)

   # Determine if the user won or lost, and then tell them accordingly

   if currentState == listedWord:
      print("win")
   else:
      print("You Lost")
      print(listedWord)




# Update the state of the game based on the user's guess.
#
# guess: a character guessed by the user
# currentState: the current state of the word/game
#
# return currentState
def updateState(guess, currentState, incorrect):
   global numWrong
   # First, determine if the letter guessed is in the word.
   numInWord = listedWord.count(guess)
   
   # If it isn't, tell the user and update the numWrong var
   if numInWord == 0:
      print("\nThe rope tightens!\n")
      numWrong += 1
      incorrect.append(guess)
    
   # If it is, congratulate them and update the state of the game.
   elif numInWord > 0:
      print("Good guess!")
   #    To update the state, make sure to replace ALL the '_' with guess """
      numInCurrent = 0
      counter = 0
      while numInWord > numInCurrent:
   #    Insert the guessed letter.
         if listedWord[counter] == guess:
            currentState[counter] = guess
            counter += 1
            numInCurrent = currentState.count(guess)
         else:
            counter +=1 


   else:
      print("\nError in starting in updateState()\n")
      exit()

   return [currentState, incorrect]


# This helpful function prompts the user for a guess,
# accepting only single letters.
# 
#
# returns a letter
def userGuess():
   guess = input("Guess a letter in the word! (Say 'exit' to stop playing) ")
   while len(guess) != 1:
      if guess.lower() == "exit":
         exit()
      else:
         guess = input("That's not a single letter?! Guess a letter in the word! (Say 'exit' to stop playing) ") ####DO MORE ERROR HANDLING

   return guess.lower()

################# DO NOT EDIT BELOW THIS LINE ##################

# A helpful function to print the hangman.
# DO NOT CHANGE
#
# state: current state of the word
def printHangperson(state, incorrect):
   person = [" O "," | \n | ", "\| \n | ", "\|/\n | ", "\|/\n | \n/  ", "\|/\n | \n/ \\"]
   print()

   if numWrong > 0:
      print(person[0])

   if numWrong > 1:
      print(person[numWrong-1])

   print("\n\n")

   for i in state:
      print(i, end=" ")

   print("\n")

   print("Incorrect guesses {}:".format(incorrect))
   print("")
# This line runs the program on import of the module
hangperson()
