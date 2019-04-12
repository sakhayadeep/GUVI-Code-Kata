n = input()
x = list(map(int, input().split()))

d = dict()

for i,j in enumerate(x):
    d[i] = j

x2 = list()

for i in d:
    if(d[i] == i):
        x2.append(i)

if(len(x2)>0):
    x2.sort()
    print(*x2)
else:
    print(-1)