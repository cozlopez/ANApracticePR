import numpy as np
import numpy.random as random

def hash_string2int(net_id, maxint):
    """Convert string to integer in the range [0, maxint)."""
    sum_chars = 0
    for char in net_id:
        sum_chars += ord(char)
    return sum_chars % maxint

def rand(seed, n):
    """Custom pseudo-random numbers approximately uniform on [0,1]. Needed for
    consistency across Python versions/machines etc. where numpy implementation
    may change. (We're generating problem-inputs from usernames.)

    Args:
      seed (integer): Random number seed, required on every call to this fn.
      n (integer): Number of random numbers to return.

    Return:
      out (list of floats): Random numbers on [0,1]
    """
    out = []
    m, a, c = 2**32, 1103515245, 12345
    for i in range(n):
        seed = (a * seed + c) % m
        out.append(float(seed) / (m-1))
    return out

def get_data(net_id, u, v):
    """Test function unique for each student based on netid"""
    seed = hash_string2int(net_id, 2**32)
    a = rand(seed, 5)
    du = a[4]*np.sin(u) + a[3]*np.cos(v)
    dv = a[2]*np.sin(v) + a[1]*np.cos(u)
    return (du,dv)
