"""This is the entry point of the program."""


def _is_prime(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return False
        else:
            return True
    else:
        return False



def list_of_prime_numbers(max_number):
    prime = []
    for i in range(max_number + 1):
        if _is_prime(i):
            prime.append(i)
    return prime

if __name__ == '__main__':
    print(_is_prime(19))
