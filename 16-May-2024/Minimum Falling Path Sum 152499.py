# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix)

        table = [[0] * n for _ in range(n)]

        for c in range(n):
            table[n-1][c] = matrix[n-1][c]

        def valid(r, c):
            return 0 <= r < n and  0 <= c < n

        for r in range(n-2, -1, -1):
            for c in range(n):
                
                x, y, z  = float('inf'), float('inf'), float('inf')
                if valid(r+1, c-1):
                    x = table[r+1][c-1]
                if valid(r+1, c):
                    y = table[r+1][c]
                if valid(r+1, c+1):
                    z = table[r+1][c+1]
               
                table[r][c] = min(x, y, z) + matrix[r][c] 

      
        return min(table[0])
