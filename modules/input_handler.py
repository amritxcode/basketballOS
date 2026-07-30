def add_practice():
    date = input("Date (YYYY-MM-DD): ")
    duration_min = int(input("Duration (min): "))
    fg_made = int(input("Field Goals Made: "))
    fg_attempted = int(input("Field Goals Attempted: "))
    three_made = int(input("Three Made: "))
    three_attempted = int(input("Three Attempted: "))
    ft_made = int(input("Free Throws Made:"))
    ft_attempted = int(input("Free Throws Attempted:"))
    vertical_cm = int(input("Vertical (cm): "))
    energy = int(input("Energy (1-10): "))
    sleep_hours = float(input("Duration (hours): "))
    notes = (input("Any Self Notes: "))

    practice = {
        "date": date,
        "duration_min": duration_min,
        "fg_made": fg_made,
        "fg_attempted": fg_attempted,
        "three_made": three_made,
        "three_attempted": three_attempted,
        "ft_made": ft_made,
        "ft_attempted": ft_attempted,
        "vertical_cm": vertical_cm,
        "sleep_hourgit git remote add origin https://github.com/amritxcode/basketballOS.gits": sleep_hours,
        "energy": energy,
        "notes": notes
    }

    return practice