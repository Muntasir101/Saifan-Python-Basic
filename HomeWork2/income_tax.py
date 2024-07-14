"""
Tax rate schedule:
0% for income up to $10,000
10% for income up to next $30,000
20% for income up to next $60,000
30% for income up to above $60,000
"""
income = float(input('Enter The Annual Income: '))

if income <= 10000:
    tax = 0
elif income <= 30000:
    tax = (income - 10000) * 0.10
elif income <= 60000:
    tax = (20000 * 0.10) + (income - 30000) * 0.20
else:
    tax = (20000 * 0.10) + (30000 * 0.20) + (income - 60000) * 0.30

print(f"Income tax for amount ${income} is: ${tax}")
