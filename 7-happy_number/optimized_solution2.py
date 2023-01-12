#!/usr/bin/env python3
class Solution:
    def isHappy(self, n: int) -> bool:
        visited_digits = set()

        while n not in visited_digits:
            visited_digits.add(n)
            n = self.sumOfSquares(n)

            if n == 1:
                return True
        return False

    def sumOfSquares(self, n: int) -> int:
        summation = 0
        while n:
            ones_digit = n%10
            ones_digit = ones_digit ** 2
            summation += ones_digit
            n = n // 10
        return summation

solution = Solution()
print(solution.isHappy(19))
