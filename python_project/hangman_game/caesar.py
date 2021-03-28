"""
File: caesar.py
Name: Lin Wei-Sung
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    TODO: The player will enter a number to determine how far to move the entire letter. After entering the password,
        the system compares the new letter arrangement to a set of addresses,
        and then uses this set of addresses to find out which letters were in the original one.
    pre-condition: Need to enter a number and password (which don't know where it come from)
    post-condition: Magically produce a combination of words that humans can understand.
    """
    number = int(input("Secret number: "))
    code = input("What\'s the ciphered string? ")
    ans = decipher(code,number)
    print("The deciphered string is: %s" %(ans))
def decipher(code, number):
    """
    The program runs in two parts:
    1. New letter columns will be made for secret numbers.
    2. Use the new letter column to compare the position,
        compare the position to the original letter column, find the correct word.
    :param code: unknown combination, probably a word or a sentence.
    :param number: It's used to move Alphabet.
    :return: The word or sentence which is understandable literally.
    """
    str = '' # The string used for decoding.
    str_1 = code.upper()
    correct_word = ''
    for i in range(number):
        str += ALPHABET[len(ALPHABET)-number+i]
    for i in range(len(ALPHABET)-number):
        str += ALPHABET[i]
# ===== The next step is to start decoding.===== #
    for i in range(len(code)):
        if str_1[i].isalpha() == True:
            location = str.find(str_1[i])
            correct_word += ALPHABET[location]
        else:
            correct_word += code[i]
    return correct_word

#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
