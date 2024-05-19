# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = [0] * 32
        
        for n in nums:
            for i in range(32):
                if n & (1 << i):
                    
                    result[i] += 1

        unique = 0
        for i in range(32):
            if result[i] % 3:
                if i == 31: 
                    unique -= (1 << i)
                else:
                    unique |= (1 << i)
        
        return unique
