# Decorators
# Need of decorator - helps in adding functionalities to wrapper function

# Function as a decorator
# def decorator_function(original_function):
#     def wrapper_function(*args, **kwargs):
#         print('wrapper function executed before {}'.format(original_function.__name__))
#         return original_function(*args, **kwargs)
#     return wrapper_function

# def display():
#     print('display fucntion ran')
    
# dec_display = decorator_function(display)
# dec_display()

# decorator_function keyword is used to define a particular function
# @decorator_function                                             
# def display():
#     print('display fucntion ran')
    
# display()                                                           


# @decorator_function
# def display_info(name, age):
#     print('dispaly_info ran with arguments {}, {}'.format(name, age))
    
# display_info('Hooters', 25)






# instead of creating decorator function, decorator class can also be made (Class a decorator)
class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function
        
    # __call__ method acts as wrapper function to add functionalities
    def __call__(self, *args, **kwargs):
        print('wrapper function executed before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


# # decoratore_class keyword is used to define a particular method
@decorator_class                                               
def display():
    print('display fucntion ran')
    
display()                                                           

@decorator_class
def display_info(name, age):
    print('dispaly_info ran with arguments {}, {}'.format(name, age))
    
display_info('Hooters', 25)