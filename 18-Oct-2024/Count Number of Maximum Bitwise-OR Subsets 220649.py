# Problem: Count Number of Maximum Bitwise-OR Subsets - https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/description/

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxim = 0

        for i in nums:
            maxim |= i
        
        def dfs(i, curr):
            nonlocal maxim

            if i == len(nums):
                return 1 if curr == maxim else 0
                 
            return dfs(i + 1, curr) +  dfs(i + 1, curr | nums[i])

        return dfs(0, 0)

        