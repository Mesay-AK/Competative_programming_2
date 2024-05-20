# Problem: Fedor and New Game - https://codeforces.com/contest/467/problem/B

n, m, k = map(int, input().split())

armies = []
for _ in range(m + 1):
    army = int(input())
    armies.append(army)

farmy = armies.pop()

friends = 0
for army in armies:
    difference = bin(farmy ^ army).count('1')
    if difference <= k:
        friends += 1

print(friends)