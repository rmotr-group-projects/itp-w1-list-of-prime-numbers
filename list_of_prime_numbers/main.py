"""This is the entry point of the program."""
import math

def _is_prime(number):
    if number == 0 or number == 1: # Check for 1 and 0
        return False
    if number == 2: # Check for 2 which is a prime
        return True
    elif (number % 2) == 0: # Check if they are even
        return False
    else:
        for x in range(3, int(math.sqrt(number)) + 1, 2):
            if number % x == 0:
                return False
        return True # These are primes


def list_of_prime_numbers(max_number):
        prime = []
        for x in range(max_number + 1):
            if _is_prime(x):
                prime.append(x)
        return prime


# if __name__ == '__main__':
#     print(_is_prime(19))
