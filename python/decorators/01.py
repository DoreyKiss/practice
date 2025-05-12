def my_decorator(func):
    '''Decorator function'''
    def wrapper(): 
        '''Return string F-I-B-O-N-A-C-C-I'''
        return 'F-I-B-O-N-A-C-C-I'
    return wrapper

@my_decorator
def pfib():
    '''Return Fibonacci'''
    return 'Fibonacci'


print(pfib())