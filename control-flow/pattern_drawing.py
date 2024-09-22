# pattern_drawing.py

# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize a variable to track the current row
row = 0

# Outer while loop for rows
while row < size:
    # Inner for loop to print asterisks in each row
    for col in range(size):
        print("*", end="")  # Print asterisks on the same line without newline

    print()  # After each row, print a newline to move to the next row
    row += 1  # Increment the row counter
