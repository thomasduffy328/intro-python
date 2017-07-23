s = str(input('Enter a string: '))
# initialize empty vectors
numBobs = 0
bobTest = str('')
# if b is found, ask if it is beginning of 'bob'
for i in range(0,len(s)-1):
    if s[i] == 'b':
        bobTest = s[i:(i+3)] # 'bob' is 3 char's long
    else:
        bobTest = ''
    if bobTest == 'bob':
        numBobs = numBobs + 1
print('Number of times bob occurs is:', numBobs)
