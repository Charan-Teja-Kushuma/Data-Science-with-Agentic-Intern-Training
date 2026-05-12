def ExpenseManager(Amount,StudentName):
    
    Expense= {
        "Amount": Amount,
        "StudentName": StudentName
    }
    return Expense
     
Amount1 = input("Enter the amount you spend on this month: ")
StudentName1 = input("Enter your name: ")
print(Amount1,StudentName1)

x = ExpenseManager(Amount,StudentName)
print(x)

