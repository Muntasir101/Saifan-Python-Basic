import math


def is_prime():
    number = int(input("Please Enter a number:"))
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % 1 == 0:
            return False
    return True


print(is_prime())
