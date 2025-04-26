# Problem: Clear Digits - https://leetcode.com/problems/clear-digits/description/

class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for i in s:
            if i.isdigit():
                if stack:
                    stack.pop()
            else:
                stack.append(i)

        return "".join(stack)