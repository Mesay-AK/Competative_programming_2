# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if len(nums) == 0:
            return -1, -1

        first = -1
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                first = mid
                r = mid - 1

            elif nums[mid] > target:
                r = mid - 1

            else:
                l = mid + 1

        first = l if nums[l] == target else first

        last = -1
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid ]== target:
                last = mid
                l = mid + 1

            elif nums[mid] > target:
                r = mid - 1

            else:
                l = mid + 1

        last = r if nums[r] == target else last

        return first, last