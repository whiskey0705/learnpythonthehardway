"""
### 王子大战外星人，营救公主 ###
1. Person()
		Prince()
		Princess()
		Alien()

2. Game()
		Rock-Paper-Scissors


"""
from random import randint
from sys import exit
GAME = ['Rock', 'Paper', 'Scissors']

class Person(object):
	def __init__(self, name):
		self.name = name

	def speak(self):
		print(f"I'm {self.name}")

# per = Person('whiskey')
# per.speak()

class Prince(Person):
	def __init__(self, tall, name):
		self.tall = tall
		super().__init__(name)

	def taunt(self):
		self.speak()
		print(f"I'm {self.tall}cm tall, You son of bitch!!!")

# pr = Prince(200, 'snk')
# print(pr.tall)
# pr.taunt()

class Princess(object):
	def __init__(self, hair, name):
		self.person = Person(name)
		self.hair = hair

	def buff_up(self):
		self.person.speak()
		print(f"I have {self.hair} hair, Actually I love Alien!")

# pcess = Princess('gold', 'lina')
# print(pcess.hair)
# pcess.buff_up()

class Alien(object):
	def __init__(self, weight, name):
		self.person = Person(name)
		self.weight = weight

	def choose(self):
		self.person.speak()
		choice = GAME[randint(0, 2)]
		print(f'My choice is {choice}, I have {self.weight}kg weight and I will kill you!!!')
		return choice


# aen = Alien(400, 'J8')
# print(aen.person.name)
# aen.choose()

class Game(object):
	def __init__(self, player1, player2, player3):
		self.player1 = player1
		self.player2 = player2
		self.player3 = player3

	def play(self):
		print(f'Welcome, {self.player1.name} and {self.player2.person.name}! Please introduce yourself')
		self.player1.taunt()
		print(f'Make your decision, my warrior {self.player1.name}')
		print('#' * 20)
		decision = input('Enter your decision >\n')
		print(f'Warrior choose {decision}')
		print('#' * 20)
		count = 3
		print(f'And your turn {self.player2.person.name}')

		choice = self.player2.choose() # 函数赋值的同时，函数已经执行

		while count > 1 :
			count = count - 1
			print(f'You only have {count} chance')
			decision = input('Enter your decision >\n')

		# if 和 上面的 while同级（一样的缩进）

		if decision == 'Rock' and choice == 'Scissors':
			print ('You win!')
			exit(0)
		elif decision == 'Scissors' and choice == 'Paper':
			print ('You win!')
			exit(0)
		elif decision == 'Papper' and choice == 'Rock':
			print ('You win!')
			exit(0)
		else:
			print('Warrior, you lose. wait!!!! Here comes our princess!!!')
			self.player3.buff_up()
			


# pom = Prince(200, 'pom')
# lina = Princess('gold', 'lina')
# snk = Alien(400, 'snk')



# game = Game(pom, snk, lina)
# game.play()
