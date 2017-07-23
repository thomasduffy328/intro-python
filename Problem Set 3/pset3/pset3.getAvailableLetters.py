def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    lettersRemaining = list(string.ascii_lowercase)
    for char in lettersGuessed:
        forDeletion = lettersRemaining.index(char)
        del(lettersRemaining[forDeletion])
    lettersRemaining = ''.join(str(i) for i in lettersRemaining)
    return(lettersRemaining)
