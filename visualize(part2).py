import time
import tkinter as Mazegame
from tkinter import ttk, Canvas, Label  
def creategrid(n):
    size = 500

    cell_width = int(size/n)
    cell_height = int(size/n)

    screen = Mazegame.Tk()
    screen.title("SHEEP vs CAVEMEN")
    grid = Canvas(screen, width = cell_width*n, height = cell_height*n, highlightthickness=0)
    grid.pack(side="top", fill="both", expand="true")

    rect = {}
    for col in range(n):
        for row in range(n):
            x1 = col * cell_width
            y1 = row * cell_height
            x2 = x1 + cell_width
            y2 = y1 + cell_height
            rect[row, col] = grid.create_rectangle(x1,y1,x2,y2, fill="red", tags="rect")
    return grid, rect, screen, cell_width

def recreate(grid, rect, screen, n, maze, delay, wid):
    for i in range(n):
        for j in range(n):
            item_id = rect[i,j]
            if maze[i][j] == 0:                      # positions where lion can move
                grid.itemconfig(item_id, fill="light green")
            elif maze[i][j] == 1:                       # blocked positions/walls
                grid.itemconfig(item_id, fill="light blue")
            elif maze[i][j] == 2:                      # positions visited    
                grid.itemconfig(item_id, fill="blue")
            elif maze[i][j] == 3:
                grid.itemconfig(item_id, fill="black")

    #load_img(size, path2, end)
    screen.update_idletasks()
    screen.update()
    time.sleep(delay)
    return

