# Problem: Minimum Operations to Reduce X to Zero - https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/

class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        target=sum(nums)-x
        left=0
        maxl=-1
        curr=0
        for right in range(len(nums)):
            curr+=nums[right]
            while left<=right and target<curr:
                curr-=nums[left]
                left+=1
            if curr==target:
                maxl=max(maxl,right-left+1)
        return maxl if maxl==-1 else len(nums)-maxl