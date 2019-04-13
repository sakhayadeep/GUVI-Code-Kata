s = list(input().split())
for i in range(len(s)):
    x = s[i][0].upper()
    y = s[i][1:].lower()
    
    s[i] = x + y

s = " ".join(s)
print(s)