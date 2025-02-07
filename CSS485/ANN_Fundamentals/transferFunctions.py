import numpy as np

def hardlim(a):
    if isinstance(a, np.ndarray):
        a[a >= 0] = 1
        a[a < 0] = 0
        return a
    if a >= 0:
        return 1
    return 0

def hardlims(a):
    if isinstance(a, np.ndarray):
        a[a >= 0] = 1
        a[a < 0] = -1
        return a
    if a >= 0:
        return 1
    return -1