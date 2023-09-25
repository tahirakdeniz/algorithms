def isSubsequence(s:str, t:str) -> bool:
    if len(s) == 0:
        return True
    j = 0
    for i in range(len(t)):
        if s[j] == t[i]:
            j+=1
        if j == len(s):
            return True
    return False

if __name__ == '__main__':
    assert isSubsequence("abc", "ahbgdc") == True
    assert isSubsequence("axc", "ahbgdc") == False