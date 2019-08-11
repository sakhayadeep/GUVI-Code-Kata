s = input()
x = y = 0
d = 'x'
for i in s:
    if i == 'G':
        if d == 'x':
            x += 1
        elif d == '-x':
            x -= 1
        elif d == 'y':
            y += 1
        else:
            y -= 1
    elif i == 'L':
        if d == 'x':
            d = 'y'
        elif d == 'y':
            d = '-x'
        elif d == '-x':
            d = '-y'
        else:
            d = 'x'
    else:
        if d == 'x':
            d = '-y'
        elif d == '-y':
            d = '-x'
        elif d == '-x':
            d = 'y'
        else:
            d = 'x'

if x == y == 0:
    print('yes')
else:
    print('no')