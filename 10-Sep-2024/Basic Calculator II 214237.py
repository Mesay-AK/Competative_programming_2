# Problem: Basic Calculator II - https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def calculate(self, s: str) -> int:
        # if 
        ops = ("+", "-", "*", "/")

        stack = []

        i = 0
        operation = ''
        
        while i < len(s):

            if operation == '*' or operation == '/':
                num = []
                while i < len(s) and  s[i] not in ops:
                    num.append(s[i])
                    i += 1

                current = int(''.join(num))
                if operation == '*':
                    last = stack.pop()
                    stack.append(current * last)
                elif operation == '/':
                    last = stack.pop()
                    stack.append(last // current)
                if i < len(s):
                    operation = s[i]
   
            else:

                if operation:
                    stack.append(operation)
                num = []
                while i < len(s) and s[i] not in ops:
                    num.append(s[i])
                    i += 1

                if i < len(s):
                    operation = s[i]
                stack.append(int(''.join(num)))

   
            i += 1

        num = stack[0]
        i = 1
        while i + 1 < len(stack):

            if stack[i] == "+":
                num += stack[i+1]
            elif stack[i] == "-":
                num -= stack[i + 1]
            i += 2
        return num


