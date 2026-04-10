from  functools import wraps

def authentication(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("------------")
        return func(*args, **kwargs)
    return wrapper