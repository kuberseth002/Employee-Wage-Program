import random

def emp_attd():
    randnumber = random.random()
    threshold = 0.5
    if randnumber < threshold:
        print("absent")
        return 0
    else:
        print("present")
        return 1

total_hours = 0
max_hours = 160
max_days = 20
current_day = 0

def calculate_wages():
    global total_hours, current_day  
    worktype = random.randint(0, 2)  
    part_time_work = 4
    full_time_work = 8
    wages_per_hour = 20
    total_wages = 0

    current_day += 1 
    print(f"\nDay {current_day}:")
    absent_or_present = emp_attd()

    if absent_or_present == 1:
        if worktype == 0:
            print("No work today")
            total_wages = 0
            print(f"Total wages: {total_wages}")
        elif worktype == 1:
            if total_hours + part_time_work <= max_hours:
                total_hours += part_time_work
                total_wages = part_time_work * wages_per_hour
                print(f"Part-time work: {part_time_work} hours")
                print(f"Total wages: {total_wages}")
            else:
                remaining_hours = max_hours - total_hours
                total_hours += remaining_hours
                total_wages = remaining_hours * wages_per_hour
                print(f"Partial part-time work: {remaining_hours} hours")
                print(f"Total wages: {total_wages}")
        elif worktype == 2:
            if total_hours + full_time_work <= max_hours:
                total_hours += full_time_work
                total_wages = full_time_work * wages_per_hour
                print(f"Full-time work: {full_time_work} hours")
                print(f"Total wages: {total_wages}")
            else:
                remaining_hours = max_hours - total_hours
                total_hours += remaining_hours
                total_wages = remaining_hours * wages_per_hour
                print(f"Partial full-time work: {remaining_hours} hours")
                print(f"Total wages: {total_wages}")
        else:
            print("Invalid input")

while total_hours < max_hours and current_day < max_days:
    calculate_wages()

print(f"Total hours worked: {total_hours}")
print(f"Total days worked: {current_day}")
