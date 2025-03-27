def longest_substring(s):
    start = max_len = 0
    seen = {}

    for end, char in enumerate(s):
        if char in seen and seen[char] >= start:
            start = seen[char] + 1
        seen[char] = end
        max_len = max(max_len, end - start + 1)
    return max_len


print(longest_substring('abcabcbb')) # 3
