#!/usr/bin/env python3
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        if len(nums) == 0:
            return (0)

        if len(nums) == 1 and nums[0] == val:
            return (0)

        if len(nums) == 1 and nums[0] != val:
            return (1)

        begin_pointer = 0
        end_pointer = len(nums) - 1

        while begin_pointer < end_pointer:
            if nums[begin_pointer] == val:
                while nums[end_pointer] == val and end_pointer >= begin_pointer:
                    end_pointer -= 1
                self.swap_elements_in_list(begin_pointer, end_pointer, nums)
            else:
                begin_pointer += 1
        print(nums)
        return end_pointer + 1

    def swap_elements_in_list(self, first_index, second_index, nums_list):
        tmp = nums_list[first_index]
        nums_list[first_index] = nums_list[second_index]
        nums_list[second_index] = tmp

solution = Solution()
solution.swap_elements_in_list(1, 3, [1, 2, 3, 4, 5, 6])
print(solution.removeElement([3, 2, 2, 3], 3))
print(solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
print(solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 9))
print(solution.removeElement([3], 2))
print(solution.removeElement([3], 3))
