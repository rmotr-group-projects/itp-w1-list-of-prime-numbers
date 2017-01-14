def _is_prime(number):
    if number == 1:
        return False
    elif number == 2 or number == 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    else:
        return True


def list_of_prime_numbers(max_number):
    list = []
    counter = 2
    while counter <= max_number:
        if _is_prime(counter):
            list.append(counter)
        counter += 1
    return list