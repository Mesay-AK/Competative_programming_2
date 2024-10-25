# Problem: Number of smaller - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B

inpt=input().split()
n, m = int(inpt[0]), int(inpt[1])

first = list(map(int, input().split()))
second = list(map(int, input().split()))

count=0
i, j = 0, 0
while i<n and j<m:
    if first[i] < second[j]:
        count+=1
        i+=1
    else:
        second[j]=count
        j+=1

while j<m:
    second[j]=count
    j+=1
rslt = ' '.join(list(map(str,second)))
print(rslt)