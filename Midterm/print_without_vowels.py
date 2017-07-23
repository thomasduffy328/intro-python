def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    sList = list(s)
    indices = []
    for i in range(0,len(sList)):
        if sList[i] in vowels:
            indices.append(i)
    for i in reversed(indices):
        del(sList[i])
    s = ''.join(str(x) for x in sList)
    print(s)
