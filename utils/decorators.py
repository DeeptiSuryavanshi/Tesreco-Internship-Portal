import time

def log_performance(func):
    def wrapper(*args):
        start = time.time()

        result = func(*args)

        end = time.time()

        print("Function:", func.__name__)
        print("Execution Time:", end - start)
        print("Result:", result)

        return result

    return wrapper