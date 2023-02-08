#!/usr/bin/env python3
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen_numbers = {}

        for i in range(0, len(nums)):
            if nums[i] in seen_numbers:
                return True
            else:
                seen_numbers[nums[i]] = 1
        return False

solution = Solution()
print(solution.containsDuplicate([1,2,3,1]))
print(solution.containsDuplicate([1,2,3,4]))
print(solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
print(solution.containsDuplicate([1]))
print(solution.containsDuplicate([]))