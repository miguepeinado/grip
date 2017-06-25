import numpy as np


def white(size=(512, 512)):
    """Create a white image
    :param
        size: size of the array
    :returns
        the array
    """
    arr = np.ones(size) * 255.
    return arr


def black(size=(512, 512)):
    """Create a black image
    :param
        size: size of the array
    :returns
        the array
    """
    arr = np.zeros(size)
    return arr


def chess(size=(512, 512)):
    """Create a four quadrant image
    :param
        size: size of the array
    :returns
        the array
    """
    arr = np.zeros(size)
    half_x = size[0]/2.
    half_y = size[1]/2.
    arr[:half_x, :half_y] = 255.
    arr[half_x:, half_y:] = 255.
    return arr
