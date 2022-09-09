import sys

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt


# grid and placement of bacteria
if len(sys.argv) != 2:
    gridsize = 100
#    gridsize = int(input("Please, enter gridsize: "))
else:
    gridsize = int(sys.argv[1])

fig = plt.figure()
grid = np.zeros((gridsize, gridsize))

x = gridsize // 2
y = gridsize // 2

x1 = gridsize // 2
y1 = gridsize // 2

# cell intervals

grid[x, ::5] = 1
grid[x, ::10] = 2


# setup the animation

im = plt.imshow(grid.T, origin="lower",
                cmap=plt.cm.get_cmap("brg", 3), animated=True)


# Setting up a random walker


def walk(x: int, y: int, grid: npt.ArrayLike):
    """Self-avoiding random walker. At a given probability, a random cell will
    split and expand in a random direction. Cells cannot overlap.

    Args:
        x,y,: Starting coordinates for bacteria cell
        grid (npt.ArrayLike): Initial grid setting for bacteria
    """

    # probability of cell splitting in a time-interval
    val = np.random.randint(0, 10)
    if val == 1:

        pos = np.array(
            [
                [x + 1, y],
                [x - 1, y],
                [x + 1, y + 1],
                [x - 1, y - 1],
                [x, y + 1],
                [x, y - 1],
                [x + 1, y - 1],
                [x - 1, y + 1],
            ]
        )
        xnew, ynew = pos[np.random.randint(0, 8)]
        if grid[xnew, ynew] == 0:
            grid[xnew, ynew] = grid[x, y]
            x = xnew
            y = ynew


def updatefig(*args):
    """Used to update the animation plot with the random walker for each timestep.

    Returns:
        im, AxesImage: Updates the image data without producing a new plot
    """
    global x, y, x1, y1  # make variable global
    im.set_array(grid)
    location = np.argwhere(grid != 0)
    steparray = np.array(location)  # convert coordinates to numpy array
    for pos in steparray:
        try:
            walk(*pos, grid)
        except IndexError as identifier:
            pass
    return (im,)


img = grid


# Animation
ani = animation.FuncAnimation(fig, updatefig, interval=2,
                              blit=True, frames=1000)
ani.save("bac3.mp4", fps=30)
plt.show()
