from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    i = 0
    j = 0
    while j < n and i < m + n:
        if(i >= m + j):
            nums1[i] = nums2[j]
            i += 1
            j += 1
            continue
        
        if nums1[i] > nums2[j]:
            nums1.insert(i, nums2[j])
            nums1.pop()
            j += 1
        else:
            i += 1
    pass

# case 1
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

merge(nums1, m, nums2, n)
print(nums1)

# case 2
nums1 = [1]
m = 1
nums2 = []
n = 0

merge(nums1, m, nums2, n)
print(nums1)

# case 3
nums1 = [0]
m = 0
nums2 = [1]
n = 1

merge(nums1, m, nums2, n)
print(nums1)