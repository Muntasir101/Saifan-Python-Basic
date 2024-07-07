number1 = int(input("Enter the First Number: "))
number2 = int(input("Enter the Second Number: "))
number3 = int(input("Enter the Third Number: "))
number4 = int(input("Enter the Fourth Number: "))
number5 = int(input("Enter the Fifth Number: "))

largest = max(number1, number2, number3, number4, number5)
smallest = min(number1, number2, number3, number4)

print(f"Largest Number is: {largest}")
print(f"Smallest Number is: {smallest}")