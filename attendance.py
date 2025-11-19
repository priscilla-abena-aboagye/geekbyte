student_names = ["Esther", "Evans", "Loiusa", "Mercedes", "Ethel", "Emmanuella", "Benjamin"]
meeting_days = ("Monday", "Tuesday", "Friday", "Saturday")

day = input("Enter the day: ").capitalize()

# checks if day is in meeting days
if day in meeting_days:
    print("Class in session today")
    user_num = int(input("How many people are present?: "))
    present_students = []
    for i in range(user_num): # loops over the inputed number to add and remove name
        name = input("Name of the person: ")
        present_students.append(name) # add name

        if name in student_names:
            student_names.remove(name) # condition to remove name

    print(f"Present Students: {present_students}")
    print(f"Total present: {len(present_students)}")
    print(f"Absent Students: {student_names}")
else:
    print("Class is not in session Today")

