# Problem: Find-the-prefix-common-array-of-two-arrays - https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        bitmaskA = 0
        bitmaskB = 0

        result = []

        for i in range(len(A)):
            bitmaskA |= (1 << A[i])
            bitmaskB |= (1 << B[i])

            common = bitmaskA & bitmaskB

            result.append(bin(common).count("1"))


        return result

