'''Implementation code for decorators that decorate functions is written here.'''

from functools import wraps

def repeat(times: int):
  def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
      for _ in range(times):
        func(*args, **kwargs)
    return wrapper
  return decorator

def repeat_until(condition: bool):
  def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
      while not condition:
        func(*args, **kwargs)
    return wrapper
  return decorator

def repeat_while(condition: bool):
  def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
      while condition:
        func(*args, **kwargs)
    return wrapper
  return decorator

def do_while(condition: bool):
  def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
      func(*args, **kwargs)
      while condition:
        func(*args, **kwargs)
    return wrapper
  return decorator

def call_if(condition: bool, default_error=None, default_response=None):
  def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
      if condition:
        func(*args, **kwargs)
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

def call_unless(condition, default_error=None, default_response=None):
  def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
      if condition:
        if default_response and default_error is not None:
          raise ValueError
        elif default_error is not None:
          raise default_error
        elif default_response is not None:
          default_response()
        else:
          return
        else:
          func(*args, **kwargs)
    return wrapper
  return decorator
