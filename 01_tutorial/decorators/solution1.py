import time, math

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} run in {round(end - start)} seconds.')
        return result
    return wrapper

@timer
def example(n):
    time.sleep(n)
    print('hdsaf')

example(5)