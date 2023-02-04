#!/usr/bin/env python3
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        current_running_sum = 0
        i = 0
        for i in range(0, len(nums)):
            current_running_sum += nums[i]
            nums[i] = current_running_sum
        return nums

solution = Solution()
print(solution.runningSum([1, 2, 3, 4]))
print(solution.runningSum([1, 1, 1, 1, 1]))
print(solution.runningSum([3, 1, 2, 10, 1]))
