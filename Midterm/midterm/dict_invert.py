def dict_invert(d):
    '''
    Takes in a dictionary with immutable values and
    returns the inverse of the dictionary
    '''
    reverse_d = {}
    # return dictionary with values as lists that are increasing

    # ask for unique values in dictonary
    uniqueElements = []
    for key in d:
        if d[key] not in uniqueElements:
            uniqueElements.append(d[key])

    # now point those unique elements to the keys of reverse_d
    for i in uniqueElements:
        reverse_d[i] = []


    # now find which values of first list correspond to reverse keys
    # return the keys of first list as values of second
    for i in uniqueElements:
        for key in d:
            if i == d[key]:
                reverse_d[i].append(key)
    for key in reverse_d:
        reverse_d[key] = (sorted(reverse_d[key]))
    return(reverse_d)
