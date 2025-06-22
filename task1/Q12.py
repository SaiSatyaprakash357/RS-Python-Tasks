# 12. Write a function to check if a string is a palindrome,
#     without using slicing or Python built-ins that reverse strings.

def is_palindrome(s):
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            return False
    return True
