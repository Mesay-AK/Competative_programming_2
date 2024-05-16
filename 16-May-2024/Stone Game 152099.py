# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        memo = {}

        def dp(i, j,turn):
            if j < i:
                return 0

            state = (i, j, turn)

            if state not in memo:
                if turn:
                    memo[state] = max(dp(i+1, j, not turn ) + piles[i] ,  dp(i, j-1,not turn) + piles[j])

                else: 
                    memo[state] = max(dp(i+1, j, not turn), dp(i, j-1, not turn))

            return memo[state]


        return dp(0, len(piles)-1, True )

            