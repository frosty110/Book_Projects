def vector_add(v, w):
    # adds corresponding elements
    return [vi + wi for vi, wi in zip(v, w)]

def vector_subtract(v, w):
    # adds corresponding elements
    return [vi - wi for vi, wi in zip(v, w)]

def vector_sum(vectors):
    result = vectors[0]
    for vector in vectors[0]:
        result = vector_add(result, vector)

    return result

from functools import reduce
# reduce function performs some computation on a list and returns the result
# higher-order function. We're taking the list vectors and passing each vector in vectors into vector_add.
def vector_sum_alt(vectors):
    return reduce(vector_add, vectors)

def scalar_multiply(c, v):
    """c is a number, v is a vector"""
    return [c * v_i for v_i in v]

def vector_mean(vectors):
    """compute the vector whose ith element is the mean of the
    ith elements of the input vectors"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i
               for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)

import math
def magnitude(v):
    return math.sqrt(sum_of_squares(v))   # math.sqrt is square root function

def squared_distance(v, w):
    """(v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
   return math.sqrt(squared_distance(v, w))

def distance(v, w):
    return magnitude(vector_subtract(v, w))