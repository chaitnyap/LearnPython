class A:
    def __init__(self, name):
        self.name = name
        print "base class", self.name

    def method(self, something):
        print str(something)

    def setName(self, name):
        self.name = "new name"

    def getName(self):
        return self.name
        

class B(A):
    def __init__(self, name):
        print "sub class"
        #A.__init__(self,name)
        A(name)
        #A.method(self,123)
        #print
        

        
beta = B("a name")
print "something", beta.getName()
