# Problem: Minimum Score Triangulation of Polygon - https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:


        n = len(values)
        dp = [[0] * n for _ in range(n)]

        for length in range(2, n):
            for i in range(n - length):
                
                j = i + length
                dp[i][j] = float('inf')

                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], values[i] * values[j] * values[k] + dp[i][k] + dp[k][j])

        return dp[0][n - 1]
