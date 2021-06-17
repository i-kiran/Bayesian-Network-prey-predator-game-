import random

def generate_random():
	return random.randint(1,8)

class game_:
	caveman1_point = (generate_random(),generate_random()) 
	pt1 = (generate_random(),generate_random())  
	i1 , j1 = pt1
	while caveman1_point == pt1:
		i1 = generate_random()
		j1 = generate_random()
	caveman2_point = i1,j1
	pt2 = (generate_random(),generate_random())
	i2 , j2 = pt2
	while caveman1_point == pt1 or caveman2_point == pt2:
		i2 = generate_random()
		j2 = generate_random()
	sheep = (i2,j2)
	
	def __init__(self):
		self.game_ = []
		for i in range(8):
			x = []
			for j in range(8):
				x.append(0) 
			self.game_.append(x) 
		p1 = self.caveman1_point[0]-1
		p2 = self.caveman1_point[1]-1
		p11 = self.caveman2_point[0]-1
		p22 = self.caveman2_point[1]-1
		p111 = self.sheep[0]-1
		p222 = self.sheep[1]-1
		self.game_[p1][p2] = 1
		self.game_[p11][p22] = 2
		self.game_[p111][p222] = 3

	def newposition(self,caveman1_move,caveman2_move,sheep_move):
		self.caveman1_point = (self.caveman1_point[0]-1,self.caveman1_point[1]) if caveman1_move == 'west' else (self.caveman1_point[0]+1,self.caveman1_point[1]) if caveman1_move == 'east' else (self.caveman1_point[0],self.caveman1_point[1]-1) if caveman1_move == 'north' else (self.caveman1_point[0],self.caveman1_point[1]+1) if caveman1_move == 'south' else self.caveman1_point
		self.caveman2_point = (self.caveman2_point[0]-1,self.caveman2_point[1]) if caveman2_move == 'west' else (self.caveman2_point[0]+1,self.caveman2_point[1]) if caveman2_move == 'east' else (self.caveman2_point[0],self.caveman2_point[1]-1) if caveman2_move == 'north' else (self.caveman2_point[0],self.caveman2_point[1]+1) if caveman2_move == 'south' else self.caveman2_point
		self.sheep = (self.sheep[0]-1,self.sheep[1]-1) if sheep_move == 'westnorth' else (self.sheep[0]-1,self.sheep[1]+1) if sheep_move == 'westsouth' else (self.sheep[0]+1,self.sheep[1]-1) if sheep_move == 'eastnorth' else (self.sheep[0]+1,self.sheep[1]+1) if sheep_move == 'eastsouth' else (self.sheep[0]-2,self.sheep[1]-2) if sheep_move == 'west2north2' else (self.sheep[0]-2,self.sheep[1]+2) if sheep_move == 'west2south2' else (self.sheep[0]+2,self.sheep[1]-2) if sheep_move == 'east2north2' else (self.sheep[0]+2,self.sheep[1]+2) if sheep_move == 'east2south2' else self.sheep
		self.game_ = []
		for i in range(8):
			x = []
			for j in range(8):
				x.append(0) 
			self.game_.append(x) 
		p1 = self.caveman1_point[0]-1
		p2 = self.caveman1_point[1]-1
		p11 = self.caveman2_point[0]-1
		p22 = self.caveman2_point[1]-1
		p111 = self.sheep[0]-1
		p222 = self.sheep[1]-1
		self.game_[p1][p2] = 1
		self.game_[p11][p22] = 2
		self.game_[p111][p222] = 3
	
