"""This is the entry point of the program."""
def is_prime(num):
    x = 'np'
    for n in range (2,num):
            if (num % n) != 0:
                x = 'p'
            else:
                x = 'np'
                break
    return x

max_number = 99
list_of_prime_numbers = []

for i in range (max_number):
    if is_prime(i) == 'p':
        list_of_prime_numbers.append (i)

print (list_of_prime_numbers)

"""
90min to figure out the math.
but we got it. 
still not sure how to code out an answer. 

edit-...we've discovered the importance of 'break' statements.

edit - another 30min to figure out the code for the function of calculating
a prime.

edit - this is where we all pause for a bit and reflect upon the staggering 
absense of such a practical answer when googling what is surely every learning 
coder's trial - checking for primes..

edit - after all that, it only took about an additional 30 min (coffee break
included) to finish off the code.

edit - bugger will not test clean "cannot import name list_of_prime_numbers"
well... its in there. im not sure where or why the test isnt working.

"""