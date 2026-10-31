# Question 10: Campus Event Financial Planning

## 1. Aim
To calculate the total expenses, income, and profit or loss of a campus event.

## 2. Input
- Number of expense items
- Expense name and amount
- Total event income
- Expected profit

## 3. Process
The program adds all expenses, calculates profit or loss by subtracting expenses from income, and checks whether the expected profit target is achieved.

## 4. Output
- Total expenses
- Total income
- Profit or loss
- Financial target achieved or not achieved

## 5. Algorithm
1. Start the program.
2. Enter the number of expense items.
3. Read each expense name and amount.
4. Add all expenses.
5. Enter total event income.
6. Enter expected profit.
7. Calculate profit or loss.
8. Check whether the profit meets the target.
9. Display the financial report.
10. Stop.

## 6. Flowchart
Start → Enter expenses → Calculate total expenses → Enter income and target → Calculate profit/loss → Check target → Display report → Stop.

## 7. Pseudocode
```text
START
INPUT number of expense items
SET total_expenses = 0

FOR each expense
    INPUT expense name and amount
    ADD amount to total_expenses
END FOR

INPUT income
INPUT expected profit

profit = income - total_expenses

DISPLAY total expenses
DISPLAY income
DISPLAY profit

IF profit >= expected profit
    DISPLAY "Financial Target Achieved"
ELSE
    DISPLAY "Financial Target Not Achieved"
END IF

STOP
```

## 8. Test Cases

| Test | Expenses | Income | Expected Profit | Expected Result |
|---|---:|---:|---:|---|
| 1 | ₹18,000 | ₹25,000 | ₹5,000 | Target Achieved |
| 2 | ₹20,000 | ₹22,000 | ₹5,000 | Target Not Achieved |
| 3 | ₹10,000 | ₹10,000 | ₹0 | Target Achieved |