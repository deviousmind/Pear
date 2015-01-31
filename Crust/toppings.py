import time
import os
from Crust import decorator


def prepare():
    filepath = os.getenv('APPDATA') + '\\Pear'
    filename = 'pear.txt'
    full_path = filepath + '\\' + filename

    if not os.path.exists(filepath):
        os.makedirs(filepath)

    return full_path


def put_a_fork_in_it():
    print(decorator.warn('Terminating, please wait...'))
    time.sleep(1)
    print(decorator.warn('import Skynet'))
    print(decorator.warn('Attempting to terminate Sarah Conner...'))
    time.sleep(1)
    print(decorator.warn('I\'ll be back.'))
    time.sleep(1)