from Personal_Projects.basketballOS.modules.input_handler import add_practice

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
                add_practice()
            case 2:
                print("View history function coming soon")
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

