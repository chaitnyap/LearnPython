dict = {'A':1, 'B':2, 'C':3, 'D':2, 'E':1}
count = {}
for value in dict.itervalues():
	count[value] = count.get(value,0) + 1
print [key for key, val in dict.iteritems() if count[val] == 1]
