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

def load_practices():
    practices = []
    with open(CSV_PATH, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["duration_min"] = int(row["duration_min"])
            row["fg_made"] = int(row["fg_made"])
            row["fg_attempted"] = int(row["fg_attempted"])
            row["three_made"] = int(row["three_made"])
            row["three_attempted"] = int(row["three_attempted"])
            row["ft_made"] = int(row["ft_made"])
            row["ft_attempted"] = int(row["ft_attempted"])
            row["vertical_cm"] = int(row["vertical_cm"])
            row["energy"] = int(row["energy"])
            row["sleep_hours"] = float(row["sleep_hours"])
            practices.append(row)
            
    return practices