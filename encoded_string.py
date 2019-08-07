s1 = list(input())
s2 = list(input())
for i in range(len(s1)):
    c1 = ord(s1[i])
    c2 = ord(s2[i]) - 96
    c1 = c1 + c2
    if c1 > 122:
        c1 = c1 - 122
        c1 += 96
    s1[i] = chr(c1)
print("".join(s1))
