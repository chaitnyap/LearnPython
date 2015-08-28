'''
set operations
'''
#n = input()
#e = set(map(int, raw_input().strip().split()))
#m = input()
#f = set(map(int, raw_input().strip().split()))
e = set(map(int, '1 2 3 4 5 6 7 8 9'.split()))
f = set(map(int, '10 1 2 3 11 21 55 6 8'.split()))
print (e.union(f))
print (e.intersection(f))
print (e.difference(f))
print (e.symmetric_difference(f))
