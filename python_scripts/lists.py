#from functools import reduce

arr = [1, 2, 3]
cmd = "insert"
a = 10
getattr(arr, cmd)(2, a)
print arr


arr = [1, 2, 5, 9, 15, 3, 21, 22, 23]
def f(x): return x % 3 == 0 or x % 5 == 0
print filter(f, arr)

arr = [1, 2, 3, 4, 5]
def cube(x): return x*x*x
print map(cube, arr)

arr = [x for x in range(1,11)]
def add(x, y): return x + y
print reduce(add, arr)
print sum(arr)

arr = [x for x in range(1,11)]
def mult(x, y): return x * y
print reduce(mult, arr)

print map((lambda x: x **2), arr)
print reduce((lambda x, y: x * y), arr)

def incr(n): return lambda x: x + n
f = incr(6)
g = incr(10)
print f(10), g(10)

arr = [1, 11, 23, 2, 34, 12]
print sorted(arr)

# Enter your code here. Read input from STDIN. Print output to STDOUT
X = input()
Y = input()
Z = input()
N = input()
def f(res):
    if sum(res) != 2:
        return res
lt = [[x,y,z] for x in range(0,X+1) for y in range(0,Y+1) for z in range(0,Z+1)]
print filter(f,lt)
