def is_palindrome(s):
    return s == s[::-1]


print(is_palindrome('hello'))  # False
print(is_palindrome('pretty'))  # False
print(is_palindrome('nympha'))  # False
