# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:

        result = []
        
        def backtracking(i, palindromes):
            if i >= len(s):
                result.append(palindromes[:])
                return 

            for j in range(i, len(s)):
                check = s[i:j + 1]
                
                if check == check[::-1]:
                    palindromes.append(check)
                    backtracking(j+1, palindromes)
                    palindromes.pop()

        backtracking(0, [])

        return result

                
