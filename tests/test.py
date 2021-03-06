from pytrace import notrace

def fib(n):
    if n in (1,2):
        return 1
    return fib(n - 1) + fib(n - 2)

def simple(arg):
    pass

@notrace
def test_no_trace(n):
    return n * 2
    
def default(arg=10):
    mix(10)

def vararg(*a):
    pass

def kwargs(**k):
    pass

def mix(a, b=1, *c, **d):
    pass

def raises(x):
    raise x

def exceptions():
    try:
        raises(ValueError("BLA"))
    except:
        pass
    else:
        assert False
    return "OK"
        
class A(object):

    def foo(self, a, b, c=None):
        return self


if __name__ == '__main__':
    import time
    t = time.time()
    simple(10)
    assert 200 == test_no_trace(100)
    vararg('', 20)
    kwargs(a=10, b=20)
    exceptions()
    A().foo(10, b=100)
    kwargs(a="DAAAAAAAAAAAAA", b=20)
    fib(4)
    mix(10, 20, 30, "bla", k="BLO")
    vararg(1, 2, 3)
    kwargs(a="BAAAAAAAAAAAAA", b=20)
    print time.time() - t
