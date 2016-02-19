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
		self.attack_points = 2
		self.weapon = None
		self.special_abil = {}
		self.stats = {}

	def attack(self):
		"""Returns attack value given creature's base, weapon, and state."""
		atk_value = self.attack_points
		if self.weapon:
			atk_value = self.attack_points + self.weapon.base_damage
		return atk_value

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


class Weapon:
	"""weapon creatures can eqip"""

	def __init__(self, atk_value):
		self.base_damage = atk_value