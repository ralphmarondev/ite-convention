def find_missing_number(nums):
    n = len(nums) + 1
    total = n * (n + 1) // 2
    return total - sum(nums)


print(find_missing_number([1, 2, 3, 5])) # 4
