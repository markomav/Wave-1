W = int(input())
L = int(input())
if L>=0 and W>=0:
    A = L*W/43560
    print(A*100//1/100 , 'acres')
if L<=0 or W<=0:
    print('distances entered cannot be negative.')