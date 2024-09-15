# Problem: Find the Longest Substring Containing Vowels in Even Counts - https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

class Solution(object):
    def findTheLongestSubstring(self, s):
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16,}

        lastSeenIndex = { 0: -1,}
        
        n = len(s)
        maxLen,  curr = 0, 0
        for i in range(n):
            if s[i] in "aeiou":
                 curr ^= vowels[s[i]]
            if  curr in lastSeenIndex:
                maxLen = max(maxLen, i - lastSeenIndex[ curr])
            else:
                lastSeenIndex[ curr] = i
        return maxLen