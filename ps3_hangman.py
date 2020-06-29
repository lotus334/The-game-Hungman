# Hangman game

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
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

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
        False otherwise
    '''
    for index in range(len(secretWord)):
        if secretWord[index] not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = []
    for index in range(len(secretWord)):
        if secretWord[index] not in lettersGuessed:
            result.append('_ ')
        else:
            result.append(secretWord[index])
    return ''.join(result)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    availableLetters = []
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            availableLetters.append(letter)
    return ''.join(sorted(availableLetters))
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    '''
    availableGuesses = 8
    lettersGuessed = []
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', str(len(secretWord)), 'letters long.')
    while availableGuesses != 0 and isWordGuessed(secretWord, lettersGuessed) == False:
        print('-------------')
        print('You have', availableGuesses, 'guesses left.')
        print('Available letters:', getAvailableLetters(lettersGuessed))
        letter = input('Please guess a letter: ')
        if letter not in lettersGuessed and letter in secretWord:
            lettersGuessed.append(letter)
            print('Good guess: ', end = '')
        elif letter not in lettersGuessed and letter not in secretWord:
            print('Oops! That letter is not in my word: ', end = '')
            lettersGuessed.append(letter)
            availableGuesses -= 1
        elif letter in lettersGuessed:
            print("Oops! You've already guessed that letter: ", end = '')
        print(getGuessedWord(secretWord, lettersGuessed))
    print('-----------')
    if isWordGuessed(secretWord, lettersGuessed) == True:
        print('Congratulations, you won!')
    else:
        print('Sorry, you ran out of guesses. The word was ' + secretWord + '.')

secretWord = chooseWord(wordlist).lower()
print(hangman(secretWord))

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
