# Problem: Super Pow - https://leetcode.com/problems/super-pow/description/

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337

        def mod_pow(x, n):
            result = 1
            x %= MOD
            while n:
                if n % 2:
                    result = (result * x) % MOD
                x = (x * x) % MOD
                n //= 2
            return result

        def helper(b_digits):
            if not b_digits:
                return 1
            last_digit = b_digits.pop()
            part1 = mod_pow(helper(b_digits), 10)
            part2 = mod_pow(a, last_digit)
            return (part1 * part2) % MOD

        return helper(b[:])