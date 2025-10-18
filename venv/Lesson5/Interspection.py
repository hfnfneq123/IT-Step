import sys
import time
import inspect

def first():
    pass

print(inspect.ismodule(time))
print(inspect.isclass(time))
print(inspect.isfunction(time))
print(sys.version)
print(sys.platform)