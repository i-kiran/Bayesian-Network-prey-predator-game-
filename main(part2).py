import time
import game
import math
import sheep
import random
import caveman
import visualize
from game import game_
from sheep import collision
from caveman import cmnaive
from sheep import sheepmoves
from sheep import checknearest
from visualize import recreate
from visualize import creategrid
from caveman import cmbayesian

if __name__ == "__main__":
	begin = time.time()
	print("please wait for training")
	print("..........")
	print(".....")
	#store the cpts
	x_move = {} #x_move
	y_move = {} #y_move
	ss_move = {}#ss_move
	#store the sheep's probability
	sheep_X = sheep_Y = {}
	#store the caveman1 probability
	caveman1_X = caveman1_Y = {}
	#store the caveman2 probability 
	caveman2_X = caveman2_Y = {}
	#store distance from corner
	c0 = {}
	#store distance from caveman 1
	c1 = {}
	#store distance from caveman2
	c2 = {}
	iter = 0
	n = 8 # size of maze
	for itr in range(500):
		start = game_()
		for i in range(50):
			iter += 1
			caveman1_x = start.caveman1[0]
			caveman1_y = start.caveman1[1]
			caveman2_x = start.caveman2[0]
			caveman2_y = start.caveman2[1]
			sx = start.sheep[0]
			sy = start.sheep[1]
			c_0 = int(checknearest(start.sheep))
			c_1 = int(math.dist(start.sheep, start.caveman1))
			c_2 = int(math.dist(start.sheep, start.caveman2))
			if str(sx) in sheep_X :
				sheep_X[str(sx)] = sheep_X[str(sx)]+1
			else:
				sheep_X[str(sx)] = 1

			if str(sy) in sheep_Y:
				sheep_Y[str(sy)] = sheep_Y[str(sy)]+1
			else:
				sheep_Y[str(sy)] = 1
			
			if str(caveman1_x) in caveman1_X:
				caveman1_X[str(caveman1_x)] = caveman1_X[str(caveman1_x)]+1
			else:
				caveman1_X[str(caveman1_x)] = 1
			
			if str(caveman1_y) in caveman1_Y:
				caveman1_Y[str(caveman1_y)] = caveman1_Y[str(caveman1_y)]+1
			else:
				caveman1_Y[str(caveman1_y)] = 1
			
			if str(caveman2_x) in caveman2_X:
				caveman2_X[str(caveman2_x)] = caveman2_X[str(caveman2_x)]+1  
			else:
				caveman2_X[str(caveman2_x)] = 1

			if str(caveman2_y) in caveman2_Y:
				caveman2_Y[str(caveman2_y)] = caveman2_Y[str(caveman2_y)]+1  
			else:
				caveman2_Y[str(caveman2_y)] = 1

			if str(c_0) in c0:
				c0[str(c_0)] = c0[str(c_0)]+1  
			else: 
				c0[str(c_0)] = 1
			
			if str(c_1) in c1:
				c1[str(c_1)] = c1[str(c_1)]+1  
			else:
				c1[str(c_1)] = 1
			
			if str(c_2) in c2:
				c2[str(c_2)] = c2[str(c_2)]+1
			else:
				c2[str(c_2)] = 1
			
			
			caveman1 = cmnaive(start, 1)
			caveman2 = cmnaive(start, 2, caveman1)
			sheep = sheepmoves(start, caveman1, caveman2)
			start.newposition(caveman1,caveman2,sheep[0])			
			
			x_move_key = str(sx)+str(caveman1_x)+str(caveman2_x)
			y_move_key = str(sy)+str(caveman1_y)+str(caveman2_y)
			ss_move_key = str(sx)+str(sy)+str(c_0)+str(c_1)+str(c_2)

			
			#updating CPT
			if 'w' in sheep[1]: #left
				if x_move_key+'w' in x_move:
					x_move[x_move_key+'w'] = x_move[x_move_key+'w']+1  
				else:
					x_move[x_move_key+'w'] = 1
			elif 'e' in sheep[1]: #right
				if x_move_key+'e' in x_move:
					x_move[x_move_key+'e'] = x_move[x_move_key+'e']+1  
				else:
				 	x_move[x_move_key+'e'] = 1
			
			if 'n' in sheep[1]: #up
				y_move[y_move_key+'n'] = y_move[y_move_key+'n']+1 if y_move_key+'n' in y_move else 1
			elif 's' in sheep[1]: #down
				y_move[y_move_key+'s'] = y_move[y_move_key+'s']+1 if y_move_key+'s' in y_move else 1
				
			if sheep[1] == 'stay': #0 step
				if ss_move_key+'0' in ss_move:
					ss_move[ss_move_key+'0'] = ss_move[ss_move_key+'0']+1 
				else:
					ss_move[ss_move_key+'0'] = 1
			else:
				if ss_move_key+str(len(sheep[1])//2) in ss_move:
					ss_move[ss_move_key+str(len(sheep[1])//2)] = ss_move[ss_move_key+str(len(sheep[1])//2)]+1 
				else:
				 	ss_move[ss_move_key+str(len(sheep[1])//2)] =1
			
			if collision(caveman1,caveman2,sheep[0]):
				break
	
	#update all CPTs
	for key in x_move:
		x_move[key] = x_move[key]/iter/(sheep_X[key[0]]/iter)/(caveman1_X[key[1]]/iter)/(caveman2_X[key[2]]/iter)
	for key in y_move:
		y_move[key] = y_move[key]/iter/(sheep_Y[key[0]]/iter)/(caveman1_Y[key[1]]/iter)/(caveman2_Y[key[2]]/iter)
	for key in ss_move:
		ss_move[key] = ss_move[key]/iter/(sheep_X[key[0]]/iter)/(sheep_Y[key[1]]/iter)/(c0[key[2]]/iter)/(c1[key[3]]/iter)/(c2[key[4]]/iter)
		
	delay = 0.1
	grid, rect, screen, wid = creategrid(n)
	for i in range(5):
		print('Game ',i+1,':')
		start = game_()
		win = False
		o = 50
		t = 0
		for i in range(o):
			sx = str(start.sheep[0])
			sy = str(start.sheep[1])
			caveman1_x = str(start.caveman1[0])
			caveman1_y = str(start.caveman1[1])
			caveman2_x = str(start.caveman2[0])
			caveman2_y = str(start.caveman2[1])
			c_0 = str(int(checknearest(start.sheep)))
			c_1 = str(int(math.dist(start.sheep, start.caveman1)))
			c_2 = str(int(math.dist(start.sheep, start.caveman2)))
			
			ss_move_key = sx+sy+c_0+c_1+c_2
			x_move_key = sx+caveman1_x+caveman2_x
			y_move_key = sy+caveman1_y+caveman2_y
		
			step = 0
			if ss_move_key+'0' in ss_move:
				prob = ss_move[ss_move_key+'0']
			else:
				prob = 0
			if ss_move_key+'1' in ss_move:
				if prob < ss_move[ss_move_key+'1']:
					step = 1
					prob = ss_move[ss_move_key+'1']
			if ss_move_key+'2' in ss_move:
				if prob < ss_move[ss_move_key+'2']:
					step = 2
				
			if step > 0:
				d_x = 'w'
				if x_move_key+'w' in x_move:
					prob = x_move[x_move_key+'w']
				else:
						prob = 0
				
				if x_move_key+'e' in x_move:
					if prob < x_move[x_move_key+'e']:
						d_x = 'e'
						prob = x_move[x_move_key+'e']
				prob = 0
				
				if y_move_key+'n' in y_move:
					prob = y_move[y_move_key+'n']
				else:
					prob = 0

				if y_move_key+'s' in y_move:
					if prob < y_move[y_move_key+'s']:
						d_y = 's'
					
			ps = start.sheep	#predicted sheep move
			if step > 0:
				if d_x == 'w':
					ps = (ps[0]-step,ps[1])
				else: 
					ps = (ps[0]+step,ps[1])

				if d_x == 'n':
					ps = (ps[0],ps[1]-step)
				else:
					ps = (ps[0],ps[1]+step)
					

			new_n = random.randint(1,100)
			if new_n < 80:
				caveman1 = cmbayesian(start, ps)
			else:
				caveman1 = cmnaive(start, 1)
			
			caveman2 = cmnaive(start, 2, caveman1)
			
			sheep = sheepmoves(start, caveman1, caveman2)
			
			start.newposition(caveman1,caveman2,sheep[0])
			
			recreate(grid, rect, screen, 8, start.game_ , delay, wid)
			
			if collision(caveman1,caveman2,sheep[0]):
				print('Winner : Caveman')
				t = 1
				end = time.time()
				print(end- begin)
				break
		if (t==0):
			print('Winner : Sheep')
			end = time.time()
			print(end- begin)
		