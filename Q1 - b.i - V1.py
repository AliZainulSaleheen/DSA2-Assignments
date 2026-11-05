import matplotlib.pyplot as plt
import numpy as np
import random

# Read the maze image
image_maze = plt.imread(r"C:\Users\aliza\Desktop\Data\Masters UK\C3 - 7WCM2026-0911-2026 - Data Structure and Algorithms 2\Assignment Info\maze.png")

# Select one colour channel
maze = image_maze[:, :, 0]

# Convert into 21 x 21 squares
maze = maze[5::10, 5::10]

# Convert black walls into 1 and white paths into 0
maze = (maze < 0.5).astype(int)


# Starting position of the maze
row = 0
col = 9

# Exit position of the maze
exit_row = 20
exit_col = 11

# Set the maximum number of steps
steps = 0
max_steps = 200

# Possible directions
directions = [
    (-1, 0),  # Up
    (1, 0),   # Down
    (0, -1),  # Left
    (0, 1)    # Right
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
