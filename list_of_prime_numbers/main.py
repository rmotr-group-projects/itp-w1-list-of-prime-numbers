"""This is the entry point of the program."""


def _is_prime(number):
    #if number < 2: return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def list_of_prime_numbers(max_number):
    primes_list =[]
    for number in range(1, max_number+1):
        if _is_prime(number) is True:
            primes_list += [number]    
    return primes_list

if __name__ == '__main__':
    print(_is_prime(1))
    print(list_of_prime_numbers(19))
