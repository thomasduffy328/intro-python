L = [1,2,3,4]

# define powers, k
k = []
for i in range(len(L)-1,-1,-1):
    k.append(i)

# now define coefficients, n
n = L

    def f(x):
    '''
    '''
    output = 0
    ourMultiples = []
    sumList = []
    for i in k:
        ourMultiples.append(x ** i)
    for i in range(0,len(n)-1):
        sumList.append(n[i] * ourMultiples[i])
    output = sum(sumList)
    return(output)
return f
