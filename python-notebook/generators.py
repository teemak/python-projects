from time import sleep

def add1(x, y):
    return x + y

class Adder:
    def __init__(self):
        self.counter = 0

    def __call__(self,  x, y):
        self.counter += 1
        return x + y

add2 = Adder()

'''def compute():
    rv = []
    for i in range(10):
        sleep(.5)
        rv.append(i)
    return rv'''

class Compute:

    def __iter__(self):
        self.last = 0
        return self

    def __next__(self):
        rv = self.last
        self.last += 1
        if self.last > 10:
            raise StopIteration()
        sleep(.5)
        return rv

def compute():
    for i in range(10):
        sleep(.5)
        yield i

for val in compute():
    print(val)

class Api:
    def run_first(self):
        first()
    def run_second(self):
        second()
    def run_last(self):
        last()

def api():
    first()
    yield
    second()
    yield
    last()
    yield

# for x in xs:
#    pass

#xi = iter(xs)      => __iter__
#while True:
#   x = next(xi)    => __next__


