import time


def tic_toc(func):
    def wrapper(*args, **kwargs):
        tic = time.perf_counter()
        value = func(*args,**kwargs)
        toc = time.perf_counter()
        print(f'{func.__name__} took {round(toc-tic,4)}s')
        return value
    return wrapper
