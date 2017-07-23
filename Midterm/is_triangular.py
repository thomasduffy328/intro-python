def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    ourSums = []
    for i in range(1,k):
        b = sum(range(1,i))
        ourSums.append(b)
    if k in ourSums:
        return True
    elif k == 1:
        return True
    else:
        return False
