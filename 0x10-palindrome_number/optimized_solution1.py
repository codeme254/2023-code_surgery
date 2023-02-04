#!/usr/bin/env python3
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        dummy_number = 0
        real_number = x

        while x > 0:
            dummy_number = (dummy_number * 10) + (x % 10)
            x = x // 10

        return dummy_number == real_number

solution = Solution()
print(solution.isPalindrome(121))
print(solution.isPalindrome(1221))
print(solution.isPalindrome(7))
print(solution.isPalindrome(35))
