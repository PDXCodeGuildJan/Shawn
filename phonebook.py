"""Make a phonebook using Python's dictionaries."""	

__author__= "Shawn Waldow"

import re

#Init our dictionary, which will store phone numbers.
phonebook ={} 

def main():
	"""The main driver function of our phonebook."""
	
	# Load any existing data into phonebook
	load_phonebook()

	print("Welcome to the phonebook")

	option = ""

	while option != "E":
		#Ask user what they want to do.
		option =input("You can:\n\t(A)dd\n\t(D)elete contacts\n\t(P)rint\n\t(E)xit\n\t(S)earch with name\n\tSearch by (N)umber\nWhich would you like? ")

		if option.upper() == "A":
			name = input("What is the new contact's name? ")
			number = input("What is " + name + "'s number? ")
			add_contact(name, number)
		elif option.upper() == "D":
			name = input("What contact are you removing? ")
			delete_contact(name)
		elif option.upper() == "E":
			print("Goodbye!")
			exit()
		elif option.upper() == "P":
			print_phonebook()
		elif option.upper() == "S":
			name = input("What contact do you want? ")
			search(name)
		elif option.upper() == "N":
			number = input("What number you seeking are? ")
			search_by_number(number)
		else:
			print("I'm sorry. I don't understand.")

def search(name):
	"""Find and print a contact's number"""
	if name in phonebook:
		number = phonebook[name]
		print(name, "'s number is", number, "\n")
	else:
		print("No such name.")

def search_by_number(search_number):
	"""Given the value number what is the key name?"""
	
	result = ""
	for name, number in phonebook.items():
		if search_number == number:
			print(number, " calls ", name, "\n")
			result = name
			break

	if result == "":
		print("Sorry no contact has that number.")

def add_contact(name, phonenumber):
	"""Does an addition to the phonebook with the given contact info."""
	
	#Remove lingering whitespace.
	regex = "\s+\Z"
	replace_with = ""
	scrubbed_name = re.sub(regex, replace_with, name)
	print(scrubbed_name)
	#Above incomplete

	#SCrub and reformat the phone number for (xxx) xxx-xxxx pattern
	#Remove all but numbers

	regex = "[0-9]+"
	nums = re.findall(regex, phonenumber)
	new_nums = ""
	for every_num in nums:
		new_nums += every_num

	# Introduce correct formatting

	formatted_num = "(" + new_nums[0:3] + ") " + new_nums[3:6] + "-" + new_nums[6:]
	print(formatted_num)


	phonebook[scrubbed_name] = formatted_num
	print(name, " was added with number ", formatted_num, "\n")

	#Save to hardisk
	save_phonebook()


def delete_contact(name):
	"""Removes the given contact from the Phonebook."""
	if name in phonebook:
		del phonebook[name]
		#Save to hardisk
		save_phonebook()

	else:
		print("That contact already does not exist.")



def print_phonebook():
	"""Prints every item in the phonebook dictionary. Pretty  pretty my pretty."""
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!JA JA, DAS PHONEBOOK IST GUT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

	for name in phonebook:
		print(name, "'s number is: ", phonebook[name])



def save_phonebook():
	"""Save the contents of the phonebook to a file."""
	
	# Open for reading
	open_file = open("phonebook.txt", "r")
	open_file.write(str(phonebook))
	open_file.close()



def load_phonebook():
	"""Load the phonebook data from  the save file."""

	global phonebook

	load_file = open("phonebook.txt", "a")
	phonebook_data = load_file.read()
	load_file.close()

	if phonebook_data: #Shorthand for is it empty, because eval doesn't like empty.
		# Convert from string back to dictonary.
		phonebook = eval(phonebook_data)



if __name__ == '__main__':
	main()