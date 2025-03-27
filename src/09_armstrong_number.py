def is_armstrong(n):
    digits = [int(digit) for digit in str(n)]
    return sum(digit ** len(digits) for digit in digits) == n


print(is_armstrong(153))  # True
print(is_armstrong(123))  # False
