import numpy as np
from scipy.ndimage import gaussian_filter
import pandas as pd

__all__ = ['rand_array', 'smooth_image','my_mat_solve','factorial_recursive','index_row']

def rand_array(shape):
    return np.random.rand(*shape)

def smooth_image(a, sigma=1):
    return gaussian_filter(a, sigma=sigma)

def my_mat_solve(A, b):
    return A.inv()*b

def factorial_recursive(n):
    total=1
    if n==1:
        return 1
    else:
        return factorial_recursive(n-1) * n

def index_row(df):
    return df.iloc[0]

    