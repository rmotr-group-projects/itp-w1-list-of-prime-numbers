"""This is the entry point of the program."""

def _is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    else:
        return True

def list_of_prime_numbers(max_number):
    list_of_primes = []
    for a in range(2, max_number + 1):
        if _is_prime(a):
            list_of_primes.append(a)
    return list_of_primes


if __name__ == '__main__':
    print(_is_prime(19))


