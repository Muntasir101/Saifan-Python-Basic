original_price = float(input("Enter the original price of the item: "))
sales_tax_rate = float(input("Enter the sales tax rate(As a percentage): "))

# calculate the sales tax amount
sales_tax_amount = (sales_tax_rate/100) * original_price

# calculate the final price after tax
final_price = original_price + sales_tax_amount

# calculate the difference
difference_amount = final_price - original_price

# calculate the difference in percentage
difference_percentage = (difference_amount/original_price) * 100

# print the result
print(f"The original price is: ${original_price}")
print(f"The sales tax amount is ${sales_tax_amount}")
print(f"The final price is: ${final_price}")
print(f"The difference amount is: ${difference_amount}")
print(f"The difference percentage is: ${difference_percentage}")