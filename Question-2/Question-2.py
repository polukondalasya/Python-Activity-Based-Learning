
n = int(input("Enter number of months: "))

previous_bill = 0

for i in range(n):
    print("\nMonth", i + 1)
    units = int(input("Enter electricity units: "))

    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = 100 * 2 + (units - 100) * 3
    else:
        bill = 100 * 2 + 100 * 3 + (units - 200) * 5

    bill = bill + 50

    if units <= 100:
        bill = bill - 20

    if bill > 1000:
        bill = bill + bill * 5 / 100

    print("Electricity Bill: Rs.", bill)

    if i > 0:
        increase = bill - previous_bill

        if increase > previous_bill * 20 / 100:
            print("Unusual increase in bill")
        else:
            print("Normal bill")

    previous_bill = bill
