# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        
        result = [0] * (n+1)

        for i in range(n+1):
            count = 0
            k = i

            while i:
                count += (i & 1)
                
                i >>= 1

            result[k] = count

        return result