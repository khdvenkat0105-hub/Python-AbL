#Food Waste Monitoring System(53rd)
days = int(input("Enter number of days: "))
limit = float(input("Enter acceptable wastage percentage: "))

if days <= 0 or limit < 0 or limit > 100:
    print("Invalid input")
else:
    for i in range(days):
        print("\nDay", i + 1)

        prepared = int(input("Enter meals prepared: "))
        served = int(input("Enter meals served: "))

        if prepared <= 0 or served < 0 or served > prepared:
            print("Invalid meal details")
        else:
            leftover = prepared - served
            wastage = leftover / prepared * 100

            print("Meals leftover:", leftover)
            print("Wastage percentage:", round(wastage, 2), "%")

            if wastage > limit:
                print("Warning: Excessive food waste")
            else:
                print("Food waste is within the limit")
