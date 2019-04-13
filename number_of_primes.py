def count_prime(l, r):
    if(l < 2 and r < 2):
        return 0
    elif(l < 2 and r >= 2):
        l = 2

    count = 0
    for i in range(l,r+1):
        prime = 'yes'
        for j in range(2,(i//2)+1):
            if(i % j == 0):
                prime = 'no'

        if(prime == 'yes'):
            count += 1

    return count

l, r = map(int, input().split())

print(count_prime(l,r))