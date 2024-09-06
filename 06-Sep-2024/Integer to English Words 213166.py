# Problem: Integer to English Words - https://leetcode.com/problems/integer-to-english-words/

class Solution:
    def numberToWords(self, num: int) -> str:
        
        if num == 0:
            return 'Zero'

        belowTwenty = [
            '', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 
            'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 
            'Eighteen', 'Nineteen'
        ]
        tens = [
            '', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety'
        ]
        
        thousands = ['', 'Thousand', 'Million', 'Billion']
        
        def helper(num):
            if num == 0:
                return ''
            elif num < 20:
                return belowTwenty[num]
            elif num < 100:
                return tens[num // 10] + ('' if num % 10 == 0 else ' ' + belowTwenty[num % 10])
            elif num < 1000:
                return belowTwenty[num // 100] + ' Hundred' + ('' if num % 100 == 0 else ' ' + helper(num % 100))
            else:
                for i, chunk in enumerate(thousands):
                    if num < 1000 ** (i + 1):
                        return helper(num // 1000 ** i) + ' ' + chunk + ('' if num % 1000 ** i == 0 else ' ' + helper(num % 1000 ** i))
        
        return helper(num).strip()