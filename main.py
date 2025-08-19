def add_time(start, duration, start_day=None):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # Parsing start time
    time, period = start.split()
    start_hour, start_minute = map(int, time.split(":"))
    
    # Converting start time to 24-hour format
    if period == "PM" and start_hour != 12:
        start_hour += 12
    elif period == "AM" and start_hour == 12:
        start_hour = 0
    
    # Parsing duration
    duration_hours, duration_minutes = map(int, duration.split(":"))
    
    # Calculating new time
    total_minutes = start_minute + duration_minutes
    extra_hours = total_minutes // 60
    new_minutes = total_minutes % 60
    
    total_hours = start_hour + duration_hours + extra_hours
    new_hour = total_hours % 24
    days_later = total_hours // 24
    
    # Determining new period (AM/PM)
    if new_hour >= 12:
        period = "PM"
        if new_hour > 12:
            new_hour -= 12
    else:
        period = "AM"
        if new_hour == 0:
            new_hour = 12
    
    # Determining the new day of the week if provided
    if start_day:
        start_day = start_day.capitalize()
        if start_day in days_of_week:
            new_day_index = (days_of_week.index(start_day) + days_later) % 7
            new_day = ", " + days_of_week[new_day_index]
        else:
            new_day = ""
    else:
        new_day = ""
    
    # Formatting the days later part
    if days_later == 1:
        days_later_text = " (next day)"
    elif days_later > 1:
        days_later_text = f" ({days_later} days later)"
    else:
        days_later_text = ""
    
    return f"{new_hour}:{new_minutes:02d} {period}{new_day}{days_later_text}"

# Example usage
print(add_time('3:00 PM', '3:10'))
print(add_time('11:30 AM', '2:32', 'Monday'))
print(add_time('11:43 AM', '00:20'))
print(add_time('10:10 PM', '3:30'))
print(add_time('11:43 PM', '24:20', 'tueSday'))
print(add_time('6:30 PM', '205:12'))
