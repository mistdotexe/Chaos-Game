from random import *
import time
import math
import matplotlib.pyplot as plt
import numpy as np

#number of points to draw in chaos game
num_points = 500000
point_cloud = [np.array([]) for i in range(num_points)]

N = 5
verts = [np.array([math.sin(2*math.pi*t/N), math.cos(2*math.pi*t/N)]) for t in range(N)]
r_opt=4/7
current_point = verts[0]

def lerp(a: np.array,b: np.array,t: float) -> list:
    return (1-t)*a + t*b


choice_weights = [0]+[1 for i in range(N-1)]
#choice_weights = choice_weights[2:] + choice_weights[:2]
print(choice_weights)
def choose_next(r: int) -> int:
    L = [i for i in range(0,len(verts))]
    L = L[r:] + L[:r]
    choice = choices(L, choice_weights, k=1)[0]
    return choice


prev_r = 0
# Draws all points in fractal
for i in range(num_points):
    point_cloud[i] = current_point
    r = choose_next(prev_r)
    #w.create_line(current_point,verts[r])
    current_point = lerp(current_point, verts[r], t = r_opt)
    prev_r = r

point_cloud = np.transpose(point_cloud)
plt.figure(figsize=(8, 6)) # Adjust figure size for better viewing
plt.scatter(point_cloud[0], point_cloud[1], s=1, c='green', alpha=1, marker='.')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()


