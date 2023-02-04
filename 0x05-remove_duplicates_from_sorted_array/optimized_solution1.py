#!/usr/bin/env python3
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 1

        fast_pointer = 1
        slow_pointer = 1

        while fast_pointer < len(nums):
            if nums[fast_pointer] == nums[fast_pointer - 1]:
                fast_pointer += 1
            else:
                nums[slow_pointer] = nums[fast_pointer]
                slow_pointer += 1
                fast_pointer += 1
        print(nums)
        return slow_pointer
solution = Solution()
print(solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
