import matplotlib.pyplot as plt
import numpy as np
import random

# Reading  the maze image

image_maze = plt.imread(r"C:\Users\aliza\Desktop\Data\Masters UK\C3 - 7WCM2026-0911-2026 - Data Structure and Algorithms 2\Assignment Info\maze.png")

# Selecting the one colour

maze = image_maze[:, :, 0]

maze = maze[5::10, 5::10]

# Defining walls into 1 and paths into 0

maze = (maze < 0.5).astype(int)

# Question 1(b.i) The Las Vegas Approach and starting position of the maze because pyton start from 0, and exit position of the maze will be as follows 

row = 0
col = 9

exit_row = 20
exit_col = 11

# Defining the maximum number of steps suggested in the questions

steps = 0
max_steps = 200

# Possible directions 2D (UP, DOWN, LEFT AND RIGHT)

directions = [
    (-1, 0),  # MOVE TO Up
    (1, 0),   # MOVE TO Down
    (0, -1),  # MOVE TO Left
    (0, 1)    # MOVE TO Right
]

# Start moving through the maze
while steps < max_steps:

    # Check if we have reached the exit
    if row == exit_row and col == exit_col:
        break

    # Create a list for possible moves
    possible_moves = []

    # Check all four directions
    for r, c in directions:

        new_row = row + r
        new_col = col + c

        # Check that the position is inside the maze
        if 0 <= new_row < 21 and 0 <= new_col < 21:

            # Check if it is a white square
            if maze[new_row, new_col] == 0:
                possible_moves.append((new_row, new_col))

    # Stop if there are no available moves
    if len(possible_moves) == 0:
        break

    # Choose a random available move
    row, col = random.choice(possible_moves)

    # Count one step
    steps = steps + 1

    print("Step:", steps, "Position:", row, col)

# Display the final result
if row == exit_row and col == exit_col:
    print("Successful! Exit found.")
else:
    print("Unsuccessful! Exit not found.")

print("Total steps:", steps)
