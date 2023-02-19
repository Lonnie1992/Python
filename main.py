# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line
import this
import time
import math
import datetime as dt
import sys
import greet

print(this)


def wait(sec: int):
    time.sleep(sec)
    return 'nothing'


def my_sin(x):
    return math.sin(x)
    return my_sin


print(my_sin(9))


def iso_now():
    now = dt.datetime.now().strftime("%Y-%m-%dT%H:%M")
    return now


print(iso_now)


def platform():
    return sys.platform


def supergreeting_wrapper(name):
    return greet.supergreeting(name)
