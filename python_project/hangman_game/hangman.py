"""
File: hangman.py
Name: Lin Wei-Sung
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    TODO: A set of words is selected at random, and the player
        has a limited number of times to guess what the random word is.
    """
    answer = random_word()
    quiz = ''
    for i in range(len(answer)):
        quiz += '-'
    rest_turns = N_TURNS
    print('The word looks like: %s' %(quiz))
    print('You have %s guesses left.' %(N_TURNS))
    pre_step = quiz     # The initial value is the same as the quiz because the answer has not been answered.
    while True:
        ch = input('Your guess: ')
        if ch.isalpha() == False or len(ch) > 1 :
            print('illegal format')
        else:
            guess_word = ch.upper()
            current_step = case_analyze(answer, pre_step, guess_word) # The status of the quiz is determined
                                                                      # by the next step of the input letter
        # ===== Failure zone ===== #
            if answer.find(guess_word) == -1:   # The condition in which the guessed letter is not in the string.
                print("There is no %s's in the word." %(guess_word))
                pre_step = current_step
                rest_turns -= 1
                if rest_turns > 0:
                    print('The word looks like: %s' % (current_step))
                    print("You have %s guesses left." %(rest_turns))
                else:
                    print('You are completely hung :(')
                    print('The word was: %s' %(answer))
                    break
        # ===== Success zone ===== #
            else:
                print("You are correct!")
                if current_step in answer:
                    print('You Win!!')
                    print('The word was: %s' %(current_step))
                    break
                else:
                    print('The word looks like: %s' %(current_step))
                    print("You have %s guesses left." % (rest_turns))
                    pre_step = current_step


def case_analyze(answer, pre_step, guess_word):
    """
    Analyses can tell if the player's input letter is in the string, and how many of the same letters there are.
    :param answer: Well...just the answer from the random.
    :param pre_step: The result from the previous step is predetermined to be a "-" of the same length as the answer.
    :param guess_word: The value entered by the player
    :return: Analyze the result that the letter has/does not correspond in the string.
    """
    location = ''   # Record the address of the letter in the answer
    start = 0       # Start at the beginning of the answer.
    if answer.find(guess_word) == -1:
        return pre_step
    else:
        while True:
            point = answer.find(guess_word, start)
            if point < len(answer) and point >= 0:  # If the address is less than the length of the answer,
                                                    # let the system automatically find the last number of the answer.
                location += str(point)
                start = point + 1                    # The starting point of the search letter is updated each time, and a +1 is used to skip the found points.
            else:
                break
    """
    What if a string has the same letters in it?
    First of all, the position of the first letter was compared with the answer. And update this result to pre_step.
    Second, use 'for' to change the address of the next appearing letter.
    """
    for j in range(len(location)):
        ch = ''
        for i in range(len(answer)):
            if i != int(location[j]):
                ch += pre_step[i]
            else:
                ch += answer[i]
        pre_step = ch
    return pre_step


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
