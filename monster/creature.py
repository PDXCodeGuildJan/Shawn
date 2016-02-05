"""Defines the Creature class, the base of all living things in our game."""

class Creature:

	# Constants for the states of creatures
	NORMAL = "normal"
	ASLEEP = "asleep"
	UNCONS = "unconscious"
	POISONED = "poisoned"
	WEAKENED = "weakened"

	def __init__(self):

		self.name =""
		self.state = Creature.NORMAL
		self.health = 20
		self.max_health = 20
		self.attack = 2
		self.weapon = None
		self.special_abil = {}
		self.stats = {}

	def attack(self):

		pass

	def heal(self, amount):

		pass

	def defend(self, amount):

		pass

	def take_damage(self, damage):

		pass

	def change_weapon(self, new_weapon):

		pass

	def change_state(self, new_state):

		pass


