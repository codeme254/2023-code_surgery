#!/usr/bin/env python3
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        seen_numbers = {}

        for i in range(0, len(nums)):
            if nums[i] in seen_numbers.keys():
                seen_numbers[nums[i]] += 1
            else:
                seen_numbers[nums[i]] = 1
        
        for key, value in seen_numbers.items():
            if value == 1:
                return key

solution = Solution()
print(solution.singleNumber([4, 1, 2, 1, 2]))