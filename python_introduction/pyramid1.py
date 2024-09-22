# Define the height of the pyramid
rows = 5

# Initialize the outer loop control variable
i = 1

# Outer loop controls the number of rows
while i <= rows:
    # Print the leading spaces for each row
    spaces = rows - i
    j = 1
    while j <= spaces:
        print(" ", end="")
        j += 1

    # Print the asterisks for each row
    stars = 2 * i - 1
    k = 1
    while k <= stars:
        print("*", end="")
        k += 1

    # Move to the next line after printing each row
    print()
    
    # Increment the outer loop control variable
    i += 1
