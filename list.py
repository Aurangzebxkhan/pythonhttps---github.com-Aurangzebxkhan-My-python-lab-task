import datetime

def find_data():
    names = []
    ages = []
    
    # Get the number of entries
    num_entries = int(input("Enter the number of entries: "))
    
    # Collect names and ages
    for _ in range(num_entries):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        names.append(name)
        ages.append(age)
    
    # Find data for "Bob"
    if "Bob" in names:
        index = names.index("Bob")
        print(f"Data for Bob: Name = {names[index]}, Age = {ages[index]}")
    else:
        print("Bob not found in the list.")

    # Show current date and time details
    now = datetime.datetime.now()
    print("Current Date and Time Details:")
    print(f"Year: {now.year}")
    print(f"Month: {now.month}")
    print(f"Week: {now.strftime('%U')}")
    print(f"Day: {now.day}")
    print(f"Hour: {now.hour}")
    print(f"Minute: {now.minute}")
    print(f"Second: {now.second}")

# Call the function
find_data()

thislist = ["apple", "banana", "cherry"]
print(thislist)

thilist2 = ["apple", "banana", "cherry"]
for item in thilist2:
    print(len(thilist2))
    break  # Exit the loop after printing the length once

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]
print(list1, "\n", list2, "\n",list3,"\n", list4, "\n")

list5 = ["apple", 1, True, False, "male", 2.5, 'a', 6]
print(list5)
print(len(list5))

# # Print each item in the list
for item in list5:
    print(item)

# # Print the 8th item in the list (index 7)
print(list5[7])
print(list5[2:5])
print(list5[1:7])
subject=[" fundamentals","ict lab","ICT theory","discreat mathemtical","function english","islamyath"]
print(subject[3])
print(subject[1:3])
print(subject[-1:5])
print(subject[-4])
print(subject[-1:-5])
print(subject[1:-5])
subject = ["fundamentals", "ict lab", "ICT theory", "discreat mathemtical", "function english", "islamyath"]

# Change "ICT theory" to a new value
subject[2] = "Advanced ICT theory ko chang kar bas ho tayh"
# Print the updated list to verify the change
print(subject)
subject[2:6]="khan g","my Name","King khan","jkajdfjl","denger khan dy sir g"
print(subject)


list=["apple","organ","banana","good apple ","new apple","old appple"]
list1=[11,13,15,13,15,16]
combinelist=list+list1
print(combinelist)

