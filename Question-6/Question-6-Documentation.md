# Question 6: Railway Fare and Reservation Calculator

## 1. Aim
To calculate railway ticket fares for passengers based on distance, travel class, age concession, reservation fee, and cancellation penalty.

## 2. Input
- Number of passengers
- Passenger name
- Passenger age
- Travel distance
- Travel class (Sleeper or AC)
- Cancellation choice (yes/no)

## 3. Process
1. Read passenger details.
2. Calculate fare based on distance.
3. Double the fare for AC class.
4. Apply 20% concession for passengers aged 60 or above.
5. Add reservation fee of ₹50.
6. Calculate total fare.
7. If the ticket is cancelled, calculate 10% cancellation penalty and refund amount.

## 4. Output
Display passenger name, ticket fare, reservation fee, total fare, cancellation penalty, and refund amount when applicable.

## 5. Algorithm
1. Start.
2. Read the number of passengers.
3. Read passenger details.
4. Calculate fare based on distance.
5. Check travel class.
6. Apply age concession if eligible.
7. Add reservation fee.
8. Display total fare.
9. Check cancellation choice.
10. Calculate penalty and refund if cancelled.
11. Repeat for all passengers.
12. Stop.

## 6. Flowchart
Start → Input Passenger Details → Calculate Distance Fare → Check Travel Class → Apply Age Concession → Add Reservation Fee → Display Total Fare → Check Cancellation → Display Penalty and Refund or Confirm Ticket → Stop

## 7. Pseudocode
```text
START
INPUT number of passengers

FOR each passenger
    INPUT name, age, distance
    INPUT travel class

    IF distance <= 100
        fare = distance * 1
    ELSE
        fare = 100 + (distance - 100) * 2
    END IF

    IF travel class is AC
        fare = fare * 2
    END IF

    IF age >= 60
        fare = fare - fare * 20 / 100
    END IF

    total = fare + 50
    DISPLAY total

    INPUT cancellation choice

    IF cancellation choice is yes
        penalty = total * 10 / 100
        refund = total - penalty
        DISPLAY penalty and refund
    ELSE
        DISPLAY ticket confirmed
    END IF
END FOR

STOP
```

## 8. Test Cases

| Test | Age | Distance | Class | Cancellation | Expected Total Fare |
|---|---:|---:|---|---|---:|
| 1 | 65 | 150 km | Sleeper | No | ₹210 |
| 2 | 30 | 50 km | Sleeper | No | ₹100 |
| 3 | 30 | 150 km | AC | No | ₹450 |
| 4 | 65 | 150 km | Sleeper | Yes | ₹210 |

**Sample Input:**
- Passenger name: Lasya
- Age: 65
- Distance: 150 km
- Class: Sleeper (1)
- Cancel ticket: no

**Sample Output:**
- Ticket Fare: ₹160
- Reservation Fee: ₹50
- Total Fare: ₹210
- Ticket Confirmed