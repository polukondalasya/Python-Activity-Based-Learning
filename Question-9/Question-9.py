
print("Multi-Currency Travel Budget Analysis")

n = int(input("Enter number of expense categories: "))
budget = float(input("Enter your travel budget in Rs.: "))

total_expense = 0
largest_expense = 0
largest_category = ""

for i in range(n):
    print("\nExpense", i + 1)

    category = input("Enter expense category: ")
    amount = float(input("Enter amount in foreign currency: "))
    rate = float(input("Enter exchange rate: "))
    fee_percent = float(input("Enter conversion fee percentage: "))

    converted = amount * rate
    fee = converted * fee_percent / 100
    final_amount = converted + fee

    total_expense = total_expense + final_amount

    if final_amount > largest_expense:
        largest_expense = final_amount
        largest_category = category

    print("Converted Amount: Rs.", converted)
    print("Conversion Fee: Rs.", fee)
    print("Final Expense: Rs.", final_amount)

print("\n----- TRAVEL BUDGET REPORT -----")
print("Total Expense: Rs.", total_expense)
print("Travel Budget: Rs.", budget)
print("Largest Expense Category:", largest_category)

if total_expense <= budget:
    print("Within Budget")
else:
    print("Budget Exceeded")
