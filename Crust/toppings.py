import time
from Crust import decorator


def put_a_fork_in_it():
    print(decorator.warn('Terminating, please wait...'))
    time.sleep(1)
    print(decorator.warn('import Skynet'))
    print(decorator.warn('Attempting to terminate Sarah Conner...'))
    time.sleep(1)
    print(decorator.warn('I\'ll be back.'))
    time.sleep(1)