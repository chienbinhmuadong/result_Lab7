import time
import random
import numpy as np

def calculate_time(func):
    def wrapper(*args, **kwargs):

        begin = time.perf_counter_ns()
        func(*args, **kwargs)
        end = time.perf_counter_ns()

        print(f'Total time taken in {func.__name__}: {end - begin} nanoseconds')

    return wrapper

array1 = np.array([random.random()*100 for i in range(0, 1000000)])
array2 = np.array([random.random()*100 for i in range(0, 1000000)])
array3 = [random.random()*100 for i in range(0, 1000000)]
array4 = [random.random()*100 for i in range(0, 1000000)]


@calculate_time
def num_py(array1, array2):
    multi = np.multiply(array1, array2)

num_py(array1, array2)


@calculate_time
def normal(array1, array2):
    multi = []
    for i in range(len(array1)):
        multi.append(array1[i] * array2[i])

normal(array3, array4)