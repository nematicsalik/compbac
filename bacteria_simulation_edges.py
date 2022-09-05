import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
from tqdm import tqdm

# import cv2
from scipy import ndimage as ndi
from skimage import feature
from itertools import zip_longest
from scipy.interpolate import *


# grid and placement of bacteria
np.random.seed(2)
fig = plt.figure()
gridsize = 100
grid = np.zeros((gridsize, gridsize))

x = gridsize // 2
y = gridsize // 2

x1 = gridsize // 2
y1 = gridsize // 2

# celler i interval

grid[x, ::5] = 1
grid[x, ::10] = 2


# setup the animation

im = plt.imshow(grid.T, origin="lower", cmap=plt.cm.get_cmap("brg", 3), animated=True)


#Setting up a random walker
def walk(x,y,grid):
    val = np.random.randint(0,10) # probability of cell splitting in a time-interval
    if val == 1:
        pos = np.random.randint(1, 9)
        if pos == 1:
            xnew = x + 1
            ynew = y
        elif pos == 2:
            xnew = x - 1
            ynew = y
        elif pos == 3:
            xnew = x + 1
            ynew = y + 1
        elif pos == 4:
            xnew = x - 1
            ynew = y - 1
        elif pos == 5:
            xnew = x
            ynew = y + 1
        elif pos == 6:
            xnew = x
            ynew = y - 1
        elif pos == 7:
            xnew = x + 1
            ynew = y-1
        else:
            xnew = x - 1
            ynew = y + 1
        if grid[xnew, ynew] == 0:
            grid[xnew, ynew] = grid[x, y]
            x = xnew
            y = ynew
def updatefig(i, *args):
    global x, y, x1, y1  # globalise variable
    im.set_array(grid)
    location = np.argwhere(grid != 0)
    steparray = np.array(location)  # convert coordinates to numpyarray
    for pos in steparray:
        try:
            walk(*pos, grid)
        except IndexError as identifier:
            pass
    # location1 = np.argwhere(grid==2)
    # steparray1= np.array(location1)
    return (im,)


# plt.title("E. coli bacteria 1 (Red) vs E coli bacteria 2 (Green) on a lattice grid")
# plt.imshow(grid)

for _ in tqdm(range(1000)):
    updatefig(1)


img = grid

edges1 = feature.canny(img)
edges2 = feature.canny(img, sigma=3)

# display results
fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(8, 3))
fig, (ax4, ax5, ax6, ax7) = plt.subplots(nrows=1, ncols=4, figsize=(8, 3))

ax1.imshow(img, cmap=plt.cm.gray)
ax1.set_title("noisy image", fontsize=20)

ax2.imshow(edges1, cmap=plt.cm.gray)
ax2.set_title("Canny filter, $\sigma=1$", fontsize=20)

ax3.imshow(edges2, cmap=plt.cm.gray)
ax3.set_title("Canny filter, $\sigma=3$", fontsize=20)
#################################

##      ANIMATION        ##

#################################

# For Animation
ani = animation.FuncAnimation(fig, updatefig, interval=1, blit=True, frames=1000)

# save as  mpeg

# ani.save('bac3.mpeg')

plt.show()
