__author__ = 'xiaoma'


def f1(a):
    def f2(b):
        return a+b
    return f2
q=f1(10)
print q
p=f1(20)
print p

print q(1)
print q(2)

print p(1)