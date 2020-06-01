from functools import wraps

#fuunction to count how often a function is called
def function_call_counter(f):
    @wraps(f)
    def inner(*args, **kwargs):
        inner.counter+=1
        return f(*args,**kwargs)
    inner.counter = 0
    return inner