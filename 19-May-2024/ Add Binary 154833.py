# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        carry = 0
        n = max(len(a), len(b))
        aa = '0'* (n-len(a)) + a
        bb = '0'* (n - len(b)) + b
        result = []

        for i in range(n-1, -1, -1):
            a = 1 if aa[i] == '1' else 0
            b = 1 if bb[i] == '1' else 0

            result.append(str(a^b^carry))
            if a+b+carry > 1:
                carry = 1

            else:
                carry = 0

        if carry:
            result.append('1')

        result = result[::-1]
        
        return ''.join(result)