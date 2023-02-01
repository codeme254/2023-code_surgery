#!/usr/bin/env python3
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if len(digits) == 0:
            return digits;
        if len(digits) == 1 and digits[0] < 9:
            digits[0] += 1
            return digits;
        
        # prefix a zero at the start of the array
        # just in case the current first element is 9
        digits.insert(0, 0)
        
        current_index = len(digits) - 1
        carry_value = 1

        while current_index >= 0:
            summation = digits[current_index] + carry_value
            if summation == 10:
                digits[current_index] = 0
                carry_value = 1
            else:
                digits[current_index] = summation
                carry_value = 0
            current_index -= 1
        
        # remove any leading zero in case it did not get replaced with a 1
        if digits[0] == 0:
            digits.remove(0)
        return digits

solution = Solution()
print(solution.plusOne([]))
print(solution.plusOne([8]))
print(solution.plusOne([9]))
print(solution.plusOne([1, 2, 3, 4]))
print(solution.plusOne([9, 9, 9, 9]))
