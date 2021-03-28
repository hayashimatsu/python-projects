"""
File: rocket.py
Name: Lin Wei-Sung
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 2

def main():
	"""
	pre-condition:Input the size of the rocket, and draw the rocket
					using the function of each part.
	post-condition:It makes a rocket that look spectacular but can't take off
	:return:
	"""
	head()
	belt()
	upper()
	lower()
	belt()
	head()

def head():
	for i in range(0, SIZE):
		for j in range(0,SIZE-i):
			print(' ', end='')
		for k in range(0,i+1):
			print('/', end='')
		for l in range(0,i+1):
			print('\\', end='') # The first backslash is used to distinguish the later backslash as text
		print("")
def belt():
	print('+', end='')
	for i in range(0, SIZE):
			print('==', end='')
	print('+')
def upper():
	for i in range(0, SIZE):
		print('|', end='')
		for j in range(SIZE-i-1):
			print('.', end='')
		for k in range(i+1):
			print('/\\', end='') # The triangular pattern in the middle increases with each additional section.
		for l in range(SIZE-i-1):
			print('.', end='')
		print('|')
def lower():
	for i in range(0, SIZE):
		print('|', end='')
		for j in range(i):
			print('.', end='')
		for k in range(SIZE-i):
			print('\\/', end='') # The triangular pattern in the middle decreases with each additional section.
		for l in range(i):
			print('.', end='')
		print('|')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()