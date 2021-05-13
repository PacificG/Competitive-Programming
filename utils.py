def allPairs(l):
    """
    Returns a generator that iterates over all pairs of elements in a list
    """
    n = len(l)
    for i in range(n):
        for j in range(i+1, n):
            yield (l[i], l[j])
