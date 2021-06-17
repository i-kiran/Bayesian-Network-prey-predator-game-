import tkinter as Mazegame
from tkinter import ttk, Canvas, Label
import random
import time
def create_grid():
	sc = Mazegame.Tk()
	sc.title("GAME - SHEEP VS CAVEMAN")
	size = int(460/8)
	cell_width = size
	cell_height = size
	grid = Canvas(sc, width = cell_width*8, height = cell_height*8, highlightthickness=0)
	grid.pack(side="top", fill="both", expand="true")
	rect = {}
	for col in range(8):
		for row in range(8):
			x1 = col * cell_width
			y1 = row * cell_height
			x2 = x1 + cell_width
			y2 = y1 + cell_height
			rect[row, col] = grid.create_rectangle(x1,y1,x2,y2, fill="red", tags="rect")
	return grid, rect, sc, cell_width

def redraw_maze(grid, rect, screen, maze, t, wid):
    grid.itemconfig("rect", fill="green")
    for i in range(8):
        for j in range(8):
            item_id = rect[i,j]
            if maze[i][j] == 0:                      
                grid.itemconfig(item_id, fill="green")
            elif maze[i][j] == 1:                       
                grid.itemconfig(item_id, fill="black")
            elif maze[i][j] == 2:                        
                grid.itemconfig(item_id, fill="black")
            elif maze[i][j] == 3:
                grid.itemconfig(item_id, fill="white")

    screen.update_idletasks()
    screen.update()
    time.sleep(t)
    return
