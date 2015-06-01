#!/usr/bin/env python

# This is a second python file and contains a function that prints
# whether the given number is a prime number or not.
def is_prime(num):
  
    if num == 1 or num <= 0:
        print "Numbers less than below 2 are not prime numbers"
    else:
        for item in range(2,num):
            if num % item == 0:
                print "%s is not a Prime Number" % num
                break  
            else:
                continue
        else:
            print "%s is a Prime Number. " % num

if __name__ == '__main__':
    is_prime(4)
    is_prime(7)
