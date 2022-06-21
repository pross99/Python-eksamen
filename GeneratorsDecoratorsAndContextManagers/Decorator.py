from functools import wraps


def my_logger(orig_func): 
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper

import time


@my_logger # Det samme som display_info = my_timer(dsiplay-info)
@my_timer
# Bruger 2 decoratorators på en ekelt function - det er fedt 
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Peter', 22)







# def outer_function(msg):
##    message = msg

#    def inner_function():
#         print(msg)
#     return inner_function

# hi_function = outer_function("hi")
# bye_function = outer_function("Bye")
