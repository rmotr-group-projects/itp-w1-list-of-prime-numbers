"""This is the entry point of the program."""


def _is_prime(number):
  #Account for 0, 1, and 2. These don't play nice with our logic.
  if number == 1 or number == 0:
    return False
  elif number == 2:
    return True
  else:
  #Begin prime algorithm. Check modulus of each number between 2 and 
  #the sqrt of our number. If modulus is 0, the number divides in
  #evenly. Add 1 to our range to account for slice index.
	  is_prime = True
	  for i in range(2,(int(number ** .5) + 1)):
		  if number % i == 0:
			  is_prime = False
			  #Make sure we break out so that the loop doesn't
			  #overwrite our variable.
			  break
	  return is_prime


def list_of_prime_numbers(max_number):
    list_of_primes = []
    #Make sure you add 1 to the range due to slice index.
    for i in range(max_number + 1):
        #Use our previous function. If true, append
        #the number to list_of_primes.
        if _is_prime(i):
            list_of_primes.append(i)
    return list_of_primes

if __name__ == '__main__':
    print(_is_prime(19))
