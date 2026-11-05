import matplotlib.pyplot as plt
import numpy as np

image = plt.imread(r"C:\Users\aliza\Desktop\Data\Masters UK\C3 - 7WCM2026-0911-2026 - Data Structure and Algorithms 2\Assignment Info\maze.png")

maze = image[:, :, 0]

maze = maze[5::10, 5::10]

maze = (maze < 0.5).astype(int)

np.set_printoptions(threshold=np.inf)

print("My Maze:")
print(maze)
