import random
import string

alphabet = []
alphabet.extend('abcdefghijklmnopqrstuvwxyz')

def load_words():
    print "Loading word list from file..."
    inFile = open("words.txt", 'r', 0)
    line = inFile.readline()
    wordlist = string.split(line)
    print " ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# from here, you should complete the empty functions

def make_init_state(word):
    """
    make initial state list according to the number of letters in selected word
    and return it
    
    e.g. word = 'apple', state = ['_', '_', '_', '_', '_'] 
    """
    state = []
    
    # start
    for index in range (len(word)):
        state.append("_")
    # end
    return state

def compare_list_str(_list, _str):
    """
    You may use the same function in problem 3. 
    """
   
    # start
    for index in range(len(_list)):
        if _list[index] != _str[index]:
            return False
    return True
    # end


def listToString(list, space=False):
    """
    Convert the list to string and return it.
    e.g. if list = ['a', 'p', 'p', '_', 'e'], then return "app_e".
    or if space is True, then return "a p p _ e".
    """
    
    # start
    if space:
        return " ".join(list)
    else:
        return "".join(list)
    # end


def getGuess(letters):
    """
    Get a guessing letter from the user. 
    If the user select the letter which are not alphabet or the one which 
    are already chosen, the function prints 
    "Please select among available letters!" 
    and currently available letters, then asks again. 
    Repating this until the user select correct letter. 
    
    !!! IMPORTANT !!!
    Though the user chose the uppercase letter, you should deal with it 
    as same as the lowercase letter.
    (hint. string object has a method lower() and upper(). Check out Python help)
    """
    
    # start
    while True:
        input_letter = raw_input("Please guess a letter: ")
        if not input_letter.lower() in letters:
            print "Please select among available letters! \n"
            print "Available letters:", listToString(letters)
        else:
            return input_letter
    # end

    
def check_guess(word, guess):
    """
    Taking a word which is string and guessing letter, 
    return True if the word contains guessing letter 
    and False otherwise. 
    """
    # start
    if guess.lower() in word or guess.upper() in word:
        return True
    else:
        return False
    # end

    
def ask_yesno(prompt):
    """
    Display the text prompt and let's the user enter a string.
    If the user enters "y", the function returns "True",
    and if the user enters "n", the function returns "False"
    If the user enters anything else, the function prints "I beg your pardon!",
    and asks again, repeating this until the user has entered a correct string.

    In fact, it is exactly same as the one you've done in the Lab. 
    """
    # start
    response = raw_input(prompt)
    while True:
        if response == "y":
            return True
        elif response == "n":
            return False
        else:
            print "I beg your pardon!"
            return None
    # end


wordlist = load_words()

# Here is the main loop!
while True:
    word = choose_word(wordlist)
    word_state = make_init_state(word)
    avail_letters = alphabet[:]
    num_of_guesses = 8    # the number of guesses the user have

    print "-----------------------------------------------------------"
    print "Welcom to the CS101 Hangman!"
    print "-----------------------------------------------------------"
    print "I am thinking of a word that is", len(word), "letters long."

    while num_of_guesses > 0 and not compare_list_str(word_state, word):
        # show remaining guesses and available letters
        print "*" * num_of_guesses                  
        print "You have", num_of_guesses, "guesses left."
        print "Available letters:", listToString(avail_letters)
        print 
    
        guess = getGuess(avail_letters)

        if check_guess(word, guess):
            """
            Because the guessing letter is in the word, you should update word_state
            and print it. 
            
            e.g. word = 'apple', guess = 'p', and previous word_state = ['_', '_', '_', '_', '_']
            then, word_state -> ['_', 'p', 'p', '_', '_']
            And "Good guess: _ p p _ _" should be printed. 
            (Hint: using listToString function to print it nicely like "_ p p _ _" instead of "_pp__")
            """
            # start
            for index in range (len(word)):
                if word[index] == guess:
                    word_state[index] = guess
            print "Good guess: %s" % listToString(word_state, True)
            avail_letters.remove(guess)
            # end
            
        else:
            """ 
            When the guessing letter is not in the word, you should print error message. 
            
            e.g. if previous word_state = ['_', 'p', 'p', '_', '_'], 
            then "Oops! That letter is not in my word: _ p p _ _ (Notice: not "_pp__")
            """
            # start
            print "Oops! That letter is not in my word: %s" % listToString(word_state, True)
            num_of_guesses -= 1
            avail_letters.remove(guess)
            # end
            
        
        print 

    if num_of_guesses > 0:
        print "Congratulations, you won!"
    else :
        print "You lose!, the answer is", word

    
    """
    You should ask the user if they want to try again or not. 
    (using the function ask_yesno)
    If the user says no then the program should be terminated.
    """
    # start
    next_Round = ask_yesno("Do you want to try again?(y/n) ")
    if not next_Round:
        break
    # end

print "Excessive playing game may harm your eye and health"