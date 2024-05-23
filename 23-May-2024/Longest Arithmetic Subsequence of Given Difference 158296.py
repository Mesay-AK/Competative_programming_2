# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        N = len(arr)
        longest = defaultdict(lambda : 1)
        track = defaultdict(int)

        for i in range(N-1 ,-1 , -1):
            val = arr[i] + difference

            if val not in track:
                longest[i] = 1

            else:
                longest[i]+= longest[track[val]]
                
            track[arr[i]] = i
        
        return max(longest.values())

            
            
        