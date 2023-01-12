#!/usr/bin/env python3
class Solution:
    def isHappy(self, n: int) -> bool:
        numbers_already_seen = {}
        while n not in numbers_already_seen:
            numbers_already_seen[n] = True
            n = self.add_and_square_digits_in_number(n)
            if n == 1:
                return True
        return False

    def add_and_square_digits_in_number(self, number):
        summation = 0

        while number >= 10:
            summation += (number%10)**2
            number = number//10
        summation += number**2
        return summation
solution = Solution()
print(solution.isHappy(19))
