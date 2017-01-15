"""This is the entry point of the program."""


def _is_prime(number):
    isPrime = 0
    prime_list = []
    if number==0:
        return "not a valid number"
    if number==1:
        return False

    for x in range(number-2):
        if (number % (x+2)) == 0:
            isPrime = isPrime + 1

    if isPrime == 0:
        return True
    else:
        return False


def list_of_prime_numbers(max_number):
    prime_list = []
    counter = 1
    while counter <= max_number:
        if _is_prime(counter):
            prime_list.append(counter)
        counter += 1
    return prime_list
    

if __name__ == '__main__':
    print(_is_prime(19))


# def list_of_prime_numbers(max_number):
# list = []
# counter = 1
# while counter < max_number:
# if _is_prime(counter):
# list.append(counter)
# counter += 1
# return list

