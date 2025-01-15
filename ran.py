is_raining = True  # Set to True if it's raining, otherwise False
have_umbrella = False  # Set to True if you have an umbrella, otherwise False

while is_raining:
    if have_umbrella:
        print("You can go outside with your umbrella.")
        break
    else:
        print("It's raining, better wait inside.")
        # Simulate waiting by manually changing the weather condition
        is_raining = False  # Change this to simulate the rain stopping

if not is_raining:
    print("It's not raining anymore, you can go outside.")
