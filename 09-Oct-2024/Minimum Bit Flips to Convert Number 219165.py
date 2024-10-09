# Problem: Minimum Bit Flips to Convert Number - https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:

        flips = 0
        common = start ^ goal
        while common:
            if common & 1:
                flips += 1
            common >>= 1

        return flips