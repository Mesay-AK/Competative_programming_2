# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution(object):
    def maxArea(self, height):
    
        left = 0
        right = len(height)-1
        maxim = 0

        while left < right:
            
            length = right - left
            width = min(height[left], height[right])
            maxim = max(length * width, maxim)

            if height[left] <= height[right]:
                left+=1

            else:
                right-=1

        return maxim


























        # length=len(height)
        # i=0
        # j=length-1
        # maximum=0
        # while i<length:
        #     while i<j:
        #         area= (j-i)* min(height[i],height[j])
        #         print(area)
        #         if area>maximum:
        #             maximum=area
        #             print(area)
        #         j-=1
        #     i+=1
        #     j=length-1
        # return maximum
        # maximum=0
        # i, j = 0, len(height)-1
        # while i<j:
        #     area=(j-i)* min(height[i],height[j])
        #     maximum=max(maximum,area)
        #     if height[i] < height[j]:
        #         i+=1
        #     else:
        #         j-=1
        # return maximum



