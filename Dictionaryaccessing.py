# Initialize a dictionary with some predefined birthday entries
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:  # Create an infinite loop to continuously prompt the user for input
    print('Enter a name: (blank to quit)')
    name = input()  # Prompt the user to enter a name and store it in the variable 'name'
    if name == '':  # Check if the user entered a blank input
        break  # Exit the loop if the input is blank

    # Check if the entered name exists in the birthdays dictionary
    if name in birthdays:
        # If the name exists, print the corresponding birthday
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        # If the name does not exist in the dictionary, prompt the user to enter the birthday
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()  # Store the entered birthday in the variable 'bday'
        
        # Update the birthdays dictionary with the new name and birthday entry
        birthdays[name] = bday
        print('Birthday database updated.')
