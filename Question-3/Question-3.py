
n = int(input("Enter number of patients: "))

for i in range(n):
    print("\nPatient", i + 1)

    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))

    consultation = float(input("Enter consultation charge: "))
    diagnostic = float(input("Enter diagnostic charge: "))
    treatment = float(input("Enter treatment charge: "))

    total = consultation + diagnostic + treatment

    if age >= 60:
        discount = total * 10 / 100
    else:
        discount = 0

    bill = total - discount

    print("\nPatient Name:", name)
    print("Total Bill: Rs.", total)
    print("Concession: Rs.", discount)
    print("Final Bill: Rs.", bill)

    if bill <= 1000:
        print("Payment Category: Low")
    elif bill <= 5000:
        print("Payment Category: Medium")
    else:
        print("Payment Category: High")
