def checkHasDuplicatedValue(list):
    hasValue = set()
    for i in range(len(list)):
        if list[i] in hasValue: # O(1)
            return True
        hasValue.add(list[i]) # O(1)
    return False