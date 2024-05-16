# Problem: D - Maximum Number of Zeroes - https://codeforces.com/gym/514644/problem/D

from collections import defaultdict
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

c = defaultdict(int)

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

extras = 0
for i in range(n):
    if a[i] != 0:
        res = gcd(b[i],a[i])
        t = (b[i]//res , a[i]//res)
        c[t] += 1
    elif a[i] == 0 and b[i] == 0:
        extras += 1
vals = list(c.values())
if len(vals):
    print(max(vals)+extras)
else:
    print(extras)