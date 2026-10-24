#Attendance Recovery Computation(12th)
attended = int(input("Enter classes attended: "))
total = int(input("Enter total classes conducted: "))
required = 75

if total <= 0 or attended < 0 or attended > total:
    print("Invalid attendance details")
else:
    percentage = attended / total * 100
    print("Current attendance:", round(percentage, 2), "%")

    extra = 0

    while (attended + extra) / (total + extra) * 100 < required:
        extra = extra + 1

    print("Additional classes to attend:", extra)
    print("Total classes after recovery:", total + extra)
