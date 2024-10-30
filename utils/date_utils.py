from datetime import datetime

def get_day_of_month(date):
    # Get the day of the week (e.g., 'Monday', 'Tuesday', ...)
    day_of_week = date.strftime('%A')
    
    # Calculate the week number
    week_number = (date.day - 1) // 7 + 1
    
    # Map week number to the appropriate string representation
    week_mapping = {
        1: "First",
        2: "Second",
        3: "Third",
        4: "Forth",
        5: "Fifth"  # In case there are fifth occurrences
    }
    
    week_str = week_mapping.get(week_number, f"{week_number}th")  # Default if week_number > 5

    # Return the formatted string
    return f"{week_str} {day_of_week}"
