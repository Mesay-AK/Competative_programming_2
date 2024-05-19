# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        result = []

        while num:
            if num & 1:
                result.append('0')
            else:
                result.append('1')

            num >>= 1

        n = len(result)
        i = 0
        answer = 0
        while i < n:
            answer += ((int(result[i]))*2**i)

            i += 1
        return answer