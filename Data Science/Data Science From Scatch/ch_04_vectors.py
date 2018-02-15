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
def vector_sum(vectors):
    return reduce(vector_add, vectors)