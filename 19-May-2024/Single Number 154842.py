# Problem: Single Number - https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        n = 0
        for i in range(len(nums)):
            n ^= nums[i]

        return n