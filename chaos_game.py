#import numpy as np
from tkinter import *
from random import *
import time
#number of points to draw in chaos game
num_points = 50000

verts = [[ 50,  50],
         [950,  50],
         [ 50, 950],
         [950, 950]]

current_point = [250,250]

def lerp(a: list,b: list,t: float) -> list:
    return [(1-t)*a_k + t*b_k for a_k,b_k in zip(a,b)]

def draw_point(p: list ,r: float):
    w.create_oval(p[0]-r, p[1]-r, p[0]+r, p[1]+r, fill="#000000")


choice_weights = [0,1,0.5,1]
cum_choice_weights = [sum(choice_weights[:i]) for i in range(1,len(choice_weights)+1)]
print(cum_choice_weights)
def choose_next(r: int) -> int:
    L = [i for i in range(0,len(verts))]
    L = L[r:] + L[:r]
    choice = choices(L, cum_weights=cum_choice_weights, k=1)[0]
    return choice


canvas_width = 1000
canvas_height = 1000
master = Tk()
master.title("Points")
w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack(expand=NO, fill=BOTH)

# Draws verticies
for p in verts:
    w.create_oval(p[0]-3, p[1]-3, p[0]+3, p[1]+3, fill="#FF0000")



prev_r = 0
# Draws all points in fractal
for i in range(num_points):
    draw_point(current_point, 0)
    
    r = choose_next(prev_r)
    current_point = lerp(current_point, verts[r], t = 1/3)
    prev_r = r


mainloop()

