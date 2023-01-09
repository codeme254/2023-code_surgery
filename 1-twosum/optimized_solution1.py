#!/usr/bin/env python3
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        look_up = {}
        for i in range(0, len(nums)):
            remainder_to_make_target = target - nums[i]
            if remainder_to_make_target in look_up:
                return [look_up[remainder_to_make_target], i]
            else:
                look_up[nums[i]] = i

solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))
