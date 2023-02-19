# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line
name = 'John'


def greet(name):
    greeting = f'Hello, {name}!'
    return greeting


print(greet(name))


def add(a, b, c):
    adding = a + b + c
    return adding


print(add(1, 2, 3))


def positive(a):
    pos = a > 0
    return pos


print(positive(-1))


def negative(a):
    neg = a < 0
    return neg


print(negative(-1))
