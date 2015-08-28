'''
check subset in under 4 lines of code
Sample input:
3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2
Sample output:
True 
False
False
'''
for i in range(input()):
    a = input(); A = set(raw_input().split())
    b = input(); B = set(raw_input().split())
    print True if A.union(B) == B else False
