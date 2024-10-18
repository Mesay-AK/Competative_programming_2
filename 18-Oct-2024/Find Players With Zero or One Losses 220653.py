# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        winners = defaultdict(int)
        losers = defaultdict(int)

        for winner, loser in matches:
            winners[winner] += 1
            losers[loser] += 1

        win = set()
        lose = set()

        for winner in winners:
            if winner not in losers:
                win.add(winner)

        for loser in losers:
            if losers[loser] == 1:
                lose.add(loser)

        return sorted(win), sorted(lose)