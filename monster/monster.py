from creature import Creature

class Monster(Creature):

	AGGRO = "aggressive"
	DEFENSE = "defensive"

	def __init__(self):
		super(Monster, self).__init__()

		self.personality = Monster.AGGRO
		self.health = 20