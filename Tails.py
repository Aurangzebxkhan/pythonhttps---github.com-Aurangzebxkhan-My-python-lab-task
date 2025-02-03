import random

numberOfStreaks = 0

for experimentNumber in range(10000):
    # Step 1: Create a list of 100 'heads' or 'tails' values
    flips = []
    for i in range(100):
        if random.randint(0, 1) == 0:
            flips.append('H')
        else:
            flips.append('T')
    
    # Step 2: Check if there is a streak of 6 heads or tails in a row
    streak_count = 1
    for i in range(1, len(flips)):
        if flips[i] == flips[i - 1]:
            streak_count += 1
            if streak_count == 6:
                numberOfStreaks += 1
                break
        else:
            streak_count = 1

# Calculate and print the chance of streaks
print('Chance of streak: %s%%' % (numberOfStreaks / 10000 * 100))
