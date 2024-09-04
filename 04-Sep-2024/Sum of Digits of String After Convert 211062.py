# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:

        def convertToNum(word):
            num = ""
            for char in word:
                num+=(str(ord(char)- 96))
            return num

        def transform(number):
            total = 0
            for num in str(number):
                total += int(num)
            return total


        number = convertToNum(s)
        for n in range(k):
            number = transform(number)

        return number
