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

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Not Division by zero"
    return a / b

def modulus(a, b):
    if b == 0:
        return "Not Division by zero"
    return a % b

def exponentiation(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        return "why you enter  Negative number"
    return math.sqrt(a)

def cube(a):
    return a ** 3

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '9':
            print("Exiting from the program. Goodbye!")
            print("Thank you for using the calculator")
            break
        
        if choice in ['1', '2', '3', '4', '5', '6']:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
        elif choice in ['7', '8']:
            a = float(input("Enter the number: "))
        
        if choice == '1':
            print("The result is:", addition(a, b))
        elif choice == '2':
            print("The result is:", subtraction(a, b))
        elif choice == '3':
            print("The result is:", multiplication(a, b))
        elif choice == '4':
            print("The result is:", division(a, b))
        elif choice == '5':
            print("The result is:", modulus(a, b))
        elif choice == '6':
            print("The result is:", exponentiation(a, b))
        elif choice == '7':
            print("The result is:", square_root(a))
        elif choice == '8':
            print("The result is:", cube(a))
        else:
            print("Invalid choice. Please try again.")
            print("Why you enter invalid choice")
        
        continue_choice = input("Do you want to continue? (Y/N): ").strip().lower()
        if continue_choice != 'y':
            print("Exiting the program. Goodbye!")
            break
    print("Thank you for using the calculator")
main()
