# Question 2: Progressive Electricity Billing

## 1. Aim
To develop a Python program to calculate electricity bills based on units consumed and compare monthly bills to identify unusual increases.

## 2. Input
- Number of months.
- Electricity units consumed in each month.

## 3. Process
1. Get the number of months from the user.
2. Enter electricity units for each month.
3. Calculate the bill using different unit slabs.
4. Add fixed charges.
5. Apply rebate if eligible.
6. Apply surcharge if the bill is above ₹1000.
7. Compare the current bill with the previous month's bill.
8. Display the bill and identify unusual increases.

## 4. Output
- Electricity bill for each month.
- Message showing whether the bill increase is unusual or normal.

## 5. Algorithm
1. Start.
2. Read the number of months.
3. Set previous bill to 0.
4. Read electricity units for each month.
5. Calculate the bill using slab rates.
6. Add fixed charges.
7. Apply rebate and surcharge if eligible.
8. Display the bill.
9. Compare the current bill with the previous bill.
10. Display unusual increase or normal bill.
11. Update the previous bill.
12. Repeat until all months are completed.
13. Stop.

## 6. Flowchart
```text
       START
         |
  Enter number of months
         |
  Set previous_bill = 0
         |
     Enter units
         |
  Calculate slab bill
         |
  Add fixed charges
         |
  Apply rebate
         |
  Apply surcharge
         |
   Display bill
         |
  Compare monthly bills
         |
  Unusual increase?
      /       \
    Yes        No
     |          |
  Display    Display
  Unusual    Normal
      \       /
  Update previous bill
         |
   More months?
      /      \
    Yes       No
     |         |
   Repeat     STOP
```

## 7. Pseudocode
```text
START
INPUT number of months
SET previous_bill = 0

FOR each month:
    INPUT units

    IF units <= 100:
        bill = units * 2
    ELSE IF units <= 200:
        bill = 100 * 2 + (units - 100) * 3
    ELSE:
        bill = 100 * 2 + 100 * 3 + (units - 200) * 5

    ADD fixed charge of 50

    IF units <= 100:
        SUBTRACT rebate of 20

    IF bill > 1000:
        ADD 5% surcharge

    DISPLAY bill

    IF month > 1:
        IF increase > 20% of previous bill:
            DISPLAY "Unusual increase"
        ELSE:
            DISPLAY "Normal bill"

    UPDATE previous_bill

STOP
```

## 8. Test Cases

| Test Case | Number of Months | Units | Expected Output |
|---|---:|---:|---|
| 1 | 1 | 100 | Bill = ₹230 |
| 2 | 1 | 150 | Bill = ₹400 |
| 3 | 1 | 250 | Bill = ₹1102.50 |
| 4 | 2 | 100, 150 | Unusual increase in bill |