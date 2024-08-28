# Problem: String Without AAA or BBB - https://leetcode.com/problems/string-without-aaa-or-bbb

class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        string = []
        
        while a > 0 or b > 0:
            if len(string) >= 2 and string[-1] == string[-2]:
                if string[-1] == 'a':
                    string.append('b')
                    b -= 1
                else:
                    string.append('a')
                    a -= 1
            else:
                if a > b:
                    string.append('a')
                    a -= 1
                else:
                    string.append('b')
                    b -= 1
        
        return ''.join(string)
