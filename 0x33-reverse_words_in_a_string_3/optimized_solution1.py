#!/usr/bin/env python3
class Solution:
    def reverse_string(self, string:str) -> str:
        """
        Reverses a single string and returns the reversed string
        """
        if len(string) <= 1:
            return string
        string = list(string)
        left_pointer = 0
        right_pointer = len(string) - 1
        while left_pointer < right_pointer:
            temp = string[left_pointer]
            string[left_pointer] = string[right_pointer]
            string[right_pointer] = temp
            right_pointer -= 1
            left_pointer += 1
        return "".join(string)

    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        for i in range(0, len(s)):
            s[i] = self.reverse_string(s[i])
        return " ".join(s)

solution = Solution()
# print(solution.reverse_string("Code"))
# print(solution.reverse_string("praise"))
print(solution.reverseWords("Let's take LeetCode contest"))
print(solution.reverseWords("God Ding"))