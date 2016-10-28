def _is_prime(number):
    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
        

def list_of_prime_numbers(max_number):
    alist = []
    for i in range(2, max_number + 1):
        if _is_prime(i):
            alist.append(i)
    return alist
    
    

if __name__ == '__main__':
    print(_is_prime(1))
