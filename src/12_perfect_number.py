def is_perfect(n):
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n


print(is_perfect(6))  # True
print(is_perfect(28))  # True
print(is_perfect(21))  # ralph age :)
print(is_perfect(22))  # nympha age :>
