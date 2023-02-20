#!/usr/bin/env python3
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
         ## A = 65 a = 97
        # Z = 90 z = 122
        left_pointer = 0
        right_pointer = len(s) - 1
        s = list(s)

        while left_pointer < right_pointer:
            left_character = s[left_pointer]
            right_character = s[right_pointer]
            while ord(left_character) not in range(65, 91) and ord(left_character) not in range(97, 123):
                left_pointer += 1
                if left_pointer < len(s):
                    left_character = s[left_pointer]
                else:
                    break
            while ord(right_character) not in range(65, 91) and ord(right_character) not in range(97, 123):
                right_pointer -= 1
                if right_pointer >= 0:
                    right_character = s[right_pointer]
                else:
                    break
            if left_pointer < right_pointer and left_pointer < len(s) and right_pointer > 0:
                tmp = s [left_pointer]
                s[left_pointer] = s[right_pointer]
                s[right_pointer] = tmp
                right_pointer -= 1
                left_pointer += 1
            else:
                break
        return "".join(s)

solution = Solution()
print(solution.reverseOnlyLetters("a-bC-dEf-ghIj"))