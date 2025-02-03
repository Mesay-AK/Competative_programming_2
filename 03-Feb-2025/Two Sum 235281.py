# Problem: Two Sum - https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        difference = {}
        for i in range(len(nums)):
            difference[target - nums[i]] = i

        for i in range(len(nums)):
            if nums[i] in difference and i != difference[nums[i]]:
                return [difference[nums[i]], i]

        