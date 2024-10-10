# Problem: Minimum Deletions to Make String Balanced - https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/


class Solution:
    def minimumDeletions(self, s: str) -> int:
        count = 0
        minim = 0
        
        for char in s:
            if char == 'b':
                count += 1
            else:
                minim = min(minim + 1, count)
                
        return minim