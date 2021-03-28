"""
File: largest_digit.py
Name: Lin Wei-Sung
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""

def main():

	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: the number we want to check
	:return: the biggest number in this number
	"""
	count = 0
	n = abs(n)
	return find_largest_digit_helper(n, count)


def find_largest_digit_helper(n, count):
	if n < 10:
		# Base case
		print("It takes "+str(O(count))+" time(s)")
		return n
	else:
		quotient = n // 10
		remainder = n % 10
		count += 1
		last_max_number = find_largest_digit_helper(quotient, count)
		if last_max_number > remainder:
			return last_max_number
		else:
			return remainder


def O(count):
	if count == 0:
		return 1
	else:
		return O(count - 1) + 1






if __name__ == '__main__':
	main()
