from functools import reduce


def f(x, y):
    return x + y


def deprecated_version_of(fa,newname=None):
    if newname is None: newname = f.__name__
    def fdepr(*a, **kw):
        for n in a:
            print(n)
        for x in kw:
            print(x,kw[x])
        return fa(*a, **kw)
    return fdepr

class ttt:
    def p(self,x,y):
        return x+y

ttt.pold = deprecated_version_of(ttt.p)


if __name__ == '__main__':
    r = reduce(f, [1, 2, 3, 4, 5, 6])
    print(r)

    t=ttt()
    r1=t.pold(1,y=3) #这里函数传参（如果同时使用元组和字典）按顺序就不会错，不按顺序就会报错
    print(r1)

    # r = reduce(t.pold, [1, 2, 3, 4, 5, 6])
    # print(r)

    #r2=f(y=2,1) #这个和这正常的函数调用是一致的
    #print(r2)
