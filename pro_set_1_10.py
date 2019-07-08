def find_sum(arr, a):
    S2 = 0
    for i in arr:
        if(i < a):
            S2 += i

    return S2

N = int(input())
arr = list(map(int, input().split()))
S = 0
for i in range(N):
    S += find_sum(arr[:i+1], arr[i])

print(S)