"""This is the entry point of the program."""


def _is_prime(number):
    if number == 1:
        return False
    for n in range((number - 1), 1, -1):
        if number % n == 0:
            return False
    return True


def list_of_prime_numbers(max_number):
    # Alternate solution
    # return [n for n in range(1, (max_number + 1)) if _is_prime(n)]

    results = []
    for number in range(1, (max_number + 1)):
        if _is_prime(number):
            results.append(number)

    return results


if __name__ == '__main__':
    print(_is_prime(19))
