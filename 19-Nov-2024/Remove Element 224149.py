# Problem: Remove Element - https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:


        left, right = 0, len(nums) - 1
        count =  nums.count(val)
        if count == len(nums):
            return 0

        while left < right:
            if nums[left] == val and nums[right] != val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
                left += 1
    
            elif nums[right] == val:
                right -= 1

            else:
                left += 1


        return len(nums) - count