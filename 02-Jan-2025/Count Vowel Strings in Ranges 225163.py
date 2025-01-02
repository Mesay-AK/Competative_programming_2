# Problem: Count Vowel Strings in Ranges - https://leetcode.com/problems/count-vowel-strings-in-ranges/

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        voweled = [0] * (len(words) + 1 )
        vowels = {"a", "e", "i", "o", "u"}

        for i in range(len(words)):
            voweled[i + 1] = voweled[i] + (1 if words[i][0] in vowels and words[i][-1] in vowels else 0)

        result = []

        for l, r in queries:
            result.append(voweled[r + 1] - voweled[l])


        return result