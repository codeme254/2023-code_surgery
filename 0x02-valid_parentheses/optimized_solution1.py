#!/usr/bin/env python3
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        opening_braces_look_up = {
                "{": 1,
                "(": 1,
                "[": 1
                }
        braces_look_up = {
                "}": "{",
                ")": "(",
                "]": "["
                }
        stack = []
        for i in range(0, len(s)):
            # [) {} ()
            # stack: [ '[']
            if s[i] in opening_braces_look_up:
                stack.append(s[i])
            else:
                if len(stack) > 0:
                    current_opening_brace = stack.pop()
                    if braces_look_up[s[i]] == current_opening_brace:
                        continue
                    else:
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

solution = Solution()
print(solution.isValid("()[]{}"))
print(solution.isValid("[){}()"))
