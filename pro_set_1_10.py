def calculate(a):
    if(a == 0):
        return 0
    else:
        return a+calculate(a-1)

def fib_sum(a):
    return calculate(a)-a

N = int(input())
arr = list(map(int, input().split()))
S = 0

for i in arr:
    S += fib_sum(i)

print(S)