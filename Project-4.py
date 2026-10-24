#Examination Result and Grace-Mark Validation(11th)
marks = []

for i in range(3):
    mark = int(input("Enter marks for subject " + str(i + 1) + ": "))
    marks.append(mark)

valid = True

for mark in marks:
    if mark < 0 or mark > 100:
        valid = False

if not valid:
    print("Invalid marks. Enter marks between 0 and 100.")
else:
    final_marks = []

    for mark in marks:
        if mark < 40 and 40 - mark <= 5:
            mark = 40

        final_marks.append(mark)

    print("Final marks:", final_marks)

    if all(mark >= 40 for mark in final_marks):
        print("Result: PASS")
    else:
        print("Result: FAIL")

    print("Total marks:", sum(final_marks))
    print("Percentage:", round(sum(final_marks) / 3, 2), "%")
