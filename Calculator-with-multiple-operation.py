import math
import os

def display_menu():
    print("Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Square Root")
    print("8. Cube")
    print("9. Exit")
    #The above is the menu of the calculator which will be displayed to the user.
    #The user will be asked to enter the choice of operation they want to perform.

def addition(a, b):
    return a + b
    #The above function will take two arguments and return the sum of the two numbers.

def subtraction(a, b):
    return a - b
    #The above function will take two arguments and return the difference of the two numbers.

def multiplication(a, b):
    return a * b
    #The above function will take two arguments and return the product of the two numbers.

def division(a, b):
    if b == 0:
        return "Not Division by zero"
    return a / b
    #The above function will take two arguments and return the division of the two numbers.
    #If the second number is zero, it will return "Not Division by zero".

def modulus(a, b):
    if b == 0:
        return "Not Division by zero"
    return a % b
    #The above function will take two arguments and return the modulus of the two numbers.
    #If the second number is zero, it will return "Not Division by zero".

def exponentiation(a, b):
    return a ** b
    #The above function will take two arguments and return the exponentiation of the two numbers.

def square_root(a):
    if a < 0:
        return "why you enter  Negative number"
    return math.sqrt(a)
    #The above function will take one argument and return the square root of the number.
    #If the number is negative, it will return "why you enter  Negative number".

def cube(a):
    return a ** 3
    #The above function will take one argument and return the cube of the number.

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '9':
            print("Exiting from the program. Goodbye!")
            print("Thank you for using the calculator")
            break
        #The above code will exit the program if the user enters 9.
        
        if choice in ['1', '2', '3', '4', '5', '6']:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            #The above code will take two numbers as input if the user enters any choice from 1 to 6.
        elif choice in ['7', '8']:
            a = float(input("Enter the number: "))
            #The above code will take one number as input if the user enters any choice from 7 to 8.
            #The above code will take the input from the user and convert it into a float.
        
        if choice == '1':
            print("The result is:", addition(a, b))
            #The above code will call the addition function and print the result.
            #The result will be the sum of the two numbers.
        elif choice == '2':
            print("The result is:", subtraction(a, b))
            #The above code will call the subtraction function and print the result.
            #The result will be the difference of the two numbers.
        elif choice == '3':
            print("The result is:", multiplication(a, b))
            #The above code will call the multiplication function and print the result.
            #The result will be the product of the two numbers.
        elif choice == '4':
            print("The result is:", division(a, b))
            #The above code will call the division function and print the result.
        elif choice == '5':
            print("The result is:", modulus(a, b))
            #The above code will call the modulus function and print the result.
            #The result will be the modulus of the two numbers.
            #If the second number is zero, it will print "Not Division by zero".
        elif choice == '6':
            print("The result is:", exponentiation(a, b))
            #The above code will call the exponentiation function and print the result.
            #The first number will be the base and the second number will be the exponent.
        elif choice == '7':
            print("The result is:", square_root(a))
            #The above code will call the square_root function and print the result.
            #If the number is negative, it will print "why you enter  Negative
        elif choice == '8':
            print("The result is:", cube(a))
            #The above code will call the cube function and print the result.
        else:
            print("Invalid choice. Please try again.")
            print("Why you enter invalid choice")
            #The above code will print "Invalid choice. Please try again." if the user enters an invalid choice.
        
        continue_choice = input("Do you want to continue? (Y/N): ").strip().lower()
        if continue_choice != 'y':
            print("Exiting the program. Goodbye!")
            break
        #The above code will exit the program if the user enters anything other than 'y'.
    print("Thank you for using the calculator")
    #The above code will print "Thank you for using the calculator" after the user exits the program.
main()
#The above code will call the main function when the program is executed.
