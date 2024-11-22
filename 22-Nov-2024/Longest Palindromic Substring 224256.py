# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:

        longest = ''
        maxim = 0

        for i in range(len(s)):
            # For odd palindrome
            left, right = i, i

            while (-1 < left and right < len(s)) and (s[left] == s[right]):
                if maxim < right - left + 1:
                    longest = s[left:right + 1]
                    maxim = right - left + 1

                left -= 1
                right += 1
            
            left, right = i, i + 1
            while left > -1 and right < len(s) and s[left] == s[right]:
                if maxim < right - left + 1:
                    longest = s[left:right + 1]
                    maxim = right - left + 1

                left -= 1
                right += 1

        return longest

        



