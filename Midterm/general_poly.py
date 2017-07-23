def general_poly (L):
    """
    L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0
    """
    def f(x):
        '''
        '''
        k = []
        for i in range(len(L)-1,-1,-1):
            k.append(i)

        # now define function f, within to have as our output
        output = 0
        ourMultiples = []
        sumList = []
        for i in k:
            ourMultiples.append(x ** i)
        for i in range(0,len(L)):
            sumList.append(L[i] * ourMultiples[i])
        output = sum(sumList)
        return(output)
    return f
