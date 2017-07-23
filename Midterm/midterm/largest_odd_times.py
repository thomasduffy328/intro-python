def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number
        of times in L. If no such element exists, returns None """
    # ask for the unique elements of input list, L
    uniqueElements = []
    for i in L:
        if i not in uniqueElements:
            uniqueElements.append(i)

    # now create a dictonary or tuple to find occurrences of each element
    occurrences = {}
    for i in uniqueElements:
        occurrences[i] = L.count(i)

    # then create odd dictionary
    odd_occurrences = {}
    for key in occurrences:
        if occurrences[key] % 2 != 0:
            odd_occurrences[key] = occurrences[key]

    # and of those elements, which is the max?
    if len(odd_occurrences) == 0:
        return None
    else:
        return(max(odd_occurrences))
