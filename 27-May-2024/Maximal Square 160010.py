# Problem: Maximal Square - https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        matrix = matrix
        memo = {}
        maxim = 0
        
        def dp(i, j):
            nonlocal maxim 

            if i < 0 or j < 0:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            if matrix[i][j] == '0':
                memo[(i, j)] = 0
                return 0
            
            left = dp(i, j - 1)
            up = dp(i - 1, j)
            diag = dp(i - 1, j - 1)
            
            memo[(i, j)] = min(left, up, diag) + 1
            maxim = max(maxim, memo[(i, j)])

            return memo[(i, j)]
        
        for i in range(m):
            for j in range(n):
                dp(i, j)
        
        return maxim * maxim
