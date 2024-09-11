# Problem: Find and Replace Pattern - https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        result = []

        for word in words:
            track1 = {}
            track2 = {}
            found = True
            for i in range(len(word)):
                if word[i] not in track1 and pattern[i] not in track2:
                    track1[word[i]] = pattern[i]
                    track2[pattern[i]] = word[i]
                elif word[i] in track1 and track1[word[i]] != pattern[i]:
                    found = False
                    break
                elif pattern[i] in track2  and track2[pattern[i]] != word[i]:
                    found = False
                    break
                    
            if found:
                result.append(word)

        return result
