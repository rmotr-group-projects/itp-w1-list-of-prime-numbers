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
    oddNumber = range(3, max_number + 1, 2)
    numbers = set(sum([range(i * i, max_number, i + i) for i in oddNumber], []))
    if max_number > 1:
        return [2] + [j for j in oddNumber if j not in numbers]
    else:
        return [j for j in oddNumber if j not in numbers]

if __name__ == '__main__':
    print(_is_prime(19))
