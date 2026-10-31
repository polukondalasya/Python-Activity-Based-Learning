# Question 4: Employee Payroll and Deduction Analysis

## 1. Aim
To calculate the employee's gross salary, deductions, and net salary using Python.

## 2. Input
- Employee name
- Basic salary
- Allowance
- Overtime amount
- Incentive

## 3. Process
1. Read employee details.
2. Add basic salary, allowance, overtime, and incentive.
3. Calculate gross salary.
4. Apply deduction based on gross salary:
   - Up to ₹20,000: 5%
   - ₹20,001 to ₹50,000: 10%
   - Above ₹50,000: 15%
5. Subtract deduction from gross salary to get net salary.

## 4. Output
Display employee name, gross salary, deduction, and net salary.

## 5. Algorithm
1. Start.
2. Read the number of employees.
3. Read employee details.
4. Calculate gross salary.
5. Check the gross salary and calculate deduction.
6. Calculate net salary.
7. Display the salary details.
8. Repeat for all employees.
9. Stop.

## 6. Flowchart

Start → Input Employee Details → Calculate Gross Salary → Calculate Deduction → Calculate Net Salary → Display Salary Details → Stop

## 7. Pseudocode
```text
START
INPUT number of employees

FOR each employee
    INPUT name, basic salary
    INPUT allowance, overtime, incentive

    gross = basic + allowance + overtime + incentive

    IF gross <= 20000
        deduction = gross * 5 / 100
    ELSE IF gross <= 50000
        deduction = gross * 10 / 100
    ELSE
        deduction = gross * 15 / 100
    END IF

    net_salary = gross - deduction

    DISPLAY name, gross, deduction, net_salary
END FOR

STOP
```

## 8. Test Cases

| Test | Gross Salary | Expected Deduction | Net Salary |
|---|---:|---:|---:|
| 1 | ₹15,000 | ₹750 (5%) | ₹14,250 |
| 2 | ₹25,000 | ₹2,500 (10%) | ₹22,500 |
| 3 | ₹60,000 | ₹9,000 (15%) | ₹51,000 |

**Sample Input:**  
Name: Lasya  
Basic: ₹20,000  
Allowance: ₹3,000  
Overtime: ₹1,000  
Incentive: ₹1,000  

**Sample Output:**  
Gross Salary: ₹25,000  
Deduction: ₹2,500  
Net Salary: ₹22,500