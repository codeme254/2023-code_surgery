#!/usr/bin/env python3
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        current_string_a_index = len(a) - 1
        current_string_b_index = len(b) - 1
        carry = 0
        final_string = ""

        while current_string_a_index >= 0 or current_string_b_index >= 0:
            if current_string_a_index >= 0:
                current_a_value = int(a[current_string_a_index])
            else:
                current_a_value = 0
            if current_string_b_index >= 0:
                current_b_value = int(b[current_string_b_index])
            else:
                current_b_value = 0

            """
            Possible combinations
            a b carry
            1 1  1
            1 1  0
            0 0  1
            0 0  0
            either a or b is 1 and carry is 0
            either a or b is 1 and carry is 1
            """

            if (current_a_value == 1 and current_b_value == 1) and carry == 1:
                # Means sum is 11, so we append 1 and carry 1
                final_string += "1"
                carry = 1
            elif (current_a_value == 1 and current_b_value == 1) and carry == 0:
                # Means sum is 10, so we append 0 and carry 1
                final_string += "0"
                carry = 1
            elif (current_a_value == 0 and current_b_value == 0) and carry == 1:
                # Means that summation is 1, so we append 1 and carry 0
                final_string += "1"
                carry = 0
            elif (current_a_value == 0 and current_b_value == 0) and carry == 0:
                # Means that the summation is so, so we append 0 and carry 0
                final_string += "0"
                carry = 0
            elif (current_a_value == 1 or current_b_value == 1) and carry == 0:
                # Means that the summation is 1, so we append 1 and carry 0
                final_string += "1"
                carry = 0
            elif (current_a_value == 1 or current_b_value == 1) and carry == 1:
                # Means that summation is 10, so we append 0 and carry 1
                final_string += "0"
                carry = 1
            current_string_a_index -= 1
            current_string_b_index -= 1

        if carry == 1:
            final_string += "1"
        return final_string[::-1]

solution = Solution()
print(solution.addBinary("1010", "1011"))