
print("Manufacturing Cost and Profitability Analysis")

n = int(input("Enter number of products: "))

for i in range(n):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))

    material = float(input("Enter material cost: "))
    labour = float(input("Enter labour cost: "))
    wastage = float(input("Enter wastage cost: "))
    machine = float(input("Enter machine cost: "))

    selling_price = float(input("Enter selling price per product: "))
    target = float(input("Enter required profit percentage: "))

    total_cost = material + labour + wastage + machine
    total_sales = selling_price * quantity

    profit = total_sales - total_cost
    profit_percentage = (profit / total_cost) * 100

    print("\nProduct Name:", name)
    print("Total Manufacturing Cost: Rs.", total_cost)
    print("Total Sales: Rs.", total_sales)
    print("Profit/Loss: Rs.", profit)
    print("Profit Percentage:", profit_percentage, "%")

    if profit_percentage >= target:
        print("Profit Target Achieved")
    else:
        print("Profit Target Not Achieved")
