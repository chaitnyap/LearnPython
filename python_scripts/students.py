# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
students = {}
for i in range(0,n):
    line = raw_input()
    print line
    temp = line.split()
    print temp
    print temp[:1]
    print temp[1:]
    students[temp[:1]] = temp[1:]
name = raw_input()
print students[name][0] + students[name][1] + students[name][2]
