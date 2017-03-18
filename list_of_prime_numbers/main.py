"""This is the entry point of the program."""


def _is_prime(number):
    if number <= 1:
        return False
    else:
        for num in range(2,11):
            if number % num == 0 and number != num:
                return False
        return True

print(_is_prime(4))

def list_of_prime_numbers(max_number):
    primelist = []
    for num in range(max_number+1):
        if _is_prime(num):
            primelist.append(num)
    return primelist
    
print(list_of_prime_numbers(11))

if __name__ == '__main__':
    print(_is_prime(19))
