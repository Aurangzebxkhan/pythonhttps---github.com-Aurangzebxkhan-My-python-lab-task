# birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

# while True:
#     print('Enter a name: (blank to quit)')
#     name = input()
#     if name == '':
#         break

#     if name in birthdays:
#         print(birthdays[name] + ' is the birthday of ' + name)
#     else:
#         print('I do not have birthday information for ' + name)
#         print('What is their birthday?')
#         bday = input()
#         birthdays[name] = bday
#         print('Birthday database updated.')


#birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4','Aurangzeb':'Feb 24'}

print("Welcome to the Birthday Database!")
print("You can look up birthdays or add new ones.")

while True:
    print('\nEnter a name to look up (or press Enter to quit):')
    name = input()
    if name == '':
        print("Goodbye!")
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name + '.')
    else:
        print('I do not have birthday information for' +name + '.')
        print("Would you like to add their birthday? (yes/no)")
        response = input().lower()
        if response == 'yes':
            print('What is their birthday?')
            bday = input()
            birthdays[name] = bday
            print("Birthday database updated: "+name + '- ' + bday)
        else:
            print("No problem, let's continue!")
