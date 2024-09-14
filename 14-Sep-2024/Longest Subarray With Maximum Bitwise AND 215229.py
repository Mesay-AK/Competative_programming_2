# Problem: Longest Subarray With Maximum Bitwise AND - https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        answer: int = 1 
        left: int = 0
        target: int = max(nums)

        for right in range(len(nums)):

            while left <= right and nums[right] != target:
                answer = max(answer, right - left)
                left += 1
            answer = max(answer, right - left + 1)
            
        return answer