"""This is the entry point of the program."""


def _is_prime(number):
	for i in range(2, number):
		if number % i == 0:
			return False
	return True


def list_of_prime_numbers(limit):
	result = []
	for i in range(1, limit + 1):
		if _is_prime(i):
			result.append(i)
	return result

if __name__ == '__main__':
    print(_is_prime(19))
