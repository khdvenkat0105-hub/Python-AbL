#Progressive Electricity Bill(2nd)
units = int(input("Enter electricity units consumed: "))

if units < 0:
    print("Invalid units")
else:
    if units <= 100:
        energy_charge = units * 2
    elif units <= 200:
        energy_charge = 100 * 2 + (units - 100) * 3
    else:
        energy_charge = 100 * 2 + 100 * 3 + (units - 200) * 5

    fixed_charge = 50
    surcharge = energy_charge * 0.05
    total_bill = energy_charge + fixed_charge + surcharge

    print("Units consumed:", units)
    print("Energy charge: Rs.", energy_charge)
    print("Fixed charge: Rs.", fixed_charge)
    print("Surcharge: Rs.", surcharge)
    print("Total bill: Rs.", round(total_bill, 2))
