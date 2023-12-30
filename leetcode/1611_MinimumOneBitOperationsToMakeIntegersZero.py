from math import floor, log2
class Solution:
    dp = dict()
    def minimumOneBitOperations(self, n: int) -> int:
        if n in self.dp:
            return self.dp[n]
        
        elif(n == 0):
            result = 0
        
        elif(n == 1):
            result = 1

        else :
            s = lambda x: 2**(x-1)
            k = lambda x: floor(log2(x)) + 1
            m = n - s(k(n))
            result = 2*self.minimumOneBitOperations(s(k(n) - 1)) - self.minimumOneBitOperations(m) + 1
        
        self.dp[n] = result
        return  result
    

# 1000 -> 1001 -> 1011 -> 1010 -> 1110 -> 1111 -> 1101 -> 1100 -> 0100
# 100 -> 101 -> 111 -> 110 -> 010
# 10 -> 11 -> 01
# 1 -> 0

# f(0) = 0
# f(1) = 1
# f(2) = f(1) + 2 = 3
# f(3) = f(2) - 1 = 2
# f(4) = f(2) + f(2) - 1 = 7
# f(5) = f(4) - f(5-4) = 6
# f(6) = f(4) - f(6-4) = 4
# f(7) = f(4) - f(7-4) =
# f(8) = f(4) + f(4) - 1

# for x is integer > 0
# let k(x) is the minimum number of bits to present x in binary format.
# For example:
# k(1) = 2 
# k(2) = 2
# k(3) = 2
# k(4) = 3

# k(x) = floor(log_2(n)) + 1

# let s(x) = for given x which is number of bits in binary format, the minimum number for which we need x binary numbers to present is 2^x-1.
# for example
# s(3) = 4
# s(2) = 2
# s(5) = 16

# s(x) = 2^(x-1)

# for given n > 0,
# turn into binary format (k(n) numbers in binary format) 
# let m = n - s(k(n)) is the number remaining after removing the most significant bit
# let turn m to s(k(n) - 1)  how many operaters do i need?
# f(s(k(n) - 1)) - f(m) + 1 + 

# for example n = 13
# n = 1101 , k(n) = 4 , s(4) = 8 = 1000
# 1101 -> 101, m = 101
# how many operators do i need 101 to 100 (m -> s(k(n) - 1)) (then to get f(n) i need f(4))
# f(100) - f(101) + f(4) + 1 
# 2*f(s(k(n) - 1)) - f(m) + 1



solution = Solution()
print(solution.minimumOneBitOperations(3)) #2
print(solution.minimumOneBitOperations(6)) #4
print(solution.minimumOneBitOperations(4)) #7
print(solution.minimumOneBitOperations(8)) #15




