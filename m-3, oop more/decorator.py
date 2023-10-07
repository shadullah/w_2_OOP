import math

# def timer(func):
#     def inner(*args):
#         print('time started')
#         # print(func)
#         func(*args)
#         print('time ended')
#     return inner

def timer(func):
    def inner(*args, **kargs):
        print('time started')
        # print(func)
        func(*args, **kargs)
        print('time ended')
    return inner

# timer()()

@timer
def get_factor(n):
    print('factorial starting')
    res  = math.factorial(n)
    print(f'factorial of {n} is {res}')

get_factor(n=10)

# vejailla way to decorate
# timer(get_factor)()
