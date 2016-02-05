from creature import Creature
from monster import Monster

class Hero(Creature):


	def __init__(self):
		super(Hero, self).__init__()

		self.level = 1
		self.health = 20



class MonsterHero(Hero, Monster):

	def __init__(self):

		Hero.__init__(self)
		Monster.__init__(self)


		self.where = "on shoulders"


def main():

	mae=Hero()
	shawn=Monster()
	two_heads = MonsterHero()
	print(two_heads.health)
	print(two_heads.where)

main()