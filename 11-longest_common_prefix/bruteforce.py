#!/usr/bin/env python3
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        current_prefix = ""
        string_character_index = 0
        current_character = strs[0][string_character_index]
        
        while string_character_index <= len(strs[0]) - 1:
            current_character = strs[0][string_character_index]
            for i in range(0, len(strs)):
                if string_character_index > len(strs[i]) - 1:
                    return current_prefix
                if current_character != strs[i][string_character_index]:
                    return current_prefix
            current_prefix += current_character
            string_character_index += 1
        return current_prefix

solution = Solution()

print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
print(solution.longestCommonPrefix(["flower", "flow"]))
print(solution.longestCommonPrefix(["fly", "kite", "flow"]))
