# Problem: Palindrome Partitioning II - https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:
        memo = {}
        
        def is_palindrome(subs):
            return subs == subs[::-1]
        
        def dp(i):
            if i == len(s):
                return -1 
            
            if i in memo:
                return memo[i]

            curr = float('inf')
            for j in range(i + 1, len(s) + 1):
                if is_palindrome(s[i:j]):
                    
                    curr = min(curr, 1 + dp(j))

            memo[i] = curr
            return curr

        return dp(0)
