#!/usr/bin/env python3
class Solution:
    def isomorphic_helper(self, s, t):
        if len(s) != len(t):
            return False
        if len(s) == 0 and len(t) == 0:
            return True
        mapping_lookup = {}
        current_s_index = 0
        current_t_index = 0

        while current_s_index < len(s) and current_t_index < len(t):
            current_s_character = s[current_s_index].lower()
            current_t_character = t[current_t_index].lower()
            # if it is not there in the lookup add it
            if not (current_s_character in mapping_lookup):
                mapping_lookup[current_s_character] = current_t_character
            # otherwise read values and compare
            else:
                if mapping_lookup[current_s_character] != current_t_character:
                    return False
            current_s_index += 1
            current_t_index += 1
        return True

    def isIsomorphic(self, s: str, t: str) -> bool:
        return (self.isomorphic_helper(s, t) and self.isomorphic_helper(t, s))
    
solution = Solution()
print(solution.isIsomorphic("foo", "bar"))
print(solution.isIsomorphic("paper", "title"))
print(solution.isIsomorphic("egg", "add"))
print(solution.isIsomorphic("a", "a"))
print(solution.isIsomorphic("badc", "baba"))