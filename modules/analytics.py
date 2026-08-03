def calculate_percentage(made, attempted):
    if attempted == 0:
        return "N/A"
    
    return round(made/attempted * 100, 2)

def analyze_performance(practices):
    if len(practices) == 0:
        return None
    
    total_duration = 0
    total_fg_made = 0
    total_fg_attempted = 0
    total_three_made = 0
    total_three_attempted = 0
    total_ft_made = 0
    total_ft_attempted = 0
    total_vertical = 0
    best_vertical = 0
    total_energy = 0
    total_sleep = 0
    for practice in practices:
        total_duration += practice["duration_min"]
        total_fg_made += practice["fg_made"]
        total_fg_attempted += practice["fg_attempted"]
        total_three_made += practice["three_made"]
        total_three_attempted += practice["three_attempted"]
        total_ft_made += practice["ft_made"]
        total_ft_attempted += practice["ft_attempted"]
        total_vertical += practice["vertical_cm"]
        if practice["vertical_cm"] > best_vertical:
            best_vertical += practice["vertical_cm"]
        total_energy += practice["energy"]
        total_sleep += practice["sleep_hours"]
        total_sessions = len(practices)

    average_vertical = round(total_vertical / total_sessions, 2)
    average_energy = round(total_energy / total_sessions, 2)
    average_sleep = round(total_sleep / total_sessions, 2)

    average_fg = calculate_percentage(
        total_fg_made,
        total_fg_attempted
    )

    average_three = calculate_percentage(
        total_three_made,
        total_three_attempted
    )

    average_ft = calculate_percentage(
        total_ft_made,
        total_ft_attempted
    )

    training_hours = round(total_duration / 60, 2)

    return {
        "sessions": total_sessions,
        "training_hours": training_hours,
        "average_fg": average_fg,
        "average_three": average_three,
        "average_ft": average_ft,
        "average_vertical": average_vertical,
        "best_vertical": best_vertical,
        "average_energy": average_energy,
        "average_sleep": average_sleep,
    }
