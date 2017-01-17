"""This is the entry point of the program."""


def _is_prime(number):
    if number>1:
        for i in range(2,number):
            if number % i == 0:
                return False
        else:
            return True


def list_of_prime_numbers(max_number):
    list=[]
    if max_number>1:
        for n in range(2,max_number+1):
            if _is_prime(n):
                list.append(n)
                n += 1
        return list
    else:
        list=[]
        return list

if __name__ == '__main__':
    print(_is_prime(33))
    print(list_of_prime_numbers(0))
