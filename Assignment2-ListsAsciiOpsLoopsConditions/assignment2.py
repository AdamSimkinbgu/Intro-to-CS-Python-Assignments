# *************** HOMEWORK 2 ***************
# GOOD LUCK!
# ************************ QUESTION 1.1 **************************
### WRITE CODE HERE
def get_digits_list(num):
    """ A simple method which receives an integer, converts and returns a list containing the numbers of
        said integer.
        @param: num[int] - The given number.
        @return: l1[list], a list of num                                                                           V"""
    l1 = []
    temp = str(num)
    for i in range(len(temp)):
        l1.append(int(temp[i]))
    return l1

# ************************ QUESTION 1.2 **************************
### WRITE CODE HERE


def get_num_of_bulls_hits(num, guess):
    """ The method is counting the number of hits and bulls the player achieves and returns a list representing
        said values. For instance, the code entered is 8765 and the guess is 8675, the method would return a list
        containing 2 indexes. The first representing the "bulls" and the second the "hits": [2, 2] in our case.
        @param: num[int] - The given code to guess.
        @param: guess[int] - The given guess to check
        @return: A list containing both the bull and hit counters                                                  V"""

    listed_num = get_digits_list(num)
    listed_guess = get_digits_list(guess)
    bull_counter = 0
    hit_counter = 0
    for i in range(len(listed_num)):
        if listed_guess[i] == listed_num[i]:
            bull_counter += 1
            continue
        for j in range(len(listed_num)):
            if listed_guess[j] == listed_num[i]:
                hit_counter += 1
    return [bull_counter, hit_counter]

# ************************ QUESTION 1.3 **************************
## DO NOT CHANGE THE FOLLOWING CODE!
# Import required module
import random


def no_duplicates_checker(num):
    """
    Args:
         A number.
    Returns:
        Boolean: True if the number has no duplicate digit; otherwise False.
    """
    num_li = get_digits_list(num)
    if len(num_li) == len(set(num_li)):
        return True
    else:
        return False


def is_guess_correct(lst):
    if lst[0] == 4:
        return True
    else:
        return False


def generate_num():
    """ Generate a 4 digits number with no repeated digits
    Return:
         the number
    """
    while True:
        num = random.randint(1000, 9999)
        if no_duplicates_checker(num):
            return num


def play(num=0):
    """ A Bulls and hit game function.
    It gets input from user and print to the user the results.
    Args:
        num [int]: for debugging.
    """
    print("Hello and welcome to Bulls And Hits game!")
    # Secret Code
    if num == 0:
        num = generate_num()
    tries = int(input('Enter number of tries: '))
    ### WRITE CODE HERE
    users_guess = int(input('Enter your guess: '))
    for i in range(tries):
        num_of_bulls, num_of_hits = get_num_of_bulls_hits(num, users_guess)
        user_answer = is_guess_correct([num_of_bulls, num_of_hits])
        if user_answer:
            print('You guessed right!')
            return
        elif i != tries - 1:
            print('bulls:', num_of_bulls, 'hits:', num_of_hits, 'num of tries: ', str(i+1) + '/' + str(tries))
            users_guess = (input('Please try again: '))
    print("You ran out of tries. The number was", num)

play(0)
# ************************ QUESTION 2.1 **************************
### WRITE CODE HERE


def my_is_upper(text):
    """ This method is responsible to check a text is made of only uppercase letters. the method ignores
        non letters characters during the check.
        @param: text [str] - a given text to the program
        @return: boolean value represents whether the text is uppercase [True] or not [False].                     V"""
    for letter in text:
        temp = letter
        if ord('a') <= ord(temp) and ord(temp) <= ord('z'):
            return False
    return True


def my_is_lower(text):
    """ This method is responsible to check a text is made of only lowercase letters. the method ignores
        non letters characters during the check.
        @param: text [str] - a given text to the program
        @return: boolean value represents whether the text is lowercase [True] or not [False].                     V"""
    for letter in text:
        temp = letter
        if ord('A') <= ord(temp) and ord(temp) <= ord('Z'):
            return False
    return True

# ************************ QUESTION 2.2 **************************
### WRITE CODE HERE


def my_upper(text):
    """ This method converts all lowercase letters to uppercase letters but ignores any other type of characters
        @param: text [str] - a given text to the program
        @return: returns a string containing the text converted to uppercase                                       V"""
    converted_text = ''
    for letter in text:
        temp = letter
        if ord('a') <= ord(temp) and ord(temp) <= ord('z'):
            converted_text += chr(ord(temp) - 32)
            continue
        converted_text += letter
    return converted_text

def my_lower(text):
    """ This method converts all uppercase letters to lowercase letters but ignores any other type of characters
        @param: text [str] - a given text to the program
        @return: returns a string containing the text converted to lowercase                                       V"""
    converted_text = ''
    for letter in text:
        temp = letter
        if ord('A') <= ord(temp) and ord(temp) <= ord('Z'):
            converted_text += chr(ord(temp) + 32)
            continue
        converted_text += letter
    return converted_text

# ************************ QUESTION 2.3 **************************
### WRITE CODE HERE
def string_changer(text):
    """ This method is a lower and upper case letter switching algorithm. A given text is converted, letter by letter,
        to uppercase from lowercase and vice versa. On the occurrence of "$" in the text, the program toggles off it's
        conversion feature until the next appearance of "$" in the text. Every odd number of "$" toggles the conversion
        off and an even number toggles it on (including zero).
        @param: text [str] - A given text for the program to manipulate according to the rules mentioned
        @return: Returns a converted list back.                                                                    V"""
    converted_text = ''
    dollar_counter = 0
    for letter in text:
        temp = letter
        if letter == '$':
            dollar_counter += 1
            continue
        if dollar_counter % 2 == 0:
            if ord('A') <= ord(temp) and ord(temp) <= ord('Z'):
                converted_text += chr(ord(temp) + 32)
                continue
            elif ord('a') <= ord(temp) and ord(temp) <= ord('z'):
                converted_text += chr(ord(temp) - 32)
                continue
        converted_text += temp
    return converted_text