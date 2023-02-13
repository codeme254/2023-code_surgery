#!/usr/bin/env python3
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        while n >= 1:
            n = n / 2
            if n == 1:
                return True
        return False
    
solution = Solution()
print(solution.isPowerOfTwo(1))
print(solution.isPowerOfTwo(16))
print(solution.isPowerOfTwo(3))
