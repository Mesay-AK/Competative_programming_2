# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
                
        intervals.sort()
        result = [intervals[0]]
        
        for start, end in intervals[1:]:
            lastEnd = result[-1][-1]

            if start <= lastEnd:
                result[-1][-1] =max(lastEnd, end)

            else:
                result.append([start, end])



        return result


        #  [1, 2, 8, 15]
        #  [3, 6, 10, 18]