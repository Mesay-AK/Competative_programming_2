# Problem: Find-the-prefix-common-array-of-two-arrays - https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen = set()

        result = []
        count = 0
        for i in range(len(A)):
            if A[i] == B[i]:
                count += 1
            if A[i] in seen:
                count += 1
            if B[i] in seen:
                count += 1
            
            result.append(count)
            seen.add(A[i])
            seen.add(B[i])

        return result

