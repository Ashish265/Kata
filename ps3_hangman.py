# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

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

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    count=0
    for i in range(len(lettersGuessed)):
        if lettersGuessed[i] in secretWord:
            count=count+1
            if count == len(secretWord):
                return True
            else:
                continue
    else:
        return False




def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    count = 0
    blank = ['_ '] * len(secretWord)

    for i, c in enumerate(secretWord):
        if c in lettersGuessed:
            count += 1
            blank.insert(count-1,c)
            blank.pop(count)
            if count == len(secretWord):
                return ''.join(str(e) for e in blank)
        else:
            count += 1
            blank.insert(count-1,'_')
            blank.pop(count)
            if count == len(secretWord):
                return ''.join(str(e) for e in blank)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    avail=string.ascii_lowercase
    avail1=list(avail)
    letterguess=set(lettersGuessed)
    for letter in letterguess:
        if letter in avail1:
            position=avail1.index(letter)
            del avail1[position]
    avail=" ".join(avail1)
    #print(avail)
    return(avail)
    

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
    # FILL IN YOUR CODE HERE..
    l=len(secretWord)
    lettersGuessed = []
    guess=str
    mistakeMade=8
    wordGuessed = False

    print("Welcome to the game, Hangman!")
    
    print("I am thinking of a word that is "+ str(l) + " letters long.")
    
    while mistakeMade>0 and mistakeMade <=8 and wordGuessed is False:
    	if getGuessedWord(secretWord,lettersGuessed)== secretWord:
    		print(" I am getting executed")
    		wordGuessed=True
    		break

    	print("You have "+ str(mistakeMade)+ " guesses left.")
    	print("Available letters : " + getAvailableLetters(lettersGuessed))
    	guess=input('Please guess a letter: ').lower()
    	if guess in secretWord:
    		if guess in lettersGuessed:
    			print("Oops! You've already guessed that letter: "+ getGuessedWord(secretWord, lettersGuessed))
    			print("----------------------------------")
    		else:
    			lettersGuessed.append(guess)
    			print("Good guess: "+ getGuessedWord(secretWord, lettersGuessed))
    			print("----------------------------------")
    	else:
    		if guess in lettersGuessed:
    			print("Oops! You've already guessed that letter: "+ getGuessedWord(secretWord, lettersGuessed))
    			print("----------------------------------")
    		else:
    			lettersGuessed.append(guess)
    			mistakeMade -=1
    			print(" Oops! That letter is not in my word: "+ getGuessedWord(secretWord, lettersGuessed))
    			print("----------------------------------")
    if wordGuessed == True:
    	return 'Congratulations, you won!'
    elif mistakeMade==0:
    	print(" Sorry, you ran out of guesses . The word was " + secretWord)
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
#print(secretWord)
hangman(secretWord)
