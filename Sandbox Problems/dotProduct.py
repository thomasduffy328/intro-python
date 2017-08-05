def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers
    '''
    # handle case where input are lists of different lengths
    if len(listA) != len(listB):
        raise ValueError('List A and List B must be of same length')

    prodList = []
    for i in range(0,len(listA)):
        prodList.append(listA[i] * listB[i])
    return sum(prodList)
