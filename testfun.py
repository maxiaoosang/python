__author__ = 'xiaoma'


def f1():
    print 1
f1()

def f2(a):
    print a
f2(2)
f2('abcdddd')

def f3(a=1,b=2,c=3):
    print a,b,c
    print 'a',a
    print 'b',b
    print 'c=%d'%c
    return a,b+c

f3()
f3(5)
print f3(b=5,c=6)

c,d=f3(b=4,c=9)
print c
print d


fx=f3
fx()


fl=lambda x,y:x+y

print fl(2,3)








