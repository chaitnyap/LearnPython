a = 10
b = 5
print "A# before", id(a), a
print "B# before", id(b), b
a = a - 1 - 4
b += 5
print "A# after deletion", id(a), a
print "B# after addition", id(b), b
a -= 6
b += 6
print "A# after deletion", id(a), a
print "B# after addition", id(b), b
a = 16
b = -1
print "A# after deletion", id(a), a
print "B# after addition", id(b), b
