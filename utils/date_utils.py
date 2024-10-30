from datetime import datetime

def get_day_of_month(date):
    day_of_week = date.strftime('%A')
    week_number = (date.day - 1) // 7 + 1
    return f"{week_number} {day_of_week}"
