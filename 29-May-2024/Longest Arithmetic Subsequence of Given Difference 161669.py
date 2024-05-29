# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        memo = {}
        maxim = 0
        
        for num in arr:
            if num - difference in memo:
                memo[num] = memo[num - difference] + 1

            else:
                memo[num] = 1

            maxim = max(maxim, memo[num])

        return maxim
