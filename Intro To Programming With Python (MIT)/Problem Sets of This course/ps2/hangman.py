# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    false = 0

    for index in range(len(secret_word)):
        if secret_word[index] not in letters_guessed:
            false += 1

    if false > 0:
        return False
    else:
        return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    for index in range(len(secret_word)):
        if secret_word[index] not in letters_guessed:
            secret_word = secret_word.replace(secret_word[index], '_')

    secret_word_final = ''
    for position in range(len(secret_word)):
        if position != (len(secret_word) - 1):
            secret_word_final = secret_word_final + secret_word[position] + ' '
        else:
            secret_word_final = secret_word_final + secret_word[position]

    return secret_word_final


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters = string.ascii_lowercase

    for item in letters_guessed:
        letters = letters.replace(item, '')

    return letters


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to game Hangman!\n')
    print('I am thinking of a word that is {} letter long.\n'.format(len(secret_word)))
    print('- ' * 6)
    print('You have 3 warning left!')
    print('You have 6 guess left!\n')
    print('Available letters: {}.\n'.format(string.ascii_lowercase))
    guess = 6
    warning = 3
    list_of_letters = list(secret_word)
    available_letters = string.ascii_lowercase
    available_letters_list = list(available_letters)
    list_of_guessed_letters = []

    while guess >= 1:
        guessed_letter = input('Please geuss a letter: ')
        if guessed_letter not in list_of_guessed_letters:
            if guessed_letter not in ['a', 'e', 'i', 'o', 'u']:
                if guessed_letter in available_letters_list:
                    if guessed_letter in list_of_letters:
                        list_of_guessed_letters.append(guessed_letter)
                        print('Good guess: ', get_guessed_word(secret_word, list_of_guessed_letters))
                        print('- ' * 6)
                        print('You have {} warning left.\n'.format(warning))
                        print('You have {} guess/es left. \n'.format(guess))
                        available_letter = get_available_letters(guessed_letter)
                        print('Avalable letters: ', available_letter)

                    else:
                        list_of_guessed_letters.append(guessed_letter)
                        print('Oopps! That letter is not in my word: ',
                              get_guessed_word(secret_word, list_of_guessed_letters))
                        print('- ' * 6)
                        guess -= 1
                        print('You have {} warning left.\n'.format(warning))
                        print('You have {} guess/es left. \n'.format(guess))
                        available_letter = get_available_letters(guessed_letter)
                        print('Avalable letters: ', available_letter)

                else:
                    if warning != 0:
                        list_of_guessed_letters.append(guessed_letter)
                        warning -= 1
                        print("Oopps! That letter is not a valid letter. You have {} warning/es left: {} \n"
                              .format(warning, get_guessed_word(secret_word, list_of_guessed_letters)))
                        print('- ' * 6)
                        available_letter = get_available_letters(guessed_letter)
                        print('Avalable letters: ', available_letter)

                    else:
                        list_of_guessed_letters.append(guessed_letter)
                        guess -= 1
                        print("Oopps! That letter is not a valid letter. You have {} guess/es left: {} \n"
                              .format(guess, get_guessed_word(secret_word, list_of_guessed_letters)))
                        print('- ' * 6)
                        available_letter = get_available_letters(guessed_letter)
                        print('Avalable letters: ', available_letter)

            else:
                if guessed_letter in available_letters_list:
                    if guessed_letter in list_of_letters:
                        list_of_guessed_letters.append(guessed_letter)
                        print('Good guess: ', get_guessed_word(secret_word, list_of_guessed_letters))
                        print('- ' * 6)
                        print('You have {} warning left.\n'.format(warning))
                        print('You have {} guess/es left. \n'.format(guess))
                        available_letter = get_available_letters(guessed_letter)
                        print('Avalable letters: ', available_letter)

                    else:
                        list_of_guessed_letters.append(guessed_letter)
                        print('Oopps! That letter is not in my word: ',
                              get_guessed_word(secret_word, list_of_guessed_letters))
                        print('- ' * 6)
                        guess -= 2
                        print('You have {} warning left.\n'.format(warning))
                        print('You have {} guess/es left. \n'.format(guess))
                        available_letter = get_available_letters(guessed_letter)
                        print('Avalable letters: ', available_letter)

                else:
                    if warning != 0:
                        list_of_guessed_letters.append(guessed_letter)
                        warning -= 1
                        print("Oopps! That letter is not a valid letter. You have {} warning/es left: {} \n"
                              .format(warning, get_guessed_word(secret_word, list_of_guessed_letters)))
                        print('- ' * 6)
                        available_letter = get_available_letters(guessed_letter)
                        print('Avalable letters: ', available_letter)

                    else:
                        list_of_guessed_letters.append(guessed_letter)
                        guess -= 1
                        print("Oopps! That letter is not a valid letter. You have {} guess/es left: {} \n"
                              .format(guess, get_guessed_word(secret_word, list_of_guessed_letters)))
                        print('- ' * 6)
                        available_letter = get_available_letters(guessed_letter)
                        print('Avalable letters: ', available_letter)

        else:
            if warning != 0:
                list_of_guessed_letters.append(guessed_letter)
                warning -= 1
                print("Oopps! That letter was entered earliar. You have {} warning/es left: {} \n"
                      .format(warning, get_guessed_word(secret_word, list_of_guessed_letters)))
                print('- ' * 6)
                available_letter = get_available_letters(guessed_letter)
                print('Avalable letters: ', available_letter)

            else:
                list_of_guessed_letters.append(guessed_letter)
                guess -= 1
                print("Oopps! That letter was entered earliar. You have {} guess/es left: {} \n"
                      .format(guess, get_guessed_word(secret_word, list_of_guessed_letters)))
                print('- ' * 6)
                available_letter = get_available_letters(guessed_letter)
                print('Avalable letters: ', available_letter)

    if guess == 0 and secret_word != get_guessed_word(secret_word, list_of_guessed_letters):
        print('You have run out of the guess! You loose! :( ')


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        and my_word and other_word are of the same length;
        False otherwise:

     >>> match_with_gaps("te_ t", "tact")
    False
    >>> match_with_gaps("a_ _ le", "banana")
    False
    >>> match_with_gaps("a_ _ le", "apple")
    True
    >>> match_with_gaps("a_ ple", "apple")
    False
    '''
    my_word_without_space = my_word.replace(' ', '')
    if len(my_word_without_space) == len(other_word):
        if my_word_without_space.count('_') > 1:
            for index in range(len(my_word_without_space)):
                if my_word_without_space[index] != '_' and my_word_without_space[index] != \
                        other_word[index]:
                    return False

            return True
        else:
            return False
    else:
        return False
    



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    >>> show_possible_matches("t_ _ t")
    tact tart taut teat tent test text that tilt tint toot tort tout trot tuft twit
    >>> show_possible_matches("abbbb_ ")
    No matches found
    >>> show_possible_matches("a_ pl_ ")
    ample amply
    '''
    possible_matches = ""

    for word in wordlist:
        if match_with_gaps(my_word, word) == True:
            possible_matches = possible_matches + word + " "

    if possible_matches == '':
        print('No matches found')
    else:
        print(possible_matches[:-1])

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to game Hangman!\n')
    print('I am thinking of a word that is {} letter long.\n'.format(len(secret_word)))
    print('- ' * 6)
    print('You have 3 warning left!')
    print('You have 6 guess left!\n')
    print('Available letters: {}.\n'.format(string.ascii_lowercase))
    guess = 6
    warning = 3
    list_of_letters = list(secret_word)
    available_letters = string.ascii_lowercase
    available_letters_list = list(available_letters)
    list_of_guessed_letters = []

    while guess >= 1:
        guessed_letter = input('Please geuss a letter: ')
        if guessed_letter == '*':
            print("Possible Letters are: \n")
            show_possible_matches(secret_word)
            print('- ' * 6)
            available_letter = get_available_letters(guessed_letter)
            print('Avalable letters: ', available_letter)
        else:
            if guessed_letter not in list_of_guessed_letters:
                if guessed_letter not in ['a', 'e', 'i', 'o', 'u']:
                    if guessed_letter in available_letters_list:
                        if guessed_letter in list_of_letters:
                            list_of_guessed_letters.append(guessed_letter)
                            print('Good guess: ', get_guessed_word(secret_word, list_of_guessed_letters))
                            print('- ' * 6)
                            print('You have {} warning left.\n'.format(warning))
                            print('You have {} guess/es left. \n'.format(guess))
                            available_letter = get_available_letters(guessed_letter)
                            print('Avalable letters: ', available_letter)

                        else:
                            list_of_guessed_letters.append(guessed_letter)
                            print('Oopps! That letter is not in my word: ',
                                  get_guessed_word(secret_word, list_of_guessed_letters))
                            print('- ' * 6)
                            guess -= 1
                            print('You have {} warning left.\n'.format(warning))
                            print('You have {} guess/es left. \n'.format(guess))
                            available_letter = get_available_letters(guessed_letter)
                            print('Avalable letters: ', available_letter)

                    else:
                        if warning != 0:
                            list_of_guessed_letters.append(guessed_letter)
                            warning -= 1
                            print("Oopps! That letter is not a valid letter. You have {} warning/es left: {} \n"
                                  .format(warning, get_guessed_word(secret_word, list_of_guessed_letters)))
                            print('- ' * 6)
                            available_letter = get_available_letters(guessed_letter)
                            print('Avalable letters: ', available_letter)

                        else:
                            list_of_guessed_letters.append(guessed_letter)
                            guess -= 1
                            print("Oopps! That letter is not a valid letter. You have {} guess/es left: {} \n"
                                  .format(guess, get_guessed_word(secret_word, list_of_guessed_letters)))
                            print('- ' * 6)
                            available_letter = get_available_letters(guessed_letter)
                            print('Avalable letters: ', available_letter)

                else:
                    if guessed_letter in available_letters_list:
                        if guessed_letter in list_of_letters:
                            list_of_guessed_letters.append(guessed_letter)
                            print('Good guess: ', get_guessed_word(secret_word, list_of_guessed_letters))
                            print('- ' * 6)
                            print('You have {} warning left.\n'.format(warning))
                            print('You have {} guess/es left. \n'.format(guess))
                            available_letter = get_available_letters(guessed_letter)
                            print('Avalable letters: ', available_letter)

                        else:
                            list_of_guessed_letters.append(guessed_letter)
                            print('Oopps! That letter is not in my word: ',
                                  get_guessed_word(secret_word, list_of_guessed_letters))
                            print('- ' * 6)
                            guess -= 2
                            print('You have {} warning left.\n'.format(warning))
                            print('You have {} guess/es left. \n'.format(guess))
                            available_letter = get_available_letters(guessed_letter)
                            print('Avalable letters: ', available_letter)

                    else:
                        if warning != 0:
                            list_of_guessed_letters.append(guessed_letter)
                            warning -= 1
                            print("Oopps! That letter is not a valid letter. You have {} warning/es left: {} \n"
                                  .format(warning, get_guessed_word(secret_word, list_of_guessed_letters)))
                            print('- ' * 6)
                            available_letter = get_available_letters(guessed_letter)
                            print('Avalable letters: ', available_letter)

                        else:
                            list_of_guessed_letters.append(guessed_letter)
                            guess -= 1
                            print("Oopps! That letter is not a valid letter. You have {} guess/es left: {} \n"
                                  .format(guess, get_guessed_word(secret_word, list_of_guessed_letters)))
                            print('- ' * 6)
                            available_letter = get_available_letters(guessed_letter)
                            print('Avalable letters: ', available_letter)

            else:
                if warning != 0:
                    list_of_guessed_letters.append(guessed_letter)
                    warning -= 1
                    print("Oopps! That letter was entered earliar. You have {} warning/es left: {} \n"
                          .format(warning, get_guessed_word(secret_word, list_of_guessed_letters)))
                    print('- ' * 6)
                    available_letter = get_available_letters(guessed_letter)
                    print('Avalable letters: ', available_letter)

                else:
                    list_of_guessed_letters.append(guessed_letter)
                    guess -= 1
                    print("Oopps! That letter was entered earliar. You have {} guess/es left: {} \n"
                          .format(guess, get_guessed_word(secret_word, list_of_guessed_letters)))
                    print('- ' * 6)
                    available_letter = get_available_letters(guessed_letter)
                    print('Avalable letters: ', available_letter)

    if guess == 0 and secret_word != get_guessed_word(secret_word, list_of_guessed_letters):
        print('You have run out of the guess! You loose! :( ')




# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


# if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)