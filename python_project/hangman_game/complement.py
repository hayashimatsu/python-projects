"""
File: complement.py
Name: Lin Wei-Sung
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    pre-condition: It starts by asking for A string containing the DNA sequence (A,T,G,C).
    post-condition: The system automatically converts case
                    and outputs the corresponding DNA complementary sequence.
    """
    str_org = input("Please give me a DNA strand and I\'ll find the complement:")
    str_new = dna_transformer(str_org)
    print('The complement of %s is %s' % (str_org, str_new))

def dna_transformer(str):
    """
    The converters convert the DNA sequence to capital letters
    and organize the base pairs corresponding to the most stable ones
    into the lowest energy complementary fragments.
    :param str:You will start with a string (case unknown) made of A,T,G,C
    :return: Returns A string consisting of A,T,G, and C
    """
    ans_1 = str.upper()
    ans_2 = ''
    for i in range(0, len(ans_1)):
        if ans_1[i] == 'A':
            ans_2 += 'T'
        elif ans_1[i] == 'T':
            ans_2 += 'A'
        elif ans_1[i] == 'C':
            ans_2 += 'G'
        elif ans_1[i] == 'G':
            ans_2 += 'C'
    return ans_2
###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
