'''
Task:
You have a non-empty set s and you have to execute N commands given in N lines. Commands will be pop, remove and discard.
Input Format:
First line contains integer n, number of elements in set. 
Second line contains space separated elements of set s. All elements are non-negative integers, less than or equal to 9. 
Third line contains integer N, number of commands.
Next N lines contains pop, remove and discard commands.
Constraints:
0<n<20 ; 0<N<20
Output Format:
Print sum of elements of set 's' in output.
'''

#n = input()
#s = set(map(int, raw_input().strip().split()))
#cn = input()
n = 9
s = set(map(int, '1 2 3 4 5 6 7 8 9'.split()))
cn = 10
while cn:
	line = raw_input().strip().split()
	if len(line) == 1:
		cmd = 's.'+line[0]+'()'
	else:
		cmd = 's.'+line[0]+'('+line[1]+')'
	exec(cmd)
	cn -= 1
print sum(s)
