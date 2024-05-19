# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

n = int(input())

for i in range(n):
    num = int(input())
    if num == 1:
        print(3)
        continue

    res = 0
    num = bin(num)[2:]

    for l in range(len(num)-1, -1, -1):
        if num[l] == '1':
            break
        res += 1

    if res == len(num)-1:
        res = 2**res + 1
        print(res)

    else:
        print(2**res)