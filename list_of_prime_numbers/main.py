"""This is the entry point of the program."""


def _is_prime(number):
    if number==1:
        return False
    for b in range(2, number):
        if number%b==0:
            return False
    return True


def list_of_prime_numbers(max_number):
        lsty=[]
        for c in range(2, max_number+1):
            if _is_prime(c)==True:
                lsty.append(c)
        return lsty
        

if __name__ == '__main__':
    print(_is_prime(19))
