def _is_prime(num):
    if num == 1:
        return True
        
    elif num == 2 or num == 3 or num == 5 or num == 7:
        return True
        
    else:
        prime = False
        for i in range(2, 9):
            if num % i == 0:
                prime = False
                break

            else:
                i += 1
                prime = True
        return prime


def list_of_prime_numbers(num):
    primelist = []
    for i in range(num+1):
        if _is_prime(i) == True:
            primelist.append(i)
        else:
            pass
    return primelist