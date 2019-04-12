N = int(input())
st = list()

for i in range(N):
    st.append(input())

def find_common_prefix(st1, st2):
    for i,s in enumerate(st1):
        if(s != st2[i]):
            return st1[:i]
    return st1

if(N > 1):
    common_prefix = find_common_prefix(st[0], st[1])

    if(N > 2):
        for i in range(N-1):
            new_common_prefix = find_common_prefix(st[i], st[i+1])
            if(len(new_common_prefix) < len(common_prefix)):
                common_prefix = new_common_prefix

    print(common_prefix)
else:
    print(st[0])