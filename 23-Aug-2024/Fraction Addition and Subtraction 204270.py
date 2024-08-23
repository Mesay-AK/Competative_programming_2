# Problem: Fraction Addition and Subtraction - https://leetcode.com/problems/fraction-addition-and-subtraction/

class Solution:
    def fractionAddition(self, expression: str) -> str:

        if expression[0] != '-':
            expression = "+" + expression
        

        def add(frac1, frac2):
            num1, den1 = frac1
            num2, den2 = frac2
            common_denominator = den1 * den2
            numerator_sum = num1 * den2 + num2 * den1
            common_divisor = gcd(abs(numerator_sum), common_denominator)
            return (numerator_sum // common_divisor, common_denominator // common_divisor)

        fractions = []
        i = 0
        while i < len(expression):

            sign = 1 if expression[i] == '+' else -1
            i += 1
            j = i

            while expression[j] != '/':
                j += 1
            numerator = int(expression[i:j]) * sign
            i = j + 1
            j = i
            while j < len(expression) and expression[j].isdigit():
                j += 1
            denominator = int(expression[i:j])
            fractions.append((numerator, denominator))
            i = j

        result_fraction = reduce(add, fractions)

        numerator, denominator = result_fraction
        if denominator == 1:
            return f"{numerator}/1"
        else:
            return f"{numerator}/{denominator}"

