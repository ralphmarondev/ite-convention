def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


print(fibonacci(6))  # 8 (0, 1, 1, 2, 3, 5, 8)
