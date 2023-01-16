#!/usr/bin/env python3
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        divider = 1
        while x >= 10 * divider:
            divider *= 10


        while x:
            right_most = x % 10
            left_most = x // divider

            if right_most != left_most:
                return False
            # chopping the left and the right digits
            x = (x %= divider) // 10
            divider = divider / 100

        return True
