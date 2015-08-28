'''
Find the uniq element in the list
Sample input:
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
Sample output:
8
'''
from collections import Counter
n = input()
r = map(int, raw_input().strip().split())
c = Counter(r)
print filter(lambda x: x[1] == 1, c.items())[0][0]
