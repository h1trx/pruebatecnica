from  functools import wraps

def auththentication(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("------------")
        return func(*args, **kwargs)
    return wrapper