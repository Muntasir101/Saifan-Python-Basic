# monthly expense
january_expense = 4000
february_expense = 3000
march_expense = 3500
april_expense = 5000
may_expense = 5500
june_expense = 2500
july_expense = 4500
august_expense = 3000
september_expense = 4500
october_expense = 6500
november_expense = 7000
december_expense = 10000

# total
total_expense = (january_expense + february_expense + march_expense + april_expense +
                 may_expense + june_expense + july_expense + august_expense + september_expense +
                 october_expense + november_expense + december_expense)

# addition
print("Total Expenses: ", total_expense)  # 59000

# division
# Average Expenses:  4916.666666666667
# 4917
average_monthly_expenses = round(total_expense / 12)
print("Average Expenses: ", average_monthly_expenses)  # 4916.666666666667

# floor division
average_monthly_expenses_floor = total_expense // 12
print("Average Expenses Floor: ", average_monthly_expenses_floor)  # 4916
