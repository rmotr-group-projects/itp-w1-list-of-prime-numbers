"""This is the entry point of the program."""


def _is_prime(number) : 
    index = 2
    is_prime = True
    while index < number : 
        if number % index == 0 : 
            is_prime = False
            index += 1
            
        else : 
            index += 1
            pass
    return is_prime


def list_of_prime_numbers(max_number) : 
    index = 1
    list = []
    while index <= max_number : 
        if _is_prime(index) : 
            list.append(index) 
            index += 1
        else : 
            index += 1
            pass
    return list

if __name__ == '__main__':
    print(_is_prime(19))