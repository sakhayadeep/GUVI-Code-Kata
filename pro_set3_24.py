x = int(input())
ls = []
for i in range(2**x):
    t = format(i, 'b')
    while len(t) < x:
        t = '0' + t
    ls.append(t)

ls.sort(key=lambda c: c.count('1'))
print(*ls, sep="\n")