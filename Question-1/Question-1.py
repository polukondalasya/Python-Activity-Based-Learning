
n = int(input("Enter number of students: "))

for i in range(n):

    print("nStudent", i + 1)

    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    attendance = int(input("Enter attendance: "))
    income = int(input("Enter family income: "))

    if marks >= 75 and attendance >= 75 and income <= 200000:
        print(name, "is Eligible for Scholarship")

    else:
        print(name, "is Not Eligible for Scholarship")
