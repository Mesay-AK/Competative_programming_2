# Problem: Baseball Game
 (Easy) - https://leetcode.com/problems/baseball-game/

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for char in operations:
            if char !=  "+" and char != "D" and char != "C":
                stack.append(int(char))

            elif char == "+":
                stack.append(stack[-1] + stack[-2])

            elif char == "D":
                stack.append(stack[-1] * 2)

            elif char == "C":
                stack.pop()

        return sum(stack)

        