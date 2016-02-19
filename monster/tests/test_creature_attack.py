__author__ = "Shawn Waldow"

import unittest

# Import the class where the function lives that you're testing

from creature import Creature, Weapon

# Make a new TestCase, CreatureAttackTest, which inherit's from unittest.TestCase
class CreatureAttackTest(unittest.TestCase): 

	def setUp(self):
		"""Required."""
		self.creature = Creature()

	def tearDown(self):
		"""Required."""
		del self.creature

	"""Do we get an int returned? Without weapon do wedo base damage? With weapon do we do expected damage? When weakend do we do 1/2 damage? Same for weapon?"""

	def test_attack_return_int(self):

		#Call and catch
		value = self.creature.attack()

		#use python's assertIs to make sure the value is an integer
		self.assertIsInstance(value, int, "Returned attack value is not an int.")

	def test_no_weapon_return_base_damage(self):
		"""Ensure a weaponless creature does only base damage."""

		self.creature.attack_points = 2

		value = self.creature.attack()

		self.assertEqual(value, 2, "Excepted base attack value not given")

	def test_with_weapon_return_damage(self):
		"""Ensure that with a weapon the creature does the base damage + weapon damage."""

		# Make a weapon
		weapon = Weapon(3)
		# Give it
		self.creature.weapon = weapon
		# Set base attack
		self.creature.attack_points = 3
		# Get total attack value
		an_attack = self.creature.attack()
		# Assert the attack value is base + weapon
		self.assertEqual(an_attack, 6, "Expected attack value wrong.")

