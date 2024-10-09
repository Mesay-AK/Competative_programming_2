# Problem: Minimum Add To Make Parentheses Valid - https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        stack = []
        for char in s:
            if not stack:
                stack.append(char)
            elif stack[-1] == '(' and char == ')':
                stack.pop()
            else:
                stack.append(char)

        return len(stack)






































        # tovalid = 0
        # stack = []
        # for i in s:
        #     if i == '(':
        #         stack.append(i)

        #     elif stack and stack[-1] == '(':
        #         stack.pop()
                
        #     else:
        #         tovalid += 1

        # return tovalid + len(stack)


            