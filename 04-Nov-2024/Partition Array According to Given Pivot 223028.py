# Problem: Partition Array According to Given Pivot - https://leetcode.com/problems/partition-array-according-to-given-pivot/description/

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller = []
        equal = []
        greater = []

        for n in nums:
            if n < pivot:
                smaller.append(n)
            elif n > pivot:
                greater.append(n)

            else:
                equal.append(n)

        return smaller + equal + greater

