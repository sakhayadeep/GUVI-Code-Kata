n = int(input())
x = list(map(int, input().split()))

d = dict()

for i in x:
    if(d.get(i) == None):
        d[i] = 1
    else:
        d[i] += 1

x2 = list()

for i in d:
    if(d[i] > 1):
        x2.append(i)

x2.sort()
print(*x2)