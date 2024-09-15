# Problem: Ugly Number II - https://leetcode.com/problems/ugly-number-ii/

class Solution(object):
    def nthUglyNumber(self, n):

        uglies = [0] * n
        uglies[0] = 1 

        i2 = i3 = i5 = 0 

        next_of_2 = 2
        next_of_3 = 3
        next_of_5 = 5

        for i in range(1, n):
            next_ugly = min(next_of_2, next_of_3, next_of_5)
            uglies[i] = next_ugly

            if next_ugly == next_of_2:
                i2 += 1
                next_of_2 = uglies[i2] * 2

            if next_ugly == next_of_3:
                i3 += 1
                next_of_3 = uglies[i3] * 3

            if next_ugly == next_of_5:
                i5 += 1
                next_of_5 = uglies[i5] * 5

        return uglies[n - 1]
