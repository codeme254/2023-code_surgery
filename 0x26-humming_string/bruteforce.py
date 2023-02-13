#!/usr/bin/env python3

# The answer is correct but it behaves weirdly when running locally
class Solution:
    def hammingWeight(self, n: int) -> int:
        number_of_one_bits = 0

        while n:
            right_most_bit = n % 2
            if right_most_bit == 1:
                number_of_one_bits += 1
            n = n >> 1
        return number_of_one_bits

solution = Solution()
# print(solution.hammingWeight(00000000000000000000000000001011))
# print(solution.hammingWeight(00000000000000000000000010000000))
print(solution.hammingWeight(11111111111111111111111111111101))
