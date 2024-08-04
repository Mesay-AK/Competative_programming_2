# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row = 1
        first_col = 1
        for r in range(len(matrix)):
            if matrix[r][0] == 0:
                first_col = 0

        for c in range(len(matrix[0])):
            if matrix[0][c] == 0:
                first_row = 0   

        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if not first_row:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0

        if not first_col:          
            for r in range(len(matrix)):
                matrix[r][0] = 0 

        return matrix

