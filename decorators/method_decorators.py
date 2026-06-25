'''Implementation code for decorators that decorate methods is written here.'''

from functools import wraps

def repeat(times: int):
  def decorator(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
      for _ in range(times):
        func(self, *args, **kwargs)
    return wrapper
  return decorator

def repeat_until(condition: bool):
  def decorator(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
      while condition:
        func(self, *args, **kwargs)
    return wrapper
  return decorator

def do_while(condition: bool):
  def decorator(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
      func(self, *args, **kwargs)
      while condition:
        func(self, *args, **kwargs)
    return wrapper
  return decorator

def call_if(condition: bool, default_error=None, default_response=None):
  def decorator(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
      if condition:
        func(self, *args, **kwargs)
      else:
        if default_error and default_response is not None:
          raise ValueError("There cannot be both a default error and a default response.")
        elif default_error is not None:
          raise default_error
        elif default_response is not None:
          default_response()
        else:
          return
    return wrapper
  return decorator

def call_unless(condition, default_response=None, default_error=None):
  def decorator(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
      if condition:
        if default_response and default_error is not None:
          raise ValueError
        elif default_response is not None:
          default_response()
        elif default_error is not None:
          raise default_error
        else:
          return
      else:
        func(self, *args, **kwargs)
    return wrapper
  return decorator
