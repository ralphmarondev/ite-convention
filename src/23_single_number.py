# Write a function that finds the element that appears only once in a
# list where every other element appears twice.
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result


print(single_number([4, 1, 2, 1, 2]))  # 4
