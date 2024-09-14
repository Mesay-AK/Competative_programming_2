# Problem: Minimum Time Difference - https://leetcode.com/problems/minimum-time-difference/

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        bucket = [False for _ in range(1440)]
        
        for time in timePoints:
            hour,minute = time.split(":")
            t = int(hour)*60 + int(minute)
            
            if(bucket[t]):
                return 0
            
            bucket[t] = True
            
        prev, curr ,first = -1,-1,-1
        result = float('inf')
        
        for i in range(len(bucket)):
            if(bucket[i]):

                if(first == -1):
                    first = i
                    prev = i
                    continue

                curr = i
                result = min(result,curr-prev)
                prev = curr
                
        result = min(result,first+1440 - prev)
        
        return result
                
        
            