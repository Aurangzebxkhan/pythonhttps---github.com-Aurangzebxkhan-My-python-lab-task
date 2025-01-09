import random
number_to_guess = random.randint(5, 10)
user_guess = 0
while user_guess != number_to_guess:
    user_guess = int(input("Guess a number between 1 and 10: "))
    if user_guess < number_to_guess:
        print("Too low!")
    elif user_guess > number_to_guess:
        print("Too high!")
print("Congratulations! You guessed the right number.")
print("the number was", number_to_guess)
print("thank you for playing")