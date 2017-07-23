def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
# secretWord = input(str('Enter a word: '))
# lettersGuessed = input(str('Enter guesses: '))
    guessList = list(lettersGuessed)
    secretList = list(secretWord)
    indexList = []
    output = 'Something went wrong :('
    fillMe = list('_' * len(secretWord))

    while len(guessList) > 0:
        testLetter = guessList.pop(0)
        proceed = testLetter in secretList
        if proceed == True:
            for i in range(0,len(secretList)):
                if secretList[i] == testLetter:
                    indexList.append(i)
            for i in indexList:
                fillMe[i] = testLetter
    output = ''.join(str(i) for i in fillMe)
    return(output)
