"""
File: similarity.py
Name: Lin Wei-Sung
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    TODO:The system will help determine which base sequence has the highest similarity.
        The system will help determine which base sequence has the highest similarity.
        So we need to input a sequence of samples and targets to look for.
    pre-condition: You are asked to enter a string containing ATGC and a set of short section also composed of ATGC.
    post-condition: Find out which part of the ATGC in this small segment
                    is most similar to a long list of ATGCs by comparison, and print it.
    :return: The base sequence with the highest similarity. (with capital sequence)
    """
    long_sequence = input('Please give me a DNA sequence to search: ')
    short_sequence = input('What DNA sequence would you like to match? ')
    most_similar_one = section_finder(long_sequence, short_sequence)
    print('The best match is %s' %(most_similar_one))
def section_finder(sample, target):
    """
    Similarity is determined by integration: if each segment has the same base, one point is added.
    Similarity points are obtained for each analysis, and the segment with the highest number of points is found at the end.
    :param sample: From a longer sequence: a sample sequence
    :param target: The target sequence that will be found in the sample sequence
    :return: The section of the sample sequence with the highest similarity
    """
    str_1 = target.upper()
    str_2 = sample.upper()
    ans = ''
    similarity_point = ''
    for i in range(len(str_2)-len(str_1)+1): # The system will determine how many times to analyze.
        str_3 = str_2[i:i+len(str_1)]   # After each comparison, the system moves the comparison one slot back.
                                        # For example, if you start at 0 this time, you start at 1 the next time.
        count = int(0)
        for j in range (len(str_1)):
            if str_3[j] == str_1[j]:    # Each set of fragments with the same base will get a point,
                count = count + 1       # which will be used as a basis for similarity.
        similarity_point += str(count)
    # The next step is to find the position of the highest number of similarity points.
    index = find_max_point(similarity_point)
    ans = str_2[index:index+len(target)]
    return ans

def find_max_point(str_similar):
    """
    This function will look for the maximum value in the string
    and return the position of the maximum value in the string.
    :param str_similar: The string of statistical similarity points
    :return: The position of the string with the maximum number of similarity points.
    """
    max = str_similar[0]
    for i in range(len(str_similar)-1):
        if str_similar[i+1] >= max:
            max = str_similar[i+1]
    location = str_similar.find(str(max))
    return location

###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
