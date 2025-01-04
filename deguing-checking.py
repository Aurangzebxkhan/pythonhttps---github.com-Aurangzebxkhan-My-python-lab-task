# Factorial Program

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        # Set a breakpoint on the next line to visualize the variables
        print(f"Step {i}: i = {i}, result = {result}")
    return result

# Ask the user for a number
number = int(input("Enter a number to calculate its factorial: "))

# Calculate the factorial
fact = factorial(number)

# Print the final result
print(f"The factorial of {number} is {fact}")
