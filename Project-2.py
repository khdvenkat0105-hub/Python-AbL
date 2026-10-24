#Employee Payroll and Deduction Analysis(4th)
basic = float(input("Enter basic salary: Rs. "))
allowances = float(input("Enter allowances: Rs. "))
overtime = float(input("Enter overtime amount: Rs. "))
incentives = float(input("Enter incentives: Rs. "))

if basic < 0 or allowances < 0 or overtime < 0 or incentives < 0:
    print("Invalid salary details")
else:
    gross_salary = basic + allowances + overtime + incentives

    if gross_salary <= 20000:
        deduction = gross_salary * 0.05
    elif gross_salary <= 40000:
        deduction = gross_salary * 0.10
    else:
        deduction = gross_salary * 0.15

    net_salary = gross_salary - deduction

    print("Gross salary: Rs.", round(gross_salary, 2))
    print("Deduction: Rs.", round(deduction, 2))
    print("Net salary: Rs.", round(net_salary, 2))
