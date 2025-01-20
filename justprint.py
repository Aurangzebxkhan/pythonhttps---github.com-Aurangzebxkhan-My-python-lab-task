# print("Welcome to my python program")
# a = input("Enter your name: ")
# print(a)

# print("You are welcome, bro")
# b = int(input("Enter your Age: "))
# if b == 10:
#     print("You are just 10 years old, enjoy your childhood!")
# elif b == 12:
#     print("You are 12 years old, keep exploring and learning new things!")
# elif b == 18:
#     print("You are 18 years old, welcome to adulthood!")
#     print("In this age Focus on goal not on whole if you focus on whole you destroy your future")
# elif b > 18:
#     print("You are above 18 years old, embrace the responsibilities and opportunities of adulthood!")
# else:
#     print("You are young and have a bright future ahead!")

# print("Your Name is ", a, "You are Year ", b, "old")
# c = input("Enter your School Name ")
# print("Your Name is ", a, "your are ", b, " Year old", "Your are read in ", c, "school/university")

# # Adding a for loop to print a list of favorite subjects
# favorite_subjects = ["Math", "Science", "History", "Art"]
# print("Your favorite subjects are:")
# for subject in favorite_subjects:
#     print(subject)

# # Adding a while loop to count down from 5
# count = 5
# while count > 0:
#     print("Countdown:", count)
#     count -= 1
# print("Countdown complete!")


print("🌟 Welcome to My Python Program! 🌟")

# Taking user details
name = input("👤 Please enter your name: ")
print(f"Hello, {name}! It's great to have you here. 😊")

# Taking user age and providing tailored messages
age = int(input("🎂 How old are you? "))
if age == 10:
    print("You're just 10 years old! Enjoy the magic of childhood. 🌈")
elif age == 12:
    print("At 12 years old, you're at the perfect age to learn and explore! 📘")
elif age == 18:
    print("Welcome to adulthood at 18! 🎉")
    print("Focus on your goals, and don't let distractions steer you away from your dreams. 🚀")
elif age > 18:
    print("Being above 18, you have so many responsibilities and opportunities ahead! Make the most of them. 💼")
else:
    print("You're young with a bright future ahead. Keep dreaming big! 🌟")

# Displaying user details
print(f"Your name is {name}, and you are {age} years old.")

# Asking for school/university name
school_name = input("🏫 What's the name of your school or university? ")
print(f"{name}, you are {age} years old and study at {school_name}. 🎓")

# Displaying favorite subjects
favorite_subjects = ["Math", "Science", "History", "Art"]
print("\n📚 Some favorite subjects you might enjoy:")
for subject in favorite_subjects:
    print(f"- {subject}")

# Countdown feature
print("\n⏳ Let's do a quick countdown:")
count = 5
while count > 0:
    print(f"Countdown: {count}")
    count -= 1
print("🚀 Countdown complete! Ready for new adventures! 🌟")
