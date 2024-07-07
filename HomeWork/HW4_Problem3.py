"""
a year is a leap if it divisible by 4
However if the year is also divisible by 100, it is not a leap year,unless
the year is divisible by 400, in which case it is a leap year
"""
year = int(input("Enter year: "))

if (year % 4 == 0) and (year % 100 != 0):
    print(f"{year} is a leap year")

elif (year % 400 == 0) and (year % 100 == 0):
    print(f"{year} is a leap year")

else:
    print(f"{year} is a not a leap year")

    """
    2005 % 4 = 

    2058 
    """