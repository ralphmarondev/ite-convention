def product_except_self(nums):
    result = [1] * len(nums)

    left = 1
    for i in range(len(nums)):
        result[i] = left
        left *= nums[i]

    right = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= right
        right *= nums[i]
    return result


print(product_except_self([1, 2, 3, 4]))
