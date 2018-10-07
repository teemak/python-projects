from time import time

def func():
    return 1

func()

def hello(name="Tee"):
    return 'Hi Tee'

def other(some_def_func):
    print('Other code runs here!')
    print(some_def_func())

    '''print('The hello() function has been run')

    def greet():
        return '\tThis is the greet() function inside hello()'

    def welcome():
        return '\tThis is the welcome() inside hello'

    print(greet())
    print(welcome())
    print('This is the end of the hello()')

    print('I am going to return a function')

    if name == 'Tee':
        return greet
    else:
        return welcome'''

def new_decorator(og_func):
    def wrap_func():
        print('Some extra code, before og code')
        og_func()
        print('Some extra code, after og code')
    return wrap_func


@new_decorator
def func_needs_decorator():
    print('I want to be decorated')

print(time())

def timer(func):
    def f(*args, **kwargs):
        before = time()
        rv = func(*args, **kwargs)
        after = time()
        print('elapsed:', int(after - before))
        return rv
    return f

@timer
def add(x, y=10):
    return x + y
#add = timer(add)

@timer
def sub(x, y=10):
    return x - y
#sub = timer(sub)

print('add(10)\t',    add(10))
print('add(20,30)\t', add(20,30))
print('add(a,b)\t',   add('a','b'))
print('sub(10)\t',    sub(10))
print('sub(20,30)\t', sub(20,30))
