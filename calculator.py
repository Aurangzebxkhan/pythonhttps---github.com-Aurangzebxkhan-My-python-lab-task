import math

def display_menu():
    print("Python Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Square Root")
    print("8. Cube")
    print("9. Exit")

def get_two_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    return num1, num2

def get_one_number():
    num = float(input("Enter the number: "))
    return num

def main():
    while True:
        display_menu()
        choice = input("Select an operation (1-9): ")

        if choice == '1':
            num1, num2 = get_two_numbers()
            print("Result:", num1 + num2)
        elif choice == '2':
            num1, num2 = get_two_numbers()
            print("Result:", num1 - num2)
        elif choice == '3':
            num1, num2 = get_two_numbers()
            print("Result:", num1 * num2)
        elif choice == '4':
            num1, num2 = get_two_numbers()
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Error: Division by zero")
        elif choice == '5':
            num1, num2 = get_two_numbers()
            print("Result:", num1 % num2)
        elif choice == '6':
            num1, num2 = get_two_numbers()
            print("Result:", num1 ** num2)
        elif choice == '7':
            num = get_one_number()
            print("Result:", math.sqrt(num))
        elif choice == '8':
            num = get_one_number()
            print("Result:", num ** 3)
        elif choice == '9':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid operation.")

        input("Press Enter to return to the main menu...")
    main()