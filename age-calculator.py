from datetime import datetime, timedelta

def calculate_age(dob):
    today = datetime.now()
    delta = today - dob

    total_days = delta.days
    total_seconds = delta.total_seconds()
    
    total_years = total_days // 365
    total_months = total_days // 30
    total_weeks = total_days // 7
    total_hours = total_seconds // 3600
    total_minutes = total_seconds // 60

    return total_years, total_months, total_weeks, total_days, int(total_hours), int(total_minutes), int(total_seconds)

def main():
    name = input("Enter your name: ")
    dob_input = input("Enter your date of birth (YYYY-MM-DD): ")

    try:
        dob = datetime.strptime(dob_input, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    total_years, total_months, total_weeks, total_days, total_hours, total_minutes, total_seconds = calculate_age(dob)

    print(f"\nHello, {name}!")
    print(f"You are {total_years} years, {total_months} months, {total_weeks} weeks, {total_days} days, {total_hours} hours, {total_minutes} minutes, and {total_seconds} seconds .")

if __name__ == "__main__":
    main()
