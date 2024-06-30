# example: Bucket list
total_money_before_purchase = 2000

phone_price = 100
shoe_price = 200
clothing_price = 200
food_price = 100
transport_cost = 100

# addition
total_expenses = phone_price + shoe_price + clothing_price + food_price + transport_cost
print("Total Expenses: ", total_expenses)

# Multiplication
# condition: 10% discount applicable
discount_amount = total_expenses * 0.10

# subtraction
final_amount = total_expenses - discount_amount
print("Final amount after 10% discount: ", final_amount)

# subtraction
remaining_money = total_money_before_purchase - final_amount
print("Remaining money: ", remaining_money)
