import numpy as np


def difference(first_array, second_array):
    """Creates a list of list elements not present in others.
    Args:
        first_array (list): Lists to process.
        second_array (list): Lists to check.
    Returns:
        list: Difference between `others`.
    Example:
        >>> difference([1, 2, 3], [3, 4])
        [1, 2]
    .. versionadded:: 0.0.1
    """
    return list(set(first_array) - set(second_array))


def union(first_array, second_array):
    """Computes the union of the passed-in arrays.
    Args:
        first_array (list): List to union with.
        second_array (list): List to unionize with `first_array`
    Returns:
        list: Unionized list.
    Example:
        >>> union([1, 2, 3], [3, 4])
        [1, 2, 3, 4]
    .. versionadded:: 0.0.1
    """
    return list(set(first_array).union(second_array))


def ones(row, column):
    """Creates a two dimensional array filled with 1.
    Args:
        row (int): No of rows.
        column (int): No of columns.
    Returns:
        list: Two dimensional array filled with 1.
    Example:
        >>> ones(2, 4)
        array([[1 1 1 1]
               [1 1 1 1]])
    .. versionadded:: 0.0.1
    """
    return np.ones((row, column), dtype=int)
