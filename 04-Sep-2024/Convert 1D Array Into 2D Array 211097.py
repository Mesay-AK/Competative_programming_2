# Problem: Convert 1D Array Into 2D Array - https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []

        result = []
        i = 0
        j = n

        while j <= len(original):
            # print(result)
            result.append(original[i:j])
            i = j
            j += n

        return result