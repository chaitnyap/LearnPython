'''
check strict superset
Sample input:
1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12
Sample output:
False
'''
A = set(map(int, raw_input().strip().split()))
n = input()
res = True
while n and res:
    B = set(map(int, raw_input().strip().split()))
    if A.intersection(B) != B:
        res = False
    n -= 1
print res
