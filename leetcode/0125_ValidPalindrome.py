def checkPalindrome(s: str) -> bool:
    i = 0
    j = len(s) - 1
    while i <= j:
        if s[i] != s[j]:
            return False
        
        i += 1
        j -= 1
    return True

def isPalindrome(s: str) -> bool:
    s = ''.join(filter(str.isalnum, input)).lower()
    return checkPalindrome(s)
