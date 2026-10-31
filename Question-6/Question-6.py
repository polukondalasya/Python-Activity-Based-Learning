
n = int(input("Enter number of passengers: "))

for i in range(n):
    print("\nPassenger", i + 1)

    name = input("Enter passenger name: ")
    age = int(input("Enter age: "))
    distance = float(input("Enter travel distance in km: "))

    print("1. Sleeper")
    print("2. AC")

    choice = int(input("Choose travel class: "))

    if distance <= 100:
        fare = distance * 1
    else:
        fare = 100 + (distance - 100) * 2

    if choice == 2:
        fare = fare * 2

    if age >= 60:
        fare = fare - fare * 20 / 100

    reservation = 50
    total = fare + reservation

    print("\nPassenger Name:", name)
    print("Ticket Fare: Rs.", fare)
    print("Reservation Fee: Rs.", reservation)
    print("Total Fare: Rs.", total)

    cancel = input("Cancel ticket? (yes/no): ")

    if cancel == "yes":
        penalty = total * 10 / 100
        refund = total - penalty

        print("Cancellation Penalty: Rs.", penalty)
        print("Refund Amount: Rs.", refund)
    else:
        print("Ticket Confirmed")
