import random

def emp_attendance():
    """
    Determines employee attendance randomly.
    
    Returns:
        int: 0 if absent, 1 if present.
    """
    try:
        return random.choice([0, 1])  # 0 for absent, 1 for present
    except Exception as e:
        print(f"Error in emp_attendance(): {e}")
        return 0  # Default to absent in case of error

def calculate_daily_wage():
    """
    Calculates the daily wage of an employee based on work type.

    Work type:
    - 0: No work
    - 1: Part-time (4 hours)
    - 2: Full-time (8 hours)

    Returns:
        tuple: (total_hours, total_wages)
    """
    try:
        worktype = random.randint(0, 2)  # Random work type selection
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
                case _:  # No work
                    total_hours = 0
                    total_wages = 0
        else:
            total_hours = 0
            total_wages = 0

        return total_hours, total_wages

    except Exception as e:
        print(f"Error in calculate_daily_wage(): {e}")
        return 0, 0  # Default to zero wages and hours in case of error

def calculate_wages_until_limit(max_hours=100, max_days=20):
    """
    Calculates wages until the given limits (maximum hours or maximum days) are reached.

    Args:
        max_hours (int, optional): The maximum number of work hours allowed. Default is 100.
        max_days (int, optional): The maximum number of workdays allowed. Default is 20.

    Returns:
        tuple: (total_hours, total_wages, days_worked)
    """
    try:
        total_hours = 0
        total_wages = 0
        days_worked = 0

        while total_hours < max_hours and days_worked < max_days:
            daily_hours, daily_wage = calculate_daily_wage()
            total_hours += daily_hours
            total_wages += daily_wage
            days_worked += 1

        print(f"Total Hours Worked: {total_hours}")
        print(f"Total Wages Earned: {total_wages}")
        print(f"Total Days Worked: {days_worked}")

        return total_hours, total_wages, days_worked

    except Exception as e:
        print(f"Error in calculate_wages_until_limit(): {e}")
        return 0, 0, 0  # Default to zero values in case of error

if __name__ == "__main__":
    calculate_wages_until_limit()
