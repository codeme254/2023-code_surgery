#!/usr/bin/env python3
class Solution:
    def mySqrt(self, x: int) -> int:
        number = x
        if number < 0:
            return None
        if number == 0 or number == 1:
            return number
        x = number
        y = (x + number/x) / 2
        while abs(y-x) > 0.0001:
            x = y
            y = (x + number/x) / 2
        return int(y)