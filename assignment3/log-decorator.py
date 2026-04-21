import logging

# one time setup
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)

        function_name = "function: " + func.__name__
        logger.log(logging.INFO, function_name)

        positional_params = "positional parameters: " + (str(args) if args else "none")
        logger.log(logging.INFO, positional_params)

        keyword_params = "keyword parameters: " + (str(kwargs) if kwargs else "none")
        logger.log(logging.INFO, keyword_params)

        return_message = "return: " + (str(value) if value is not None else "none")
        logger.log(logging.INFO, return_message)

        logger.log(logging.INFO, '------------')

        return value
    
    return wrapper

@logger_decorator
def no_params():
    print("I would like to sleep")
no_params()

@logger_decorator
def variable_params(*args): 
    return True
variable_params(1, 2, 3, 4)

@logger_decorator
def kwargs_decorator(**kwargs):
    return logger_decorator
kwargs_decorator(a=1, b=2)
