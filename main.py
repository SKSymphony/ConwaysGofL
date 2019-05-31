import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Cell(object):
    def __init__(self, row_col, probLife):
        self.row, self.col = row_col
        self.probLife = probLife
        self.color = np.random.choice([0, 255], p=[probLife, 1-probLife])


    def countNeighbors(self, color_grid, row, col):
        total = int((color_grid[row, (col-1)%N] + color_grid[row, (col+1)%N] +
                color_grid[(row-1)%N, col] + color_grid[(row+1)%N, col] +
                color_grid[(row-1)%N, (col-1)%N] + color_grid[(row-1)%N, (col+1)%N] +
                color_grid[(row+1)%N, (col-1)%N] + color_grid[(row+1)%N, (col+1)%N])/255)
        return total

def gridGenerator(N, tracking_grid):
    # Create a matrix of Cell objects where we pass to each of them:
    # Their [row, col] and initial probability
    grid = np.empty(shape=(N, N))
    for row in range(N):
        for col in range(N):
            cell = Cell([row, col], p)
            grid[row, col] = cell.color
            tracking_grid[row, col] = cell
    return grid, tracking_grid


N = 10
p = 0.5

def main():
    # Declare object_grid:
    object_grid = np.empty(shape=(N, N), dtype=object)

    # Call Grid generatingfunction:
    grid, object_grid = gridGenerator(N, object_grid)

    #for row in object_grid:
    #    for cell in row:
            # print(cell.color)
            # print(str(cell.row) + "  " + str(cell.col))
            # print(cell.countNeighbors(grid, cell.row, cell.col))

    plt.imshow(grid, interpolation='nearest')
    plt.show()

main()
