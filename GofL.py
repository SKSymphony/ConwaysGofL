import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def letThereBeLife(frameNum, img, grid, object_grid):
    for rows in object_grid:
        for cell in rows:
            cell.total = cell.countNeighbors(grid, cell.row, cell.col)
    for rows in object_grid:
        for cell in rows:
            total = cell.countNeighbors(grid, cell.row, cell.col)
            if cell.color == 255:
                if (cell.total < 2) or (cell.total > 3):
                    cell.color = 0
            else:
                if cell.total == 3:
                    cell.color = 255
                    # update data
            grid[cell.row, cell.col] = cell.color
    img.set_data(grid)

    return img

class Cell(object):
    def __init__(self, row_col, probLife):
        self.row, self.col = row_col
        self.probLife = probLife
        self.color = np.random.choice([0, 255], p=[probLife, 1-probLife])
        self.total = 0


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


N = 50
p = 0.5

def main():
    # Declare object_grid:
    object_grid = np.empty(shape=(N, N), dtype=object)

    # Call Grid generatingfunction:
    grid, object_grid = gridGenerator(N, object_grid)
    updateInterval = 50
    #for row in object_grid:
    #    for cell in row:
            # print(cell.color)
            # print(str(cell.row) + "  " + str(cell.col))
            # print(cell.countNeighbors(grid, cell.row, cell.col))
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, letThereBeLife, fargs=(img, grid, object_grid),
                                  frames=10,
                                  interval=updateInterval,
                                  save_count=50)


    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=15, bitrate=1800)
    ani.save('GofL.mp4', writer=writer)

    plt.show()

if __name__ == '__main__':
    main()
