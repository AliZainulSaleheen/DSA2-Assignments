import matplotlib.pyplot as plt
# Read the maze image
image_maze = plt.imread(r"C:\Users\aliza\Desktop\Data\Masters UK\C3 - 7WCM2026-0911-2026 - Data Structure and Algorithms 2\Assignment Info\maze.png")

# Select one colour channel
maze = image_maze[:, :, 0]

# Convert into 21 x 21 squares
maze = maze[5::10, 5::10]

# Convert black walls into 1 and white paths into 0
maze = (maze < 0.5).astype(int)

# Display the maze size
print("Maze size:", maze.shape)

# Question 1(b.ii) - Backtracking Approach

# Starting position of the maze
row = 0
col = 9

# Exit position of the maze
exit_row = 20
exit_col = 11

# Four possible directions
directions = [
    (1, 0),   # Down
    (0, 1),   # Right
    (0, -1),  # Left
    (-1, 0)   # Up
]

# Store the starting position
path = [(row, col)]

# Store the visited squares
visited = [(row, col)]

# Start searching for the exit
while len(path) > 0:

    # Get the current position
    row, col = path[-1]

    # Check if we reached the exit
    if row == exit_row and col == exit_col:
        print("Successful! Exit found.")
        break

    # Check if a new direction is available
    found = False

    # Try all four directions
    for r, c in directions:

        new_row = row + r
        new_col = col + c

        # Check if the position is inside the maze
        if 0 <= new_row < 21 and 0 <= new_col < 21:

            # Check if it is a path and not visited before
            if maze[new_row, new_col] == 0 and (new_row, new_col) not in visited:

                # Save the new position
                path.append((new_row, new_col))
                visited.append((new_row, new_col))

                print("Moving to:", new_row, new_col)

                found = True
                break

    # Go back if no new direction is available
    if found == False:
        path.pop()
        print("Backtracking to previous position")

# Check the final result
if len(path) == 0:
    print("Unsuccessful! Exit not found.")
else:
    print("Total squares in final path:", len(path))
