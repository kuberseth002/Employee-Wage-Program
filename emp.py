import random

def emp_attendance():
    return random.choice([0, 1])  # 0 for absent, 1 for present

def calculate_daily_wage():
    worktype = random.randint(0, 2)  # 0: No work, 1: Part-time, 2: Full-time
    part_time_hours = 4
    full_time_hours = 8
    wages_per_hour = 20
    total_hours = 0
    total_wages = 0

    if emp_attendance() == 1:
        match worktype:
            case 1:
                total_hours = part_time_hours
                total_wages = part_time_hours * wages_per_hour
            case 2:
                total_hours = full_time_hours
                total_wages = full_time_hours * wages_per_hour
            case _:
                total_hours = 0
                total_wages = 0
    else:
        total_hours = 0
        total_wages = 0

    return total_hours, total_wages

def calculate_wages_until_limit(max_hours=100, max_days=20):
    total_hours = 0
    total_wages = 0
    days_worked = 0

    while total_hours < max_hours and days_worked < max_days:
        daily_hours, daily_wage = calculate_daily_wage()
        total_hours += daily_hours
        total_wages += daily_wage
        days_worked += 1

    print(total_hours)
    print(total_wages)
    print(days_worked)

if _name_ == "_main_":
    calculate_wages_until_limit()