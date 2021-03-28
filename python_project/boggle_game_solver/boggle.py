"""
File: boggle.py
Name: Lin Wei-Sung
----------------------------------------
TODO: To build a system that fits Boggle's rules, you first have to build a board
	and find out if the combination of words on the board matches the words in the dictionary.
"""
import time
# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO:步驟有二
	1. 製作一個4*4的矩陣，在console內輸入(文字+空格)*4次後換行，如果不按照規則則會強制停止輸入。
		Make a 4 × 4 matrix and type (text + space)*4 times in the Console to wrap the line.
		If you don't follow the rules, you will be forced to stop.
	2. 利用find_word輸入讀取的字典與棋盤，find_word將會進入recursion mode: 從棋盤上尋找各種路徑所組合的單字。
		Using the dictionary and checkerboard read by find_word input,
		find_word will enter recursion mode: looking for words combined by various paths on the boggleboard.
	pre-condtion: 等待輸入棋盤內的文字
	 				(Wait for input of text in the boggleboard)
	post-condition: 顯示出該棋盤的組合下共有多少個單字被記錄在dictionary內，並一一列出。
					(Shows how many words are recorded in the dictionary under the combination
					of the checkerboard, and lists them one by one.)
	"""
	count = 0
	boggle_board = [list() for i in range(4)]
	turn_down_boggle = False
	dictionary = read_dictionary(FILE)
	while True:
		if count == 4 or turn_down_boggle == True:
			print("boggle board is finished!")
			break
		else:
			str = input(f"{count + 1} row of letters: ")
			# check space's location
			for i in range(len(str)):
				space_location = i % 2
				if space_location == 1:
					if str[i] != " ":
						print("Illegal input")
						turn_down_boggle = True
						break
				else:
					boggle_board[count].append(str[i].lower())
			count += 1
	# start counting
	start = time.time()
	find_word(dictionary, boggle_board)
	# end counting
	end = time.time()
	print(f"The process takes {round(end - start, 4)} second")


def read_dictionary(filename):
	"""
	將所有的單字都視為key，value則為True，往後只要不是在字典內的單字則會被判斷成None
	(All words are treated as keys, value is True,
	and any word that is not in the dictionary will be judged as None thereafter.)
	:param filename: location of dictionary.txt
	:return: dictionary format：dictionary[word]=[True]
	"""
	dictionary_name_true = {}
	with open(filename, 'r') as f:
		lines = f.readlines()
		for line in lines:
			name = line.strip()
			dictionary_name_true[name] = True
	return dictionary_name_true


def find_word(dictionary, boggle_board):
	"""
	每次都賦予一個空字串word_lst來儲存現存的所有組合，未來將會使用組合去判斷是否存在於dictionary內
	(Each time an empty word_lst string is given to store all the existing combinations,
	which will be used in the future to determine if they are in the dictionary)
	:param dictionary: dictionary format：dictionary[word]=[True]
	:param boggle_board: boggleboard with 4*4 type
	:return: None
	"""
	word_lst = []
	for x in range(len(boggle_board)):
		for y in range(len(boggle_board)):
			current_lst = []
			exploration_gateway = False
			total_word_list = find_word_helper(boggle_board, dictionary, x, y, current_lst, word_lst, exploration_gateway)
	print(f"There are {len(total_word_list)} words in total.")

def find_word_helper(boggle_board, dictionary, org_x, org_y, current, word_lst, exploration_gateway):
	"""
	# 請容許我用中文敘述我的想法 #
	1.	由於棋盤上的單字有可能是重複的，因此將每個字母都以座標表示，這樣才有獨一性。
		current 是個list == [(x1, y1), (x2, y2)...]，要將current利用for row, column in current的方式，
		將矩陣的座標(row, column)套入boggle_board(棋盤)內，找出相對應的字，組合成要找尋的詞。
	2.	exploration_gateway代表有沒有4字以上的可能性，一開始都是使用False，在find_word_helper內的判斷式中，
		開關為False才能被檢視是否為單字，如果是單字的話，會將開關打開，並進入下一階段的recursion，
		本對策為對付每次進入recursion都要經過判斷式的考驗，光只有current >= 4只會將搜尋目標限制在四個字母。
	3.	base_case：當所有的路徑都被記錄在current內，經過"if element in current:"的判斷式一直都是pass的情況，就會退回。
	:param boggle_board: boggleboard with 4*4 type.
	:param dictionary: dictionary format：dictionary[word]=[True]
	:param org_x: The x coordinate of the current position on the board is determined by find_word.
	:param org_y: The y coordinate of the current position on the board is determined by find_word.
	:param current: Find nearby coordinates under X and Y coordinates, and record them in "current".
	:param word_lst: A word that is identified by the coordinates accessed in current
	:param exploration_gateway: The switch for "Whether to continue looking for more than four characters".
	:return: All word combinations found under the x,y coordinates.
	"""
	if len(current) >= 4 and exploration_gateway == False:
		word = ""
		for row, column in current:
			word += boggle_board[row][column]
		value = dictionary.get(word) # .get("key")
		if value and word not in word_lst:
			exploration_gateway = True
			word_lst.append(word)
			print("Found:  " + str(word))
			# Try to look through the word for longer words
			find_word_helper(boggle_board, dictionary, org_x, org_y, current, word_lst, exploration_gateway)
	else:
		target_x = 0
		target_y = 0
		for i in range(-1, 2, 1):
			for j in range(-1, 2, 1):
				# Retrieves a coordinate that corresponds to a position in the matrix
				# within a range adjacent to one unit.
				target_x = org_x + i
				target_y = org_y + j
				if 0 <= target_x < len(boggle_board):
					if 0 <= target_y < len(boggle_board):
						element = (target_x, target_y)
						if element in current:
							pass
						else:
							# choose
							current.append(element)
							# explore
							exploration_gateway = False
							find_word_helper(boggle_board, dictionary, target_x, target_y, current, word_lst, exploration_gateway)
							# un-choose
							current.pop()
	return word_lst

# def has_prefix(sub_s):
# 	"""
# 	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
# 	:return: (bool) If there is any words with prefix stored in sub_s
# 	"""
# 	pass

if __name__ == '__main__':
	main()
