#!/usr/bin/env python3
class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        if len(nums) < 3:
            return 0
        number_of_triplets = 0
        starting_index = 2
        found_right = False
        found_left = False

        while starting_index < len(nums):
            left_pointer = 0
            right_pointer = starting_index - 1
            while right_pointer > left_pointer:
                if nums[starting_index]- nums[right_pointer] == diff:
                    found_right = True
                    while left_pointer < right_pointer:
                        if nums[right_pointer]- nums[left_pointer] == diff:
                            found_left = True
                            if found_left and found_right:
                                # print(left_pointer, right_pointer, starting_index)
                                number_of_triplets += 1
                        left_pointer += 1
                right_pointer -= 1
                found_right = False
                found_left = False
            starting_index += 1
        return number_of_triplets

solution = Solution()
print(solution.arithmeticTriplets([0,1,4,6,7,10], 3))
print(solution.arithmeticTriplets([0,1,2,3,4,5,6], 1))