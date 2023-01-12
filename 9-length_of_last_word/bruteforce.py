#!/usr/bin/env python3
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        s_arr = s.split()
        return len(s_arr[len(s_arr) - 1])

solution = Solution()
print(solution.lengthOfLastWord("  Fly Me to the Moon    "))
