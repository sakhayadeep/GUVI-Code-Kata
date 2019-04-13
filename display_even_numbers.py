l, r = map(int, input().split())
even = list()
for i in range(l+1, r):
    if(i%2==0):
        even.append(i)

print(*even)