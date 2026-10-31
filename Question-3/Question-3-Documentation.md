# Question 3: Hospital Billing and Patient Classification

## 1. Aim
To develop a Python program to calculate hospital bills using consultation, diagnostic, and treatment charges, apply concessions, and classify patients based on their final bill amount.

## 2. Input
- Number of patients.
- Patient name.
- Patient age.
- Consultation charge.
- Diagnostic charge.
- Treatment charge.

## 3. Process
1. Get the number of patients.
2. Enter patient details.
3. Calculate the total bill by adding consultation, diagnostic, and treatment charges.
4. Check the patient's age.
5. Give a 10% concession if the patient is 60 years or above.
6. Calculate the final bill.
7. Classify the patient based on the final bill amount.
8. Display the bill details.

## 4. Output
- Patient name.
- Total bill amount.
- Concession amount.
- Final bill amount.
- Payment category (Low, Medium, or High).

## 5. Algorithm
1. Start.
2. Read the number of patients.
3. Repeat for each patient:
   - Read patient name and age.
   - Read consultation, diagnostic, and treatment charges.
   - Calculate the total bill.
   - If age is 60 or above, calculate 10% concession.
   - Otherwise, concession is zero.
   - Calculate the final bill.
   - If bill is up to ₹1000, classify as Low.
   - If bill is up to ₹5000, classify as Medium.
   - Otherwise, classify as High.
   - Display the bill details.
4. Stop.

## 6. Flowchart
```text
          START
            |
    Enter number of patients
            |
     Enter patient details
            |
    Enter all three charges
            |
     Calculate total bill
            |
       Age >= 60?
        /       \
      Yes        No
       |          |
 Calculate      Discount
 10% discount    = 0
       \          /
      Calculate final bill
            |
      Bill <= 1000?
        /       \
      Yes        No
       |          |
      Low     Bill <= 5000?
                /     \
              Yes      No
               |        |
            Medium     High
                \      /
          Display bill details
                |
          More patients?
             /     \
           Yes      No
            |        |
          Repeat    STOP
```

## 7. Pseudocode
```text
START

INPUT number of patients

FOR each patient:
    INPUT name
    INPUT age
    INPUT consultation charge
    INPUT diagnostic charge
    INPUT treatment charge

    total = consultation + diagnostic + treatment

    IF age >= 60:
        discount = total * 10 / 100
    ELSE:
        discount = 0

    bill = total - discount

    IF bill <= 1000:
        category = "Low"
    ELSE IF bill <= 5000:
        category = "Medium"
    ELSE:
        category = "High"

    DISPLAY name
    DISPLAY total
    DISPLAY discount
    DISPLAY bill
    DISPLAY category

STOP
```

## 8. Test Cases

| Test Case | Age | Total Charges | Expected Final Bill | Category |
|---|---:|---:|---:|---|
| 1 | 65 | ₹3500 | ₹3150 | Medium |
| 2 | 30 | ₹800 | ₹800 | Low |
| 3 | 45 | ₹6000 | ₹6000 | High |
| 4 | 60 | ₹2000 | ₹1800 | Medium |

**Sample Input for Test Case 1:**
```text
Number of patients: 1
Name: Lasya
Age: 65
Consultation: 500
Diagnostic: 1000
Treatment: 2000
```

**Expected Output:**
```text
Patient Name: Lasya
Total Bill: Rs. 3500
Concession: Rs. 350
Final Bill: Rs. 3150
Payment Category: Medium
```

## 9. Output Screenshot
Insert the saved Question-3 output screenshot here.