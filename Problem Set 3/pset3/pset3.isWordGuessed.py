def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
    False otherwise
    '''
    # secretWord = input(str('Enter a word: '))
    # lettersGuessed = input(str('Enter guesses: '))
    guessList = list(lettersGuessed)
    secretList = list(secretWord)
    output = False

    while len(guessList) > 0:
        testLetter = guessList.pop(0)
        proceed = testLetter in secretList
        if proceed == True:
            index = secretList.index(testLetter)
            del(secretList[index])
    if len(secretList) == 0:
        output = True
    return(output)
