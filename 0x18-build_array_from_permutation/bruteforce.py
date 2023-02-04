#!/usr/bin/env python3
class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        answer_array = []

        for i in range(0, len(nums)):
            answer_array.append(nums[nums[i]])
        
        return answer_array
    
solution = Solution()
print(solution.buildArray([0,2,1,5,3,4]))