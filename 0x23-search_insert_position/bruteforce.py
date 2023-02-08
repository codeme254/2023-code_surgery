#!/usr/bin/env python3
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in range(0, len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return i
        return len(nums)
    
solution  = Solution()
print(solution.searchInsert([1,3,5,6], 5))
print(solution.searchInsert([1,3,5,6], 2))
print(solution.searchInsert([1,3,5,6], 7))
print(solution.searchInsert([1], 1))
print(solution.searchInsert([1], 5))
