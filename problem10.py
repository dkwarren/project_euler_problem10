"""
	Projet Euler # 10
	Author:		David Warren II
	Date: 		4 May, 2017
	Objective:	Find the sum of all primes below 2,000,000

	Note: 	I will use the sieve of Eratosthenes to find all primes
		between 0 and 2,000,000 then sum them.
"""
import sys
import math

def log(message): # error catcher
	print(message)

def sum(primes):
	total = 0
	for i in range(2, len(primes)): # because 0 and 1 don't count
		total += primes[i]
	return total

def sieve(n):
	numbers = [1] * n # all numbers between 0 and n
	primes = [] # our list of primes

	for i in range(2, int(math.sqrt(len(numbers)))): # between 2 and sqrt(n)
		if (numbers[i]): # if the value is 1
			x = 1
			for j in range(i**2, n, x * i): # i^2 + i, i^2 + 2i, ...
				numbers[j] = 0 # sets the value to false denoting non-prime
				x += 1

	for i in range(n):
		if (numbers[i]): # if true, then it is a prime
			primes.append(i) # our list of primes
	return sum(primes)

def main(n):
	print("Finding the sum of all primes below %d" % n)
	print("The sum of primes below %d is %d" % (n, sieve(n)))

if __name__ == "__main__":
	if (len(sys.argv) == 2): # makes sure there is an argument
		main(int(sys.argv[1])) 
	else:
		log("This program needs at least 1 integer argument.")