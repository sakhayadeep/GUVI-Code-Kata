s = input()
n = len(s)

s = list(s)

if(n % 2 == 0):
    for i in range(0,n-1,2):
        s[i], s[i+1] = s[i+1], s[i]

else:
    for i in range(0,n-2,2):
        s[i], s[i+1] = s[i+1], s[i]

s = "".join(s)

print(s)