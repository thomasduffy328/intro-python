# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------
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

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    secretList = list(secretWord)
    indexList = []
    dupList = []
    fillMe = list('_' * len(secretWord))

    while len(lettersGuessed) > 0:
        testLetter = lettersGuessed.pop(0)
        if testLetter in secretList and secretList.count(testLetter) == 1:
            index = secretList.index(testLetter)
            fillMe[index] = testLetter
        if testLetter in secretList and secretList.count(testLetter) > 1:
            for i in range(0,len(secretList)):
                if secretList[i] == testLetter:
                    dupList.append(i)
            for i in dupList:
                fillMe[i] = testLetter
    output = ''.join(str(i) for i in fillMe)
    return(output)

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

# --------
# THE GAME
# --------
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # first prompt
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', str(len(secretWord)), 'letters long')
    guessesLeft = 8
    lettersGuessed = []
    print('--------')

    while guessesLeft > 0:
        print('You have', str(guessesLeft), 'guesses left')
        availableLetters = getAvailableLetters(lettersGuessed)
        print('Available letters:', availableLetters)
        guess = str(input('Please guess a letter: '))
        guess = guess.lower()
        if guess in availableLetters:
            lettersGuessed.append(guess)
            if guess in secretWord:
                print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
                print('--------')
            else:
                print('Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))
                print('--------')
                guessesLeft -= 1
        else:
            print('Oops! You\'ve already guessed that letter:', getGuessedWord(secretWord, lettersGuessed))
            print('--------')
        if isWordGuessed(secretWord, lettersGuessed):
            break
    if isWordGuessed(secretWord, lettersGuessed):
        print('Congratulations, you won!')
    else:
        print('Sorry, you ran out of guesses. The word was', secretWord)
