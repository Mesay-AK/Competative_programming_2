# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        r = len(triangle)
        dp = [[0] * (i+1) for i in range(r+1)]

        for i in range(r-1, -1, -1):
            m = len(triangle[i])
            for j in  range(m-1, -1, -1):
 
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]
                


        return dp[0][0]