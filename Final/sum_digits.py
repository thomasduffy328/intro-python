def sum_digits(s):
    """
    assumes s a string
    Returns an int that is the sum of all of the digits in s.
    If there are no digits in s it raises a ValueError exception.
    """
    sList = list(s)
    numList =[]
    for i in range(0, len(sList)):
        try:
            numList.append(int(sList[i]))
        except ValueError:
            pass
    if len(numList) == 0:
        raise ValueError
    return sum(numList)
