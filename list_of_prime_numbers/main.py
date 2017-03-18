"""This is the entry point of the program."""


def _is_prime(number):
    
    if number == 1:
        return False
    elif number == 2:
        return True
    else: 
        for i in range(2, number):
            if number%i==0 :
                return False
        else:
            return True
        
        


def list_of_prime_numbers(max_number):
    list_primes=[]
    for n in range(2, max_number+1):
        if _is_prime(n) == True:
            list_primes.append(n)
        else: 
            continue
    return list_primes

if __name__ == '__main__':
    print(_is_prime(19))
