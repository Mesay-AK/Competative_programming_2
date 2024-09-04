# Problem: Maximum Distance in Arrays - https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:

        minim = arrays[0][0]
        maxim = arrays[0][-1]
        max_distance = 0

        for i in range(1, len(arrays)):
            cur_min = arrays[i][0]
            cur_max = arrays[i][-1]

            max_distance = max(max_distance, abs(cur_max - minim))

            max_distance = max(max_distance, abs(maxim - cur_min))
            
            minim = min(minim, cur_min)
            maxim = max(maxim, cur_max)
        
        return max_distance
