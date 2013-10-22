WRONG_GUESSES_ALLOWED=5


def hangman(word):
    
    """
    Requires word to be a string

    Repeats asking the player for a letter and telling the player whether their
    guess is in the word.

    If the player guesses right, the position(s) of the letter in the word is
    revealed.

    If the player guesses wrong a number of times, the player is informed that
    they lost.

    If the player guesses all the letters in the word, informs the player that
    they have won.
    """
    # We want to keep around a set of wrong_guesses, and a set of right_guesses.

    # Write a while loop (that stops when either the word is complete, or there
    # have been five wrong guesses) to keep asking the player for a guess, and
    # processing that guess.

def letter_pool(right_guesses, wrong_guesses):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    print alphabet
    for letter in range(len(alphabet)):
        for guess in right_guesses:
            if alphabet[letter] == guess:
                alphabet[letter] = " "
        for guess in wrong_guesses:
            if alphabet[letter] == guess:
                alphabet[letter] = " "
    return alphabet

print letter_pool("afg", "lmp")
    """
    Requires right_guesses to be a string of letters the player has guessed
    before correctly, and wrong_guesses to be a string of letters the player has
    guessed before incorrectly.

    Returns the alphabet minus any letter that has been guessed before
    """

def ask_for_letter(right_guesses, wrong_guesses):
    letter = raw_input("Please enter a letter: ")
    if letter.isalpha():
        if len(letter) == 1:
            if letter in right_guesses or letter in wrong_guesses:
                print "You've already guessed this letter."
            else:
                return letter
        else:
            print "Please only enter one letter."
    else:
        print "Please enter a valid letter."
        
print ask_for_letter("abc", "def")

    """
    Requires right_guesses to be a string of letters the player has guessed
    before correctly, and wrong_guesses to be a string of letters the player has
    guessed before incorrectly.

    Asks the player for a letter.

    If the input is exactly one letter and has not been guessed before, returns
    that letter.

    If the input is either not a letter, or not a single letter, or has been
    guessed before, asks the player for input again.
    """

def display_word_with_guesses(word, guesses):
    result = ""
    for character in word:
        if character in guesses:
            result += character
        else:
            result += "_"
    return result
	
    """
    Returns a string where every letter in the word contained in guesses is
    shown as that letter, and every letter in the word not contained in guesses
    is shown as an underscore.
    """
   

def example(word):
    """
    return the word, reversed
    """
    return word[::-1]

hangman("transcode")
