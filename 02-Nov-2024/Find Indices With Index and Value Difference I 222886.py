# Problem: Find Indices With Index and Value Difference I - https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/description/

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:

        for left in range(len(nums)):
            right = left + indexDifference

            while right < len(nums):
                if abs(nums[right] - nums[left]) >= valueDifference:
                    return left, right

                right += 1

        return -1, -1