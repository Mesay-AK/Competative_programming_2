# Problem: Vowel of All Substring - https://leetcode.com/problems/vowels-of-all-substrings/

class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)

        vowels = "aeiou"
        count = 0
        for i, char in enumerate(word):
            if char in vowels:
                count += ((i + 1) * (n - i))

        return count