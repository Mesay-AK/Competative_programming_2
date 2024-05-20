# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        carry = 0
        mask = 0xffffffff
        while b&mask != 0:

            carry = a & b
            a = a ^ b
            b = carry << 1
        return a & mask if b > mask else a

