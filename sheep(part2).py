import math
def checknearest(vector):
	if (vector[0] < 5):
		x_cood = 1
	else:
		x_cood = 8

	if (vector[1] < 5):
		y_cood = 1
	else:
		y_cood = 8
	d = math.dist(vector , [x_cood,y_cood])
	return d

def sheepmoves(start, caveman1, caveman2):
	s = start.sheep
	v1 = start.caveman1
	move = 'still'	
	if math.dist(v1,s) > 8 and math.dist(start.caveman2,s) > 8 and s!=caveman1 and s !=caveman2:
		val = [s,move]
		return val 
	sum = 0
	flag = checknearest((s[0]-1,s[1]-1))**0.5 + math.dist(v1,(s[0]-1,s[1]))**0.5 + math.dist(start.caveman2,(s[0]-1,s[1]))**0.5
	if flag > sum and s[0]-1 > 0 and s[1]-1 > 0:
		sum = flag
		move = 'westnorth'
		vector = (s[0]-1,s[1]-1)
	flag = checknearest((s[0]-2,s[1]-2))**0.5 + math.dist(v1,(s[0]-1,s[1]))**0.5 + math.dist(start.caveman2,(s[0]-1,s[1]))**0.5
	if flag > sum and s[0]-2 > 0 and s[1]-2 > 0:
		sum = flag
		move = 'west2north2'
		vector = (s[0]-2,s[1]-2)
	flag = checknearest((s[0]-1,s[1]+1))**0.5 + math.dist(v1,(s[0]-1,s[1]))**0.5 + math.dist(start.caveman2,(s[0]-1,s[1]))**0.5
	if flag > sum and s[0]-1 > 0 and s[1]+1 < 9:
		sum = flag
		move = 'westsouth'
		vector = (s[0]-1,s[1]+1)
	flag = checknearest((s[0]-2,s[1]+2))**0.5 + math.dist(v1,(s[0]-1,s[1]))**0.5 + math.dist(start.caveman2,(s[0]-1,s[1]))**0.5
	if flag > sum and s[0]-2 > 0 and s[1]+2 < 9:
		sum = flag
		move = 'west2south2'
		vector = (s[0]-2,s[1]+2)
	flag = checknearest((s[0]+1,s[1]-1)) + math.dist(v1,(s[0]-1,s[1])) + math.dist(start.caveman2,(s[0]-1,s[1]))
	if flag > sum and s[0]+1 < 9 and s[1]-1 > 0:
		sum = flag
		move = 'eastnorth'
		vector = (s[0]+1,s[1]-1)
	flag = checknearest((s[0]+2,s[1]-2)) + math.dist(v1,(s[0]-1,s[1])) + math.dist(start.caveman2,(s[0]-1,s[1]))
	if flag > sum and s[0]+2 < 9 and s[1]-2 > 0:
		sum = flag
		move = 'east2north2'
		vector = (s[0]+2,s[1]-2)
	flag = checknearest((s[0]+1,s[1]+1)) + math.dist(v1,(s[0]-1,s[1])) + math.dist(start.caveman2,(s[0]-1,s[1]))
	if flag > sum and s[0]+1 < 9 and s[1]+1 < 9:
		sum = flag
		move = 'eastsouth'
		vector = (s[0]+1,s[1]+1)
	flag = checknearest((s[0]+2,s[1]+2)) + math.dist(v1,(s[0]-1,s[1])) + math.dist(start.caveman2,(s[0]-1,s[1]))
	if flag > sum and s[0]+2 < 9 and s[1]+2 < 9:
		sum = flag
		move = 'east2south2'
		vector = (s[0]+2,s[1]+2)
	val = [vector, move] 
	return val


def collision(caveman1,caveman2,sheep):
	if (abs(caveman1[0] - sheep[0]) + abs(caveman1[1] - sheep[1]) == 1) or (abs(caveman2[0] - sheep[0]) + abs(caveman2[1] - sheep[1]) == 1):
		return True
	return False

