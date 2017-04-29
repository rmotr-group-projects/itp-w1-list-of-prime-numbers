"""This is the entry point of the program."""


def _is_prime(number):
    for i in range(2,number):
        if number%i == 0:
            return False
    return True
        
            


def list_of_prime_numbers(max_number):
    prime_list = []
    for i in range(2,max_number+1):
         if _is_prime(i):
            prime_list.append(i)
    return prime_list
    
if __name__ == '__main__':
    print(_is_prime(19))
