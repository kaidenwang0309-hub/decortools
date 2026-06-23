from functools import wraps

def combine(dec1, dec2):
  def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
      @dec1
      @dec2
      func(*args, **kwargs)
    return wrapper
  return decorator

def method_combine(dec1, dec2):
  def decorator(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
      @dec1
      @dec2
      func(self, *args, **kwargs)
    return wrapper
  return decorator
