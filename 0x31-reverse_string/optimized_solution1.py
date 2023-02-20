#!/usr/bin/env python3
class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) <= 1:
            return s
        
        left_pointer = 0
        right_pointer = len(s) - 1

        while left_pointer < right_pointer:
            temp = s[left_pointer]
            s[left_pointer] = s[right_pointer]
            s[right_pointer] = temp
            left_pointer += 1
            right_pointer -= 1
        return s
    
solution = Solution()
print(solution.reverseString(["h","e","l","l","o"]))
print(solution.reverseString(["H","a","n","k","a","h"]))