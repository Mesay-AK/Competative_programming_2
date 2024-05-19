# Problem: Minimum Number of Operations to Make Array XOR Equal to K - https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        final_xor = 0
        for n in nums:
            final_xor = final_xor ^ n

        count = 0
        while k:

            if (k&1) != (final_xor &1):
                count += 1
            k >>= 1
            final_xor >>= 1

        count += bin(final_xor).count('1') 
        return count