# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 20:30:59 2019

@author: Callum
"""

'''

PRIME FACTORIZATION - by Callum Alexander

This program allows you to input an integer, prime factorize it, and have it return its
prime factors in an array.
The list of prime numbers is generated each time based on the input number, using the AKS
primality test. Computationally, this test is pretty heavy, however it can test if the number is 
prime in polynomial time and is deterministic, unlike faster algorithms.

The program recursively calculates the prime factors by dividing the input number by the lowest possible
prime until the remainder on the division equals zero. This process is recursively structured until the
input value has 2 prime factors.

dependencies include math

'''


from math import sqrt


def PrimeFactorization(n, factorArray, primeArray, primeFactor, count):

    
    b = n / primeFactor # divsion occurs

    #if a divisible prime
    if n%primeFactor == 0:
        
        count = 0
        factorArray.append(primeFactor) # adds the prime factor to the array of factors
        primeFactor = primeArray[0] # returns the testing factor to 2
        n = b # setting the input number to the other factor of the division
        PrimeFactorization(n, factorArray, primeArray, primeFactor, count) # recursion occuring
        
    #non divisible
    elif n%primeFactor != 0 and n != 1: # The condition for n !=1 ensures that the recursions stops when n is prime
        
        count += 1 # if the division has a remainder, it will test the next value in the list of prime numbers
        primeFactor = primeArray[count]
        PrimeFactorization(n, factorArray, primeArray, primeFactor, count) # recursions occuring




def populatePrimeArray(n, array):
    upper = int(n/4 * 3) # populates the list of prime numbers up to 75% of the actual input value
    for i in range(2, upper):
        if aksPrimalityTest(i) == True:
            array.append(i)
    return array


def aksPrimalityTest(n): # AKS Primality Test - see wikipedia for more information
    if n==2:
        return True
    c=1
    for i in range(n//2+1):
        c=c*(n-i)//(i+1)
        if c%n:
            return False
    return True


n = int(input('Input the number that you want to prime factorize >>>>>>>  '))
factorArray = []
primeArray = []

count = 0

primeArray = populatePrimeArray(n, primeArray)

primeFactor = primeArray[0]
PrimeFactorization(n, factorArray, primeArray, primeFactor, count)
print(factorArray)