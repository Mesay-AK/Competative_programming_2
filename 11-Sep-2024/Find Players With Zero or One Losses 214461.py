# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        winner = defaultdict(int)
        loser = defaultdict(int)

        for game in matches:
            winner[game[0]] += 1
            loser [game[1]] += 1

        win = set()
        lose = set()

        for i in winner:
            if i not in loser:
                win.add(i)

        for i in loser:
            if loser[i] == 1:
                lose.add(i) 

        return sorted(win), sorted(lose)                