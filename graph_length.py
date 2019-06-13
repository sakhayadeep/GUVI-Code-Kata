#shky
def get_sum(UV_list):
    rejects = []
    last = '1'
    sum = 1
    for i in UV_list:
        if(last == i[0]):
            sum += int(i[2])
            last = i[2]
        else:
            rejects.append(i)

    return (sum, rejects)

#driver code
N, M = map(int,input().split())

UVs = []
for i in range(M):
    UV = input()
    UVs.append(UV)

result = get_sum(UVs)

while True:
    new_result = get_sum(result[1])
    if(new_result[0] > result[0]):
        result = new_result
    else:
        break
print(result[0])
