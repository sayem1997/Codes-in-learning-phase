import hangman

word_list = hangman.load_words()


def find_same_char(my_word, other_word):
    position = 0
    while True:
        try:
            position += my_word.index['_', position]
            for char1 in my_word:
                if char1 in other_word[position]:
                    return True
            return False
        except ValueError:
            break



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

    for word in word_list:
        if match_with_gaps(my_word, word) == True:
                possible_matches = possible_matches + word + " "

    if possible_matches == '':
        print('No matches found')
    else:
        print(possible_matches[:-1])

