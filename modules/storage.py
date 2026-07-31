import csv
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(BASE_DIR, "data", "practice_log.csv")

def save_practice(practice):
    file_exists = os.path.exists(CSV_PATH)
    with open(CSV_PATH, "a", newline ="") as file:
        fieldnames = ['date', 'duration_min', 'fg_made', 'fg_attempted', 'three_made', 'three_attempted', 'ft_made', 'ft_attempted', 'vertical_cm', 'sleep_hours', 'energy', 'notes']

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()
        writer.writerow(practice)
