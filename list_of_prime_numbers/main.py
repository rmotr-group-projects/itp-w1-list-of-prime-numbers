"""This is the entry point of the program."""


def _is_prime(num):
    primes = []
    if num <= 1 or isinstance(num,float):
      return False
    if num % 2 == 0 and num > 2:
      return False
    else:
      for i in range(2,int(num**0.5)+1):
        if num % i == 0:
          return False
      return True

def list_of_prime_numbers(max_number):
    primes = []
    for num in range(max_number + 1):
        if _is_prime(num):
          primes.append(num)
    return primes

if __name__ == '__main__':
    print(_is_prime(19))
