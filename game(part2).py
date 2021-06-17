import random

class game_:

	def __init__(self):
		self.caveman1 = (random.randint(1,8),random.randint(1,8)) 
		x = random.randint(1,8)
		y = random.randint(1,8)
		while self.caveman1 == (x,y):
			x = random.randint(1,8)
			y = random.randint(1,8)
		self.caveman2 = (x,y)
		x = random.randint(1,8)
		y = random.randint(1,8)
		while self.caveman1 == (x,y) or self.caveman2 == (x,y):
			x = random.randint(1,8)
			y = random.randint(1,8)
		self.sheep = (x,y)
		self.game_ = []
		for i in range(8):
			x = []
			for j in range(8):
				x.append(0) 
			self.game_.append(x) 
		
		self.game_[self.caveman1[0]-1][self.caveman1[1]-1] = 1
		self.game_[self.caveman2[0]-1][self.caveman2[1]-1] = 2
		self.game_[self.sheep[0]-1][self.sheep[1]-1] = 3

	def newposition(self,caveman1,caveman2,sheep):
		self.caveman1 = caveman1
		self.caveman2 = caveman2
		self.sheep = sheep
		self.game_ = []
		for i in range(8):
			x = []
			for j in range(8):
				x.append(0) 
			self.game_.append(x) 		
		self.game_[self.caveman1[0]-1][self.caveman1[1]-1] = 1
		self.game_[self.caveman2[0]-1][self.caveman2[1]-1] = 2
		self.game_[self.sheep[0]-1][self.sheep[1]-1] = 3
