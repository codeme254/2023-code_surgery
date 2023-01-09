#!/usr/bin/env python3
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                summation = nums[i] + nums[j]
                if summation == target:
                    return [i, j]

solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))
