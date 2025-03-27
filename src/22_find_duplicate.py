def find_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return None


print(find_duplicate([1, 2, 3, 4, 5, 2])) # 2
