# Problem: Divide intervals into minimum number of groups - https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
    
        start = []
        end = []

        for s, e in intervals:
            start.append(s)
            end.append(e)

        start.sort()
        end.sort()

        groups = 0
        curr = 0
        i, j = 0, 0

        while i < len(intervals) and j < len(intervals):
            if start[i] > end[j]:
                j += 1
                curr -= 1

            else:
                curr += 1
                i += 1
                
            groups = max(groups, curr)

        return groups