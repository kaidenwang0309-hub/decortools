'''Custom errors for decortools.'''

class TimeOutError():
  '''Raised when time runs out on try_for decorator.'''
  pass

class FailedCallError():
  '''Raised when a call fails with any of the conditionally-calling decorators.'''
  pass

class FalseConditionalError():
  '''Raised when conditional evaluates to False and stops execution in the 
  try_while and try_while_not decorators.'''
  pass
