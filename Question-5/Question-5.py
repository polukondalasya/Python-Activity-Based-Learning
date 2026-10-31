
print("Mobile Plan Comparison")

usage = float(input("Enter required data in GB: "))
days = int(input("Enter required validity days: "))
budget = float(input("Enter your budget: "))

plans = [
    ("Basic", 199, 2, 28, 50),
    ("Standard", 299, 5, 28, 40),
    ("Premium", 399, 10, 56, 30)
]

best_plan = ""
lowest_cost = 999999

for name, price, data, validity, extra_rate in plans:

    extra_data = usage - data

    if extra_data < 0:
        extra_data = 0

    extra_charge = extra_data * extra_rate
    total_cost = price + extra_charge

    print("\nPlan:", name)
    print("Total Cost: Rs.", total_cost)

    if validity >= days and total_cost <= budget:
        if total_cost < lowest_cost:
            lowest_cost = total_cost
            best_plan = name

if best_plan != "":
    print("\nBest Plan:", best_plan)
    print("Final Cost: Rs.", lowest_cost)
else:
    print("\nNo suitable plan found")
