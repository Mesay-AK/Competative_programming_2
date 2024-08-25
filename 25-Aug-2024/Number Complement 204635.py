# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        complements = []

        while num:
            if num & 1:
                complements.append('0')
            else:
                complements.append('1')

            num >>= 1


        complements= ''.join(complements[::-1])

        return int(complements, 2)
