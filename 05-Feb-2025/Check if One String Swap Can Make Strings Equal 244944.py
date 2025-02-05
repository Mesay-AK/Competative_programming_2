# Problem: Check if One String Swap Can Make Strings Equal - https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        to_be_swapped = []

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                to_be_swapped.append(i)


        if len(to_be_swapped) > 2:
            return False
        elif len(to_be_swapped) == 0:
            return True

        if s1[to_be_swapped[0]] != s2[to_be_swapped[-1]] or s1[to_be_swapped[-1]] != s2[to_be_swapped[0]]:
            return False

        return True