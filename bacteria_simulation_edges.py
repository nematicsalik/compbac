import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import typer

fig = plt.figure()


class Walker:
    """Modelling bacteria as self-avoiding random walkers on a grid."""

    def __init__(self, gridsize: int, bactype1: int, bactype2: int, interval: int):
        """_summary_

        Args:
            gridsize (int): Size of grid.
            bactype1 (int): First bacteria species.
            bactype2 (int): Second bacteria species.
            interval (int): Interval between bacteria starting point.
        """
        self.grid = np.zeros((gridsize, gridsize))
        self.gridsize = gridsize
        self.x = gridsize // 2
        self.y = gridsize // 2
        self.grid[self.x, ::interval] = bactype1
        self.grid[self.x, :: interval * 2] = bactype2

    def walk(self):
        """Self-avoiding random walker. At a given probability, a random cell will
        split and expand in a random direction. Cells cannot overlap.

        Args:
            x,y,: Starting coordinates for bacteria cell
            grid (npt.ArrayLike): Initial grid setting for bacteria
        """
        x = self.x
        y = self.y
        grid = self.grid
        location = np.argwhere(self.grid != 0)
        for x, y in location:
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


def main(gridsize: int):
    mywalker = Walker(100, 1, 2, 5)
    im = plt.imshow(
        mywalker.grid.T, origin="lower", cmap=plt.cm.get_cmap("brg", 3), animated=True
    )
    typer.echo(f"Gridsize is {gridsize}!")

    def updatefig(*args):
        """Used to update the animation plot with the random walker for each timestep.

        Returns:
            im, AxesImage: Updates the image data without producing a new plot
        """
        im.set_array(mywalker.grid)
        mywalker.walk()
        return (im,)
    _ = animation.FuncAnimation(fig, updatefig, interval=5, blit=True, frames=1000)
    plt.show()


if __name__ == "__main__":
    typer.run(main)
