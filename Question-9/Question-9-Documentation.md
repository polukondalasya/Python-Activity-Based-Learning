# Question 9: Multi-Currency Travel Budget Analysis

## 1. Aim
To convert foreign travel expenses into Indian Rupees, calculate conversion fees, compare expenses with the budget, and identify the largest expense category.

## 2. Input
- Number of expense categories
- Travel budget in Rupees
- Expense category
- Foreign currency amount
- Exchange rate
- Conversion fee percentage

## 3. Process
- Read the travel budget.
- Read expense details.
- Convert foreign currency into Indian Rupees.
- Calculate the conversion fee.
- Add the fee to the converted amount.
- Calculate total expenses.
- Identify the largest expense category.
- Compare total expenses with the budget.

## 4. Output
- Converted amount
- Conversion fee
- Final expense for each category
- Total expense
- Travel budget
- Largest expense category
- Budget status

## 5. Algorithm
1. Start.
2. Read the number of expense categories.
3. Read the travel budget.
4. Set total expense to zero.
5. Repeat for each expense category.
6. Read category, amount, exchange rate, and fee percentage.
7. Calculate converted amount.
8. Calculate conversion fee.
9. Calculate final expense.
10. Add final expense to total expense.
11. Identify the largest expense category.
12. Compare total expense with the budget.
13. Display the report.
14. Stop.

## 6. Flowchart
Start → Input budget and expense details → Convert currency → Calculate conversion fee → Calculate final expense → Update total expense → Identify largest category → Compare with budget → Display report → Stop.

## 7. Pseudocode
```text
START
INPUT number of categories
INPUT budget

total_expense = 0
largest_expense = 0

FOR each category
    INPUT category, amount, rate, fee_percent

    converted = amount * rate
    fee = converted * fee_percent / 100
    final_amount = converted + fee

    total_expense = total_expense + final_amount

    IF final_amount > largest_expense
        largest_expense = final_amount
        largest_category = category
    END IF
END FOR

IF total_expense <= budget
    DISPLAY "Within Budget"
ELSE
    DISPLAY "Budget Exceeded"
END IF

DISPLAY total expense and largest category
STOP
```

## 8. Test Cases

| Test | Total Expense | Budget | Expected Result |
|---|---:|---:|---|
| 1 | ₹13,056 | ₹15,000 | Within Budget |
| 2 | ₹13,056 | ₹10,000 | Budget Exceeded |
| 3 | ₹8,466 | ₹9,000 | Within Budget |

**Sample calculation:** Hotel = ₹8,466; Food = ₹4,590; Total = ₹13,056. Largest category = Hotel.