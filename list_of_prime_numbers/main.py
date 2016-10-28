"""This is the entry point of the program."""


def _is_prime(number):
    if number < 2:
        return False
    if number == 2 or number == 3:
        return True
    for i in range(2, number - 1):
        if number % i == 0:
            return False
    return True

def list_of_prime_numbers(max_number):
    prime_list = []
    for j in range(1, max_number + 1):
        if _is_prime(j) == True:
            prime_list.append(j)
    return prime_list



if __name__ == '__main__':
    print(_is_prime(19))


