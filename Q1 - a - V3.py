# Importing the required libraries and uploading the image maze

import matplotlib.pyplot as plt
import numpy as np

image_maze = plt.imread(r"C:\Users\aliza\Desktop\Data\Masters UK\C3 - 7WCM2026-0911-2026 - Data Structure and Algorithms 2\Assignment Info\maze.png")

# Convert the image maze into black and white, and making into 21 x 21 squares 
maze = image_maze[:, :, 0]
maze = maze[5::10, 5::10]

# Convert the maze into 0 and 1, and display the complete maze in the terminal
maze = (maze < 0.5).astype(int)
np.set_printoptions(threshold=np.inf)

print("My Maze of 21 x 21 squares:")
print(maze)
