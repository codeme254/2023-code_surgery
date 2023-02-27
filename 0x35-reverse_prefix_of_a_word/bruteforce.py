#!/usr/bin/env python3
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        pointer = 0
        final_string = ""
        while pointer < len(word):
            if word[pointer] == ch:
                break
            pointer += 1

        if pointer < len(word):
            # means we found the character
            # Do the reverse logic
            forward_pointer = pointer + 1
            while pointer >= 0:
                final_string += word[pointer]
                pointer -= 1
            if forward_pointer < len(word):
                while forward_pointer < len(word):
                    final_string += word[forward_pointer]
                    forward_pointer += 1
                return final_string
            else:
                return final_string
        else:
            return final_string

solution = Solution()
print(solution.reversePrefix("abcdefd", "d"))
print(solution.reversePrefix("xyxzxe", "z"))
print(solution.reversePrefix("abcd", "z"))
print(solution.reversePrefix("", "z"))