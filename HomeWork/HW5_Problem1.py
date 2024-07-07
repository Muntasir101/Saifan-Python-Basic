def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


principal = float(input("Enter The Principal Amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time(years): "))

simple_interest = calculate_simple_interest(principal, rate, time)

threshold_amount = float(input("Enter the threshold Amount: "))

if simple_interest > threshold_amount:
    print(f"The simple interest is ${simple_interest}, which is above the threshold amount: ${threshold_amount}")
else:
    print(f"The simple interest is ${simple_interest}, which is not above the threshold amount: ${threshold_amount}")