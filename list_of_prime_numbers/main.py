"""This is the entry point of the program."""


def _is_prime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    else:
        return True


def list_of_prime_numbers(x):
    a=[]
    for i in range(2,x+1):
        if _is_prime(i):
            a.append(i)
    return a

if __name__ == '__main__':
    print(_is_prime(19))
