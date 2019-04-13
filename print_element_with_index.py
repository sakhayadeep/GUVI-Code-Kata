n = input()
x = list(map(int, input().split()))

for i,j in enumerate(x):
    print(j, i, end="\n")