# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = defaultdict(int)

        def dp(left):
            if left == 0:
                return 1

            if left < 0:
                return 0
            if left not in memo:
                for n in nums:
                    memo[left] += dp(left - n)


            return memo[left]

        return dp(target)
                    
