#!/usr/bin/env python3

class Solution:
    def convertToBinaryAndCountOneBits(self, number:int) -> int:
        if number == 0:
            return 0
        binary_string = '';
        while number > 0:
            remainder = number % 2
            if remainder == 1:
                binary_string += '1'
            number = number // 2
        return len(binary_string)
    def countBits(self, n: int) -> list[int]:
        result_array = []
        for i in range(0, n+1):
            number_of_one_bits = self.convertToBinaryAndCountOneBits(i)
            result_array.append(number_of_one_bits)
        return result_array;

solution = Solution()
print(solution.convertToBinaryAndCountOneBits(15))
print(solution.countBits(2))
print(solution.countBits(5))
