# assume s is a set of lower-string characters
# write program that enumerates vowels in the string 's'
s = str(input('Enter a string: '))
# initialize list of vowels and empty vectors
vowels = ['a','e','i','o','u']
numVowels = 0
# loop thru char's asking if each is in vowels, if so + 1
for char in s:
    if char in vowels != False:
        numVowels = numVowels + 1
# print result
print('Number of Vowels:', numVowels)
