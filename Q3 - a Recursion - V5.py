
# Question 3(a) - Recursion in this program follow the instructions using the 3 colours (blue, red and green). Every colour is having a different rule for moving to next index.
# It will start from index Zero (0) through recursion to move the list. This will stop when the following index is outside the list and/or when next blue cannot be found.
# In the end it will return the all visited indexes in order.


def follow_instructions(instructions: list[str]) -> list[int]:

# This function find the first and/or current colour and utilize the recursion to move to the next index based on the colour defined rule.
    def move(index):

        if index >= len(instructions):
            return []

        colour = instructions[index]

# When the colour is blue, it will look for next blue from list and switch to the element right after it.
        if colour == "blue":

            next_blue = -1

            for i in range(index + 1, len(instructions)):
                if instructions[i] == "blue":
                    next_blue = i
                    break

            if next_blue == -1:
                return [index]

            next_index = next_blue + 1

# When it is red, multiply the current index by 2 and adding (+1) and when green it will move to the next index by adding (+1).
        elif colour == "red":
            next_index = 2 * index + 1

        elif colour == "green":
            next_index = index + 1

# Storing the current index information and call the function once again using the next index until the stopping condition is met.
        return [index] + move(next_index)

    return move(0)


# Validating the function using the example output provided by the teacher. Further, 2 additional lists are used to validate that the function is appropriately following the colour rules and returns visited indexes as expected.

instructions = ["blue", "green", "red", "blue", "green", "red"]

print("Example provided by the teacher:", follow_instructions(instructions))


# Test 1 - Validating GREEN and RED movements
list_1 = ["green", "red", "blue", "green", "red"]

print("Test 1:", follow_instructions(list_1))


# Test 2 - Validating the BLUE, GREEN and RED movements
list_2 = ["blue", "red", "green", "blue", "green", "red"]

print("Test 2:", follow_instructions(list_2))
