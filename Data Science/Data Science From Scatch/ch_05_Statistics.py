def median(v):
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2

    if n % 2 == 1:
        # if odd, return the middle value
        return sorted_v[midpoint]
    else:
        lo = sorted_v[midpoint - 1]
        hi = sorted_v[midpoint]
        return (lo + hi) / 2


# this isn't right if you don't from __future__ import division
def mean(x):
    return sum(x) / len(x)