"""This is the entry point of the program."""

def _is_prime(number):
    
    is_prime = True # flag 
    
    if number < 2: # numbers less than two are not considered to be prime
        is_prime = False
    
    for factor in range(2,int(number ** 0.5) + 1): #search for factors can stop at this point
        if (number % factor == 0):
            is_prime = False
            break # stop searching if number is not a prime 
            
    return is_prime

def list_of_prime_numbers(max_number):
    
    prime_numbers = [] 
    
    for prime in range(2,max_number+1):
        if _is_prime(prime): 
            prime_numbers.append(prime) # add the prime number to list
    
    return prime_numbers
        
if __name__ == '__main__':
    print(_is_prime(19))
    print(list_of_prime_numbers(100000))