"""A phonebookprogram implemented with classes."""

__author__ = "Shawn Waldow"

import re

class Contact:
	"""Defines the contact object to store info about people."""

	def __init__(self, f_name, l_name):
		"""Doc strings for init funcs not necesarry."""
		self.first_name = f_name
		self.last_name = l_name
		self.phone_num = ""
		self.addresses = {}
		self.email = ""


	def update_address(	self, addy_key, street=None, unit=None, city=None, 
						state=None, zip_code=None, country=None):
		"""Update the address at addy_key with the info passed."""
		
		#Check to see if you have an address with that key already.
		if addy_key in self.addresses:
			temp_address = self.addresses[addy_key]
		else:
			# Make a new Address object
			temp_address = Address()
		
		if street:
			temp_address.street = street
		if unit:
			temp_address.unit = unit
		if city:
			temp_address.city = city
		if state:
			temp_address.state = state
		if zip_code:
			temp_address.zip_code = zip_code
		if country:
			temp_address.country = country

		self.addresses[addy_key] = temp_address


	def format_phone_num(self, phone_num):
		"""Format the number all pretty."""
		#Scrub and reformat the phone number for (xxx) xxx-xxxx pattern
		#Remove all but numbers

		regex = "[0-9]+"
		nums = re.findall(regex, phone_num)

		#Take every thing in the list of numbers and make it into a str of nums
		new_nums = ""
		for every_num in nums:
			new_nums += every_num

		# Introduce correct formatting

		formated_num = "(" + new_nums[0:3] + ") " + new_nums[3:6] + "-" + new_nums[6:]
		
		#Save formated number to contact
		self.phone_num = formated_num


	def __str__(self):
		"""Print out the contact's info prettily."""

		# Initialize formated string
		formated_str = "{0} {1}".format(self.first_name, self.last_name)

		#If theres a phone number
		if self.phone_num:
			#Format the phone number
			self.format_phone_num(self.phone_num)
			# Add the pretty phone number to the formated string
			formated_str += "\nPhone: {0}".format(self.phone_num)

		#If there is an email
		if self.email:
			formated_str += "\nEmail: {}".format(self.email)

		#Are there addresses?
		if self.addresses:
			formated_str += "\nAddresses:"
			formated_str += "\n----------------------------------"
			#Loop through all the  adresses and print them
			for key, address in self.addresses.items():
				formated_str += "\n{}:".format(key)
				formated_str += "\n{}:".format(str(address))
				formated_str += "\n----------------------------------"

		return formated_str

class Address:
	"""Defines the Address object to be used with Contact."""

	def __init__(self):

		self.street = ""
		self.unit = ""
		self.city = ""
		self.state = ""
		self.zip_code = ""
		self.country = ""

	def __str__(self):
		"""Print out the address, formated prettily. __str__ makes is defualt
		for print."""

		formated_str =''
		formated_str += self.street

		if self.unit != "":
			formated_str += "\n" + self.unit
		
		formated_str += "\n" + self.city + " " + self.state
		formated_str += " " + self.zip_code
		formated_str += "\n" + self.country

		return formated_str

def main():

	jim = Contact("Jim", "Jones")
	jim.phone_num = "3332224444"
	jim.email = "JJ@koolaid.com"
	jim.update_address("Home", city = "Loopyville")
	jim.update_address("Work", city = "Hometown")
	print(jim)

if __name__ == "__main__":
	main()
















