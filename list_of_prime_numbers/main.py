"""This is the entry point of the program."""


def _is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False 
    
    else:
        return True


def list_of_prime_numbers(max_number):
    results_list = []
    for i in range(1, max_number+1):
        if _is_prime(i) is True:
            results_list.append(i) 
            
    return results_list
    
   

    


if __name__ == '__main__':
   print(list_of_prime_numbers(19))
