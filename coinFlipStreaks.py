import random

def generate_flips(num_flips):
    """Generate a list of random 'H' and 'T' values."""
    flips = ['H' if random.randint(0, 1) == 0 else 'T' for _ in range(num_flips)]
    return flips

def check_streak(flips, streak_length):
    """Check for streaks of 'H' or 'T' of a given length in the list."""
    current_streak = 1
    streak_found = False
    for i in range(1, len(flips)):
        if flips[i] == flips[i - 1]:
            current_streak += 1
            if current_streak == streak_length:
                streak_found = True
                break
        else:
            current_streak = 1
    return streak_found

def experiment(num_trials, num_flips, streak_length):
    """Run the experiment to find the percentage of streaks."""
    streak_count = 0
    for _ in range(num_trials):
        flips = generate_flips(num_flips)
        if check_streak(flips, streak_length):
            streak_count += 1
    return (streak_count / num_trials) * 100

# Parameters for the experiment
num_trials = 10000
num_flips = 100
streak_length = 6

# Run the experiment and print the result
percentage_streaks = experiment(num_trials, num_flips, streak_length)
print(f'Percentage of streaks of {streak_length} in {num_flips} flips: {percentage_streaks}%')
