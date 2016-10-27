"""This is the entry point of the program."""

# Sorry, got a head start 
from math import sqrt

def _is_prime(number):
    # 1 is not a prime number, so start with 2
    i = 2
    while i <= sqrt(number):
        # if the number is divisible by any number lower than its sqrt, not a prime
        if number % i == 0:
            return False
        # check with next number
        i += 1
    # If reached here without exit, it is prime
    return True

def list_of_prime_numbers(max_number):
    # build sieve of erysthothanes(sp?)
    sieve = [0] * (max_number+1)
    # manually mark 0 and 1 as not prime
    if max_number < 2:
        return []
    
    [sieve[0], sieve[1]] = [1, 1]
    output = []
    
    # loop over all elements and mark off the primes
    for index in range(max_number+1):
        # reiterate if the number selected is not prime
        if sieve[index] != 0:
            continue
        
        # Add to output if prime
        output.append(index)
        
        # Mark off multiples in sieve
        for i in range(index, max_number+1, index):
            sieve[i] += 1
    
    return output

if __name__ == '__main__':
    print(_is_prime(4))
    print(list_of_prime_numbers(100))
