
n = int(input("Enter number of products: "))

subtotal = 0
total_tax = 0

for i in range(n):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    category = input("Enter category (food/clothing/electronics): ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    amount = price * quantity
    subtotal = subtotal + amount

    if category == "food":
        tax = amount * 5 / 100
    elif category == "clothing":
        tax = amount * 12 / 100
    else:
        tax = amount * 18 / 100

    total_tax = total_tax + tax

    print("Product:", name)
    print("Amount: Rs.", amount)
    print("Tax: Rs.", tax)

if subtotal >= 2000:
    discount = subtotal * 10 / 100

    if discount > 500:
        discount = 500
else:
    discount = 0

final_bill = subtotal + total_tax - discount

print("\n----- FINAL BILL -----")
print("Subtotal: Rs.", subtotal)
print("Total Tax: Rs.", total_tax)
print("Discount: Rs.", discount)
print("Final Bill: Rs.", final_bill)
