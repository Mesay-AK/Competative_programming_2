# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        number = ''
        for char in s:
            number+=(str(ord(char)- 96))
        i = 0
        while i <= k - 1:
            summ = 0
            for j in number:
                summ += int(j)

            number = str(summ)
            i += 1

        return int(number)
