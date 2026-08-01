def calculate_percentage(made, attempted):
    if attempted == 0:
        return "N/A"
    
    return round(made/attempted * 100, 2)