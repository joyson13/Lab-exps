import random
import random
def isPrime(num):
    if num > 1:
        for i in range(2,num):
             if (num % i) == 0:
                 return 0
             else:
                 return 1
    else:
        return 0

primes = [i for i in range(1,10000) if isPrime(i)==1]

def attack():
	print("Before attack\n")

	p = random.choice(primes)
	g = random.choice(primes)
	
	print("Value of p is:\t",p)
	print("Value of g is:\t",g)

	a = random.choice(primes)
	b = random.choice(primes)
	print("The Private key for Alice is:\t",a)
	x = (g**a)%p
	y = (g**b)%p
	print("The Public key for Alice is:\t",x)
	tom_b = random.choice(primes)
	tom_y = (g**tom_b)%p
	print("The Public key for Tom is:\t",tom_y)

	a_k1 = (y**a)%p
	print("Alice's Key 1:\t",a_k1)
	a_k2 = (x**tom_b)%p
	print("Alice's Key 2:\t",a_k2)

	print("The Private key for Bob is:\t",b)
	
	print("The Public key for Bob is:\t",y)
	tom_a = random.choice(primes)
	tom_x = (y**tom_a)%p
	print("The Private key for Tom is:\t",tom_x)

	b_k1 = (y**tom_a)%p
	print("Bob's Key 1:\t",b_k1)
	b_k2 = (x**b)%p
	print("Bob's Key 2:\t",b_k2)
	
	print("\nAfter attack:\n")
	print("Alice's key 1:\t",a_k1)
	print("Alice's key 2:\t",tom_y)
	print("Tom's key 1:\t",tom_y)
	print("Tom's key 2:\t",tom_x)
	print("Bob's key 1:\t",tom_x)
	print("Bob's key 2:\t",b_k2)

print("Key Exchange with man in middle present")
attack()

'''
Joyson Gaurea 8390

Value of p is:   7149
Value of g is:   4677
The Private key for Alice is:    4803
The Public key for Alice is:     594
The Public key for Tom is:       3954
Alice's Key 1:   6468
Alice's Key 2:   4233
The Private key for Bob is:      9421
The Public key for Bob is:       2931
The Private key for Tom is:      4512
Bob's Key 1:     4512
Bob's Key 2:     6468

After attack:

Alice's key 1:   6468
Alice's key 2:   3954
Tom's key 1:     3954
Tom's key 2:     4512
Bob's key 1:     4512
Bob's key 2:     6468
'''