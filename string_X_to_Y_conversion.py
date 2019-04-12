"""
Given 2 strings X,Y convert X to Y as cheaply as possible. Let the cost of insertion, deletion and updation be 1. Print the minimum cost.
Example:
INPUT
BALL BALOON
OUTPUT
3    
"""
def convert(s1, s2):
    cost = 0
    n1 = len(s1)
    n2 = len(s2)
    
    ################ part 1 ######################
    if(s1 == s2):
        return cost

    ################ part 2 ######################
    s1,s2 = list(s1),list(s2)
    
    while(s1[0] != s2[0]):
        s1.pop(0)
        cost += 1
    
    n = len(s1)
    i = 0
    while(i<n):
        if(s1[i] not in s2):
            s1.pop(i)
            n -= 1
            cost += 1
        i += 1
        n -= 1

    for i in s2:
        if(i not in s1):
            cost += 1
    
    ################ part 3 ######################
    if((n1 > n2) and (cost == 0)):
        cost = n1 - n2 
    
    ##############################################
    return cost

X,Y = input().split()
print(convert(X, Y))
