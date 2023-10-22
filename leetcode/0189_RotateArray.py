from typing import List

def rotate(nums: List[int], k: int) -> None: #O(n*k)
    for i in range(k):
        last = nums.pop() # O(1)
        nums.insert(0, last) #O(n)

def reverse(nums, i, j):
    li = i
    ri = j
        
    while li < ri:
        nums[li], nums[ri] = nums[ri], nums[li]        
        li += 1
        ri -= 1
        

def rotate2(nums: List[int], k: int) -> None:
    lenNums = len(nums)
    k = k%lenNums
    if(k < 0):
        k += lenNums
        
    reverse(nums, 0, lenNums - k - 1)
    reverse(nums, lenNums - k, lenNums - 1)
    reverse(nums, 0, lenNums - 1)


rotateFunc = rotate2

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotateFunc(nums, k)
print(nums)

nums = [-1,-100,3,99]
k = 2
rotateFunc(nums, k)
print(nums)