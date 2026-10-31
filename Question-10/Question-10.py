
print("Campus Event Financial Planning")

n = int(input("Enter number of expense items: "))

total_expenses = 0

for i in range(n):
    print("\nExpense", i + 1)

    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: "))

    total_expenses = total_expenses + amount

income = float(input("\nEnter total event income: "))
target = float(input("Enter expected profit: "))

profit = income - total_expenses

print("\n----- EVENT FINANCIAL REPORT -----")
print("Total Expenses: Rs.", total_expenses)
print("Total Income: Rs.", income)
print("Profit/Loss: Rs.", profit)

if profit >= target:
    print("Financial Target Achieved")
else:
    print("Financial Target Not Achieved")
