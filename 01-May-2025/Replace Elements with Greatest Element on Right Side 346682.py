# Problem: Replace Elements with Greatest Element on Right Side - https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largest = arr[-1]
        arr[-1] = -1

        for i in range(len(arr)-2, -1, -1):

            large = arr[i] if largest < arr[i] else largest
            arr[i] = largest
            largest = large

            
                

        return arr