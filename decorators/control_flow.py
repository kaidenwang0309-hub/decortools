'''Control flow functions for time (and conditionally) restrained decorators.'''

import time

def wait(seconds):
  time.sleep(seconds)

def while_true(condition):
  while condition:
    pass

def while_false(condition):
  while not condition:
    pass

  
