"""
File: anagram.py
Name: Lin Wei-Sung
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""
import time
# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    2 steps should be followed：
    1. 利用read_dictionary讀取文字檔，並且將所有文字檔按照字數與單次整理起來，方便之後查閱。
        (Use read_dictionary to read text files, and all text files according to the number of words
        and a single sorting up, convenient after access.)
    2. 將輸入的單字透過find_anagrams整理，並且將得到的結果與字典內的單字進行比較，有找到的話將會印出並且於最後統計出現了幾個anagram。
        (The words are sorted through the find_anagrams and the resulting words are compared with the words
        in the dictionary. If they are found, they will be printed and there will be several anagrams at the end.)
    pre-condition: Wait for word be inputted
    post-condition: Lists the words found, and displays a list of occurrences of words and the time taken by the computation.
    :return: None
    """
    testing_str = ""
    dictionary = read_dictionary(FILE)
    while True:
        print("Welcome to stanCode \"Anagram Generator\" (or -1 to quit) ")
        testing_str = input("Show me what you got: ").lower()
        if testing_str == str(-1):
            break
        else:
            # start counting
            start = time.time()
            find_anagrams(testing_str, dictionary)
            # end counting
            end = time.time()
            print(f"The process takes {round(end - start,3)} second")


def read_dictionary(filename):
    """
    為了節省搜尋的時間，讀取文字檔的同時將會按照字數整理好，往後將會按照輸入文字的字數尋找相對應的key。
    In order to save the time of searching, the text file will be sorted according to the number of words
    when it is read, and then the corresponding key will be searched according to the number of words of the input text.
    :param filename: File path.
    :return: A sorted dictionary.
    """
    dictionary_number_name_lst = []
    dictionary_name_true = {}
    dictionary = {}
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            name = line.strip()
            number = len(name)
            dictionary_name_true[name] = True
            for key, value in dictionary_name_true.items():
                dictionary_number_name_lst.append((number, (key, value)))
            dictionary_name_true.pop(name)
    for element in dictionary_number_name_lst:
        if element[0] not in dictionary.keys():
            dictionary[element[0]] = []
            dictionary[element[0]].append(element[1])
        else:
            dictionary[element[0]].append(element[1])
    return dictionary


def find_anagrams(target, dictionary):
    """
    find_anagrams將會根據輸入的單字尋找相對應字數的字典key。
        (Find_Anagrams will find the dictionary key that matches the number of words entered.)
    方式是將target(由console讀到的單字)數字化後，整理成字典的形式並命名為target_word_dict，
    以及將編號整理至list內，命名為target_dict_key，並將兩者作為find_anagrams_helper的input，作為判斷的依據。
        (This is done by digitizing the target(the word read by the console), putting it into a dictionary and naming it
         target_word_dict; and put the numbers in the list, named target_dict_key. Both are used as the input of
         find_anagrams_helper to make the judgment.)
    :param target: the word we want to arrange and check it whether is in the dictionary
    :param dictionary: A dictionary sorted by read_dictionary
    :return: the word recognized by the dictionary.
    """
    number = len(target)        # 輸入的文字長度，給予dictionary讀取。(Type the length of the text, let the dictionary read.)
    special_dictionary = {}     # 存取經過dictionary[number]所得到的key(name)與value(True)
                                # Access key(name) and value(True) from dictionary[number]
    give_number_for_target = 0  # 給予輸入單字內的每個字母一個數字編號，未來會讀取的是單字所對應的編號。
                                # Each letter in the input word is given a numeric number.
                                # The number corresponding to the word will be read in the future.
    target_dict_key = []        # 將每個字母的編號做成一個list (Make a list of the numbers of each letter)
    target_word_dict = {}       # 將單字的字母與編號用dictionary的形式記錄起來，用於日後排列組合用的。
                                # The letters and numbers of a word are recorded in the form of dictionary
                                # for later arrangement and combination.
    str_temp = ""
    dictionary_creater = dictionary[number]
    for key, value in dictionary_creater:
        special_dictionary[key] = value
    for i in range(number):
        target_dict_key.append(give_number_for_target)
        str_temp = target[i]
        target_word_dict[give_number_for_target] = str_temp
        give_number_for_target += 1
    print("===== Searching engine is working =====")
    word_list = find_anagrams_helper(target_word_dict, target_dict_key, special_dictionary, [], [])
    print("Searching...")
    if len(word_list) == 0:
        print("Sorry man, the word must exist but not for this dictionary")
    else:
        print(str(len(word_list)) + " anagrams: " + str(word_list))
    print("====== Searching 完了いたしました。=======")
    print("")


def find_anagrams_helper(target_word_dict, target_dict_key, dictionary, current, get_word_list):
    """
    將會透過recursion找出所有符合長度的單字，並且透過判斷式紀錄與字典內相符的單字。
        (All words that match the length will be found through recursion,
        and the words that match the dictionary will be recorded through judgment.)
    :param target_word_dict: key = 字母的編號，value = 相對應的字母，
            【for example】；target_word_dict = {0: 'c', 1: 'o', 2: 'n', 3: 't', 4: 'a', 5: 'i', 6: 'n', 7: 's'},
            判斷式將會依照數字找出對應的字母，組合成新的單字後丟進special_dictionary內判斷是否存在。
            (The judgment form will find out the corresponding letters according to the numbers, combine them
            into a new word and throw it into the special_dictionary to determine whether it exists.)
    :param target_dict_key: 由每個字母的編號構成的list，作為構成element的素材。
            (A list composed of the numbers of each letter serves as the material for the elements.)
    :param dictionary: 該處的dictionary為由find_anagrams構成的特製字典，其單字的長度與目標單字的長度相同。
            (The "dictionary" is a special dictionary made up of Find_Anagrams, whose words have the same length
            as the target word.)
    :param current: 透過recursion組成的各種單字。(Words formed through recursion.)
    :param get_word_list: 透過分析過後得到與字典內相符的單字。
            (The words that match the dictionary are obtained through analysis.)
    :return: get_word_list
    """
    if len(current) == len(target_word_dict):
        word = ""
        for i in range(len(current)):
            word += target_word_dict[int(current[i])]
        value = dictionary.get(word)
        if value and word not in get_word_list:
            print("Searching... ")
            get_word_list.append(word)
            print("Found:  "+str(word))
    else:
        for element in target_dict_key:
            if element in current:
                pass
            else:
                # Choose
                current.append(element)
                # Explore
                find_anagrams_helper(target_word_dict, target_dict_key, dictionary, current, get_word_list)
                # Un-choose
                current.pop()
    return get_word_list

# def has_prefix(sub_s):
#     """
#     :param sub_s:
#     :return:
#     """
#     pass


if __name__ == '__main__':
    main()
