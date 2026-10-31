# Question 1: University Scholarship Allocation

### 1. Aim
To write a Python program to check whether a student gets a scholarship or not.

### 2. Input
- Student name
- Marks
- Attendance
- Family income

### 3. Process
First, we enter the student details. Then the program checks marks, attendance and family income using if-else conditions.

### 4. Output
It displays whether the student is eligible or not eligible for the scholarship.

### 5. Algorithm
1. Start the program.
2. Enter student details.
3. Check marks are 75 or above.
4. Check attendance is 75 or above.
5. Check income is below ₹2,00,000.
6. If all conditions are true, print Eligible.
7. Otherwise, print Not Eligible.
8. Stop the program.

### 6. Pseudocode
```text
START
Enter student details
IF marks >= 75 AND attendance >= 75 AND income <= 200000
    PRINT Eligible
ELSE
    PRINT Not Eligible
STOP
```

### 7. Flowchart
```text
       START
         |
   Enter Details
         |
   Check Conditions
         |
    All Correct?
      /     \
    Yes      No
     |        |
  Eligible  Not Eligible
      \      /
        STOP
```

### 8. Sample Input

Enter number of students: 1
Enter student name: Lasya
Enter marks: 95
Enter attendance: 98
Enter family income: 98000


### 9. Sample Output
Lasya is Eligible for Scholarship

### 10. Conclusion
I successfully completed this program using a for loop and if-else conditions.