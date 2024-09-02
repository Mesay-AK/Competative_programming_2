# Problem: Find the Student that Will Replace the Chalk - https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/description/

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:

        total = sum(chalk)
        k = k% total

        i = 0
        while chalk[i] <= k:
            k -= chalk[i]
            i += 1

        return i
        