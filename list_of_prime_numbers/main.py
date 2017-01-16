"""This is the entry point of the program."""
import math

def _is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True

def list_of_prime_numbers(max_number):
    list = []
    for i in range(max_number + 1):
        if _is_prime(i):
            list.append(i)
    return list

if __name__ == '__main__':
    print(_is_prime(19))
    print(list_of_prime_numbers(19))
