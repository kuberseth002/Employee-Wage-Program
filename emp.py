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
      
total_hours=0

def calculate_wages():
    worktype = random.randint(0, 2)  
    part_time_work = 4
    full_time_work = 8
    wages_per_hour = 20
    total_hours = 0
    total_wages = 0

    absent_or_present = emp_attd()

    if absent_or_present == 1:
        if worktype == 0:
            total_hours += 0
            print("No work today")
            total_wages = 0
            print(f"Total wages: {total_wages}")
        elif worktype == 1:
            total_hours += part_time_work
            total_wages = part_time_work * wages_per_hour
            print(f"Total wages: {total_wages}")
        elif worktype == 2:
            total_hours += full_time_work
            total_wages = full_time_work * wages_per_hour
            print(f"Total wages: {total_wages}")
        else:
            print("Invalid input")
        
    print(f"Total worked so far:{total_hours}")
calculate_wages()