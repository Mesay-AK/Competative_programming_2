# Problem: Height Checker
(Easy) - https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = [0]*101
        for height in heights:
            count[height] += 1
        expected = []

        for i in range(len(count)):
            expected.append([i]*count[i])

        e = []
        for char in expected:
            if char != []:
                e += char

        ans = 0
        for i in range(len(e)):
            if e[i] != heights[i]:
                ans += 1
        return ans        

