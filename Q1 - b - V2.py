# Asking the user to decide an approach to solve the provide maze

print("Please decide a method to solve the provided maze:")
print("1. Backtracking")
print("2. Las Vegas")

method_approach = input("Enter your choice 1 or 2: ")

if method_approach == "1":
    print("You have selected the Backtracking approach to solve the provided maze")

elif method_approach == "2":
    print("You have selected the Las Vegas approach to solve the provided maze")

else:
    print("Invalid input, please enter the value and/or number 1 or 2 only")
