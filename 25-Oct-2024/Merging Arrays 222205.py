# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

inpt=input().split()
m, n = int(inpt[0]), int(inpt[1])

first = list(map(int,input().split()))
second = list(map(int,input().split()))

merged = []

i,j = 0, 0
while i<len(first) and j<len(second):
    if first[i]<=second[j]:
        merged.append(first[i])
        i+=1
    else:
        merged.append(second[j])
        j+=1
merged.extend(first[i:])
merged.extend(second[j:])
merged=' '.join(list(map(str,merged)))
print(merged)
