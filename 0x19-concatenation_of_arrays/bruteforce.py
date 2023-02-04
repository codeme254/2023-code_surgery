#!/usr/bin/env python3
class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:

        final_array = []
        final_array_length = len(nums) * 2
        """
        Create a new array of twice the length of original array
        Then fill it with dummy values
        """
        final_array.extend([None] * final_array_length)

        for i in range(0, len(nums)):
            final_array[i] = nums[i]
            final_array[i + len(nums)] = nums[i]

        return final_array

solution = Solution()
print(solution.getConcatenation([1, 2, 3]))