def is_perm(L1,L2):
    '''
    Given lists, L1 and L2. If both lists are permutations of one another
    (that is the elements are exactly the same just in a different order)
    then return True, otherwise return False
    '''
    # create clones to manipulate
    L1clone = L1[:]
    L2clone = L2[:]
    sameness = 0
    while len(L1clone) != 0:
        char = L1clone.pop(0)
        if char in L2clone:
            sameness += 1
            L2clone.remove(char)
    if sameness == len(L1):
        return True
    else:
        return False

def largest(L1,L2):
    '''
    Given lists, L1 and L2, find the most frequent matching occurrence in both
    L1 and L2 and return tuple with value, frequency, and type
    '''
    # we can assume that they are already permutations of each other
    frequencyList = []
    for i in L1:
        frequencyList.append(L1.count(i))
    frequencyMax = max(frequencyList)
    frequencyMaxIndex = 0
    for j in range(0,len(frequencyList)):
        if frequencyList[j] == frequencyMax:
            frequencyMaxIndex = j
    largestItem = L1[frequencyMaxIndex]
    output = (largestItem, frequencyMax, type(largestItem))
    return(output)

def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other.
            If they are permutations of each other, returns a
            tuple of 3 items in this order:
            the element occurring most, how many times it occurs, and its type
    '''
    if len(L1) != len(L2):
        return False
    if len(L1) == 0 and len(L2) == 0:
        return (None, None, None)
    elif is_perm(L1,L2):
        return largest(L1,L2)
    else:
        return False
