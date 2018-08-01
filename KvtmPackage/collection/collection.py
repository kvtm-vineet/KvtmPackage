
def group_by(collection, iteratee):
    """Creates an object composed of keys generated from the results of running
    each element of a `collection` through the iteratee.
    Args:
        collection (list|dict): Collection to iterate over.
        iteratee (str): Key of collection using which the grouping will be done.
    Returns:
        dict: Results of grouping by `iteratee`.
    Example:
        >>> results = group_by([{'a': 1, 'b': 2}, {'a': 3, 'b': 4}], 'a')
        >>> assert results == {1: [{'a': 1, 'b': 2}], 3: [{'a': 3, 'b': 4}]}
    .. versionadded:: 0.0.1
    """
    ret = dict()
    for o in collection:
        key = o[iteratee]
        ret.setdefault(key, [])
        ret[key].append(o)
    return ret
