#!/usr/bin/env python3
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            if target > nums[middle]:
                left = middle + 1
            else:
                right = middle - 1
        
        return left