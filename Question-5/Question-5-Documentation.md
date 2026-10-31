# Question 5: Multi-Plan Telecommunications Cost Optimization

## 1. Aim
To compare different mobile plans and find the most economical plan based on data usage, validity, and budget.

## 2. Input
- Required data usage in GB
- Required validity days
- Budget

## 3. Process
1. Read the user's data usage, validity, and budget.
2. Store mobile plan details.
3. Calculate extra data usage.
4. Calculate extra charges.
5. Calculate total plan cost.
6. Check validity and budget.
7. Select the cheapest eligible plan.

## 4. Output
Display each mobile plan's total cost and the best suitable plan.

## 5. Algorithm
1. Start.
2. Read data usage, validity, and budget.
3. Store mobile plan details.
4. Repeat for each plan.
5. Calculate extra data and extra charges.
6. Calculate total cost.
7. Check whether the plan satisfies validity and budget.
8. Find the lowest-cost eligible plan.
9. Display the best plan and its cost.
10. Stop.

## 6. Flowchart
Start → Input Usage, Validity and Budget → Check Mobile Plans → Calculate Extra Charges → Calculate Total Cost → Check Eligibility → Select Cheapest Plan → Display Result → Stop

## 7. Pseudocode
```text
START
INPUT usage, days, budget

SET best_plan = empty
SET lowest_cost = large number

FOR each mobile plan
    CALCULATE extra data
    CALCULATE extra charges
    CALCULATE total cost

    IF validity is enough AND total cost <= budget
        IF total cost < lowest_cost
            UPDATE lowest_cost
            UPDATE best_plan
        END IF
    END IF
END FOR

IF best_plan is not empty
    DISPLAY best_plan and lowest_cost
ELSE
    DISPLAY no suitable plan
END IF

STOP
```

## 8. Test Cases

| Test | Usage | Days | Budget | Expected Result |
|---|---:|---:|---:|---|
| 1 | 4 GB | 28 | ₹400 | Standard |
| 2 | 1 GB | 28 | ₹250 | Basic |
| 3 | 8 GB | 56 | ₹500 | No suitable plan |
| 4 | 10 GB | 56 | ₹450 | Premium |

**Sample Input:**
- Usage: 4 GB
- Validity: 28 days
- Budget: ₹400

**Sample Output:**
- Best Plan: Standard
- Final Cost: ₹299