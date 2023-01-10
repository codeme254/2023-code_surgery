#!/usr/bin/env python3
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        replace_pointer = (m + n) - 1
        nums_one_pointer = m - 1
        nums_two_pointer = n - 1

        while nums_two_pointer >= 0 and nums_one_pointer >=0:
            if nums2[nums_two_pointer] > nums1[nums_one_pointer]:
                nums1[replace_pointer] = nums2[nums_two_pointer]
                nums_two_pointer -= 1
            else:
                tmp = nums1[nums_one_pointer]
                nums1[nums_one_pointer] = nums1[replace_pointer]
                nums1[replace_pointer] = tmp
                nums_one_pointer -= 1
            replace_pointer -= 1

        while nums_two_pointer >= 0:
            nums1[replace_pointer] = nums2[nums_two_pointer]
            nums_two_pointer -= 1
            replace_pointer -= 1
solution = Solution()
solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
