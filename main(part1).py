import tkinter as Mazegame
from tkinter import ttk, Canvas, Label
import random
import time
import math
import game
import visualize
import sheep
import caveman
from caveman import collision
from caveman import cm_moves
from game import game_
from sheep import sheep_moves
from sheep import check_nearest
from visualize import create_grid
from visualize import redraw_maze
if __name__ == "__main__":
	begin = time.time()
	t = 0.2
	grid, rect, screen, wid = create_grid()
	start = game_()
	iter =30
	for a in range(iter):
		cm1 = 1
		cm2 = 2
		caveman1_point = cm_moves(start, cm1)
		caveman2_point = cm_moves(start, cm2, caveman1_point[0])
		sheep = sheep_moves(start, caveman1_point[0], caveman2_point[0])
		redraw_maze(grid, rect, screen, start.game_, t, wid)
		if collision(caveman1_point[0],caveman2_point[0],sheep[0]):
			print('winner : Caveman')
			end = time.time()
			print(end- begin)
			print("+++++++++++++++++")
			exit()
		start.newposition(caveman1_point[1],caveman2_point[1],sheep[1])
	print('Winner : Sheep')
	end = time.time()
	print(end- begin)