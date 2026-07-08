# decorators

# changes to title case

import functools


def to_upper(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        return func(*args, *kwargs) * 10

    return decorator


@to_upper
def addNum(num1, num2):
    return num1 + num2

print(addNum(1, 2))