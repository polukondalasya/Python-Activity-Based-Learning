# Question 8: Manufacturing Cost and Profitability Analysis

## 1. Aim
To calculate manufacturing costs, total sales, profit or loss, and check whether the required profit target is achieved.

## 2. Input
- Number of products
- Product name
- Quantity
- Material cost
- Labour cost
- Wastage cost
- Machine cost
- Selling price per product
- Required profit percentage

## 3. Process
- Read the product details.
- Add material, labour, wastage, and machine costs.
- Calculate total sales using selling price × quantity.
- Calculate profit or loss.
- Calculate profit percentage.
- Compare profit percentage with the required target.

## 4. Output
- Product name
- Total manufacturing cost
- Total sales
- Profit or loss
- Profit percentage
- Profit target status

## 5. Algorithm
1. Start.
2. Read the number of products.
3. Repeat for each product.
4. Read product details and costs.
5. Calculate total manufacturing cost.
6. Calculate total sales.
7. Calculate profit or loss.
8. Calculate profit percentage.
9. Check whether the profit target is achieved.
10. Display the results.
11. Stop.

## 6. Flowchart
Start → Input product details → Calculate total cost → Calculate total sales → Calculate profit → Calculate profit percentage → Check profit target → Display result → Stop.

## 7. Pseudocode
```text
START
INPUT number of products

FOR each product
    INPUT name, quantity
    INPUT material, labour, wastage, machine costs
    INPUT selling price and target percentage

    total_cost = material + labour + wastage + machine
    total_sales = selling_price * quantity
    profit = total_sales - total_cost
    profit_percentage = (profit / total_cost) * 100

    IF profit_percentage >= target
        DISPLAY "Profit Target Achieved"
    ELSE
        DISPLAY "Profit Target Not Achieved"
    END IF

    DISPLAY results
END FOR

STOP
```

## 8. Test Cases

| Test | Total Cost | Sales | Target | Expected Result |
|---|---:|---:|---:|---|
| 1 | ₹8,000 | ₹10,000 | 20% | Achieved (25%) |
| 2 | ₹8,000 | ₹9,000 | 20% | Not achieved (12.5%) |
| 3 | ₹8,000 | ₹8,000 | 10% | Not achieved (0%) |