# Problem: Dungeon Game - https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        memo = {}
        m, n = len(dungeon), len(dungeon[0])

        def dp(i, j):
            if i == m or j == n:
                return float('inf')

            if i == m - 1 and j == n - 1:
                return max(1 - dungeon[i][j], 1)

            if (i, j) not in memo:

                total = min(dp(i+1, j), dp(i, j+1))

                memo[(i, j)] = max(total - dungeon[i][j], 1)

            return memo[(i, j)]

        return dp(0, 0)