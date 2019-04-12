n = int(input())
x = list(map(int, input().split()))

d = dict()

for i in x:
    if(d.get(i) == None):
        d[i] = 1
    else:
        d[i] += 1
        
for i in d:
    if(d[i] == 1):
        print(i)