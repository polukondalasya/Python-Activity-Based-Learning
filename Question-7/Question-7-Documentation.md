# Question 7: Retail Billing with Multiple Discount Rules

## 1. Aim
To calculate the total shopping bill by applying product taxes and discounts.

## 2. Input
- Number of products
- Product name
- Product category
- Product price
- Product quantity

## 3. Process
1. Read the number of products.
2. Enter product details.
3. Calculate amount using price × quantity.
4. Calculate tax based on product category.
5. Calculate subtotal and total tax.
6. Apply a 10% discount if subtotal is ₹2,000 or more.
7. Limit the maximum discount to ₹500.
8. Calculate and display the final bill.

## 4. Output
Display subtotal, total tax, discount, and final bill.

## 5. Algorithm
1. Start.
2. Read number of products.
3. Set subtotal and total tax to zero.
4. Read product details.
5. Calculate product amount.
6. Calculate tax based on category.
7. Add amount and tax to totals.
8. Check discount condition.
9. Calculate final bill.
10. Display bill details.
11. Stop.

## 6. Flowchart
Start → Input Products → Calculate Amount → Calculate Category Tax → Calculate Subtotal and Tax → Check Discount → Calculate Final Bill → Display Bill → Stop

## 7. Pseudocode
```text
START
INPUT number of products

SET subtotal = 0
SET total_tax = 0

FOR each product
    INPUT name, category, price, quantity
    amount = price * quantity
    subtotal = subtotal + amount

    IF category is food
        tax = amount * 5 / 100
    ELSE IF category is clothing
        tax = amount * 12 / 100
    ELSE
        tax = amount * 18 / 100
    END IF

    total_tax = total_tax + tax
END FOR

IF subtotal >= 2000
    discount = subtotal * 10 / 100
    IF discount > 500
        discount = 500
    END IF
ELSE
    discount = 0
END IF

final_bill = subtotal + total_tax - discount
DISPLAY subtotal, total_tax, discount, final_bill

STOP
```

## 8. Test Cases

| Test | Subtotal | Tax | Discount | Final Bill |
|---|---:|---:|---:|---:|
| 1 | ₹3,000 | ₹410 | ₹300 | ₹3,110 |
| 2 | ₹1,000 | ₹50 | ₹0 | ₹1,050 |
| 3 | ₹6,000 | ₹1,080 | ₹500 | ₹6,580 |

**Sample Input:**
- Rice: ₹1,000, Food, Quantity 1
- Mobile: ₹2,000, Electronics, Quantity 1

**Sample Output:**
- Subtotal: ₹3,000
- Total Tax: ₹410
- Discount: ₹300
- Final Bill: ₹3,110