
def _is_prime(number):
    if number == 1:
        return False
    if number == 2:
        return True
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def list_of_prime_numbers(max_number):
    list_of_primes = []
    for x in range(1,max_number+1):
        if _is_prime(x) == True:
            list_of_primes.append(x)
        
    return list_of_primes


if __name__ == '__main__':
    print(_is_prime(19))




