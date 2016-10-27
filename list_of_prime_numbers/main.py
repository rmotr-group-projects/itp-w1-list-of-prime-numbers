def _is_prime(number):
    if number == 1:
        return False
        
    else:
	
        is_prime = True
    	for i in range(2, number):
            if number % i == 0:
                is_prime = False

    return is_prime





def list_of_prime_numbers(max_number):
    prime_numbers = []
    if max_number == 0:
        return prime_numbers
    elif max_number == 1:
        return prime_numbers
   
    for i in range(1, max_number + 1):
        if _is_prime(i):
            prime_numbers.append(i)
            
    return prime_numbers

if __name__ == '__main__':
    print(_is_prime(19))

print _is_prime(20)