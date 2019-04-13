def make_dict(a):
    d = dict()
    for i in a:
        if(d.get(i) == None):
            d[i] = 1
        else:
            d[i] += 1
    return d

x,y = input().split()
x = list(x)
y = list(y)
x.sort()
y.sort()

n1 = len(x)
n2 = len(y)

x = make_dict(x)
y = make_dict(y)

if(n1 == n2):
    isomorphic = 'yes'
    for i,j in zip(x,y):
        if(x[i] != y[j]):
            isomorphic = 'no'

    print(isomorphic)

else:
    print('no')