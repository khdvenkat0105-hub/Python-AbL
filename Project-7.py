#Student Timetable Conflict Detection(23rd)
# Each tuple contains (subject, day, time)

schedule = [
    ("Python", "Monday", "9 AM"),
    ("Maths", "Monday", "10 AM"),
    ("Physics", "Tuesday", "9 AM"),
    ("English", "Monday", "9 AM")
]

conflict_found = False

for i in range(len(schedule)):
    for j in range(i + 1, len(schedule)):
        subject1, day1, time1 = schedule[i]
        subject2, day2, time2 = schedule[j]

        if day1 == day2 and time1 == time2:
            print("Timetable conflict:")
            print(subject1, "and", subject2)
            print("Day:", day1)
            print("Time:", time1)
            conflict_found = True

if conflict_found == False:
    print("No timetable conflicts found")
