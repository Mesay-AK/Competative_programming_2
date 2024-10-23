# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if not nums:
            return -1, -1

        left = bisect_left(nums, target)
        right = bisect.bisect(nums, target) - 1

       
        left = -1 if left >= len(nums)  or nums[left] != target else left
        right = -1 if right >= len(nums) or nums[right] != target  else right

        return (left, right)
