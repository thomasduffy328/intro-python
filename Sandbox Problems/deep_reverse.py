def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also
    reverses the order of the int elements in every element of L.
    It does not return anything.
    """
    tempL = []
    for i in range(len(L)-1,-1,-1):
        tempL.append(L[i][::-1])
    return tempL
