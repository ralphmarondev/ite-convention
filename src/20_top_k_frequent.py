from collections import Counter


def top_k_frequent(nums, k):
    count = Counter(nums)
    return [item[0] for item in count.most_common(k)]


print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
