
n = int(input("Enter number of employees: "))

for i in range(n):
    print("\nEmployee", i + 1)

    name = input("Enter employee name: ")
    basic = float(input("Enter basic salary: "))
    allowance = float(input("Enter allowance: "))
    overtime = float(input("Enter overtime amount: "))
    incentive = float(input("Enter incentive: "))

    gross = basic + allowance + overtime + incentive

    if gross <= 20000:
        deduction = gross * 5 / 100
    elif gross <= 50000:
        deduction = gross * 10 / 100
    else:
        deduction = gross * 15 / 100

    net_salary = gross - deduction

    print("\nEmployee Name:", name)
    print("Gross Salary: Rs.", gross)
    print("Deduction: Rs.", deduction)
    print("Net Salary: Rs.", net_salary)
