from modules.input_handler import add_practice
from modules.storage import save_practice
from modules.storage import load_practices
from modules.analytics import calculate_percentage


def display_menu():
    print ('''
====================================
        AthleteOS v1.0
====================================

1. Add Practice
2. View History
3. Analyze Performance
4. Weekly Report
5. Exit''')

while True:
    display_menu()

    try:
        user_input = int(input("Choose an option(1-5): "))
        match user_input:
            case 1:
                practice = add_practice()
                save_practice(practice)
                print("Practice saved successfully")
            case 2:
                practices = load_practices()

                print("\n--- Practice History ---")

                for practice in practices:
                    fg_percentage = calculate_percentage(
                        practice["fg_made"],
                        practice["fg_attempted"]
                    )
                    three_percentage = calculate_percentage(
                        practice["three_made"],
                        practice["three_attempted"]
                        )
                    ft_percentage = calculate_percentage(
                        practice["ft_made"],
                        practice["ft_attempted"]
                    )
                    date = practice["date"]
                    duration = practice["duration_min"]
                    vertical = practice["vertical_cm"]
                    energy = practice["energy"]
                    sleep = practice["sleep_hours"]
                    
                    print("=" * 40)
                    print(f"Date       : {date}")
                    print(f"Duration   : {duration} min")
                    print(f"FG%        : {fg_percentage}")
                    print(f"3PT%       : {three_percentage}")
                    print(f"FT%        : {ft_percentage}")
                    print(f"Vertical   : {vertical} cm")
                    print(f"Energy     : {energy}/10")
                    print(f"Sleep      : {sleep} hrs")
                    print("=" * 40)
                    print()
            case 3:
                print("Analyze Performance funct coming soon")
            case 4:
                print("Weekly Report function coming soon")
            case 5:
                break
            case _:
                print("Enter a valid number between 1 to 5.")
    except ValueError:
        print("Please enter a valid number.")