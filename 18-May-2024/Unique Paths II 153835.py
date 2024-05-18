# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        n, m = len(obstacleGrid), len(obstacleGrid[0])
        memo = {}

        def dp(r, c):

            if r == n or m == c or obstacleGrid[r][c] == 1:
                return 0

            if r == n-1 and c == m-1:
                return 1

            state = (r, c)

            if state not in memo:
                right = dp(r, c + 1)
                down = dp(r + 1, c)

                memo[state] = right + down

            return memo[state]

        return dp(0, 0)

            
            