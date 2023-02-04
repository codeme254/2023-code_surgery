#!/usr/bin/env python3
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        elements_frequencies = {}
        array_length = len(nums)

        for i in range(0, len(nums)):
            if nums[i] in elements_frequencies.keys():
                elements_frequencies[nums[i]] += 1
            else:
                elements_frequencies[nums[i]] = 1

        for key, value in elements_frequencies.items():
            if value > array_length / 2:
                return key

solution = Solution()
print(solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))