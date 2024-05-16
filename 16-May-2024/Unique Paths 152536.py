# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        table = [[0] * n for _ in range(m)]

        for r in range(m):
            table[r][n-1] = 1

        for c in range(n):
            table[m-1][c] = 1

        for r in range(m-2, -1, -1):
            for c in range(n-2, -1, -1):
                table[r][c] = table[r+1][c] + table[r][c+1]


        return table[0][0]