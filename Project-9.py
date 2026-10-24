#Student Marks Matrix Analysis(42nd)
marks = []

n = int(input("Enter number of students: "))

for i in range(n):
    student_marks = []

    print("Enter marks for student", i + 1)

    for j in range(3):
        mark = int(input("Enter marks for subject " + str(j + 1) + ": "))
        student_marks.append(mark)

    marks.append(student_marks)

if n <= 0:
    print("Invalid number of students")
else:
    totals = []

    for i in range(n):
        total = sum(marks[i])
        average = total / 3
        totals.append(total)

        print("\nStudent", i + 1)
        print("Marks:", marks[i])
        print("Total:", total)
        print("Average:", round(average, 2))

    highest = max(totals)
    topper = totals.index(highest) + 1

    print("\nTop student: Student", topper)
    print("Highest total:", highest)
