def is_palindrome(line: str) -> bool:
    s = ''.join(filter(str.isalnum, line.lower()))
    for i in range(len(s)):
        if s[i] == s[len(s)-i-1]:
            return True
        else:
            return False


print(is_palindrome(input().strip()))
