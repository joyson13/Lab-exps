#8390 Joyson Gaurea
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
p = random.choice(primes)
g = random.choice(primes)
print("Value of p is:\t",p)
print("Value of g is:\t",g)
a = random.choice(primes)
b = random.choice(primes)
print("The Private key for Alice is:\t",a)
print("The Private key for Bob is:\t",b)
x=(g**a)%p
y=(g**b)%p
print("Public keys for Alice and Bob are ",x," and ",y," respectively")
print("Public keys are exchanged here")
print("Alice receives public key ",y," and\n Bob receives public key ",x)
ka = (y**a)%p
kb = (x**b)%p
print("Secret keys of Alice and Bob are ",ka," and ",kb," respectively")

'''
Joyson Gaurea 8390

Value of p is:   2351
Value of g is:   1409
The Private key for Alice is:    5057
The Private key for Bob is:      491
Public keys for Alice and Bob are  2030  and  1112  respectively
Public keys are exchanged here
Alice receives public key  1112  and
 Bob receives public key  2030
Secret keys of Alice and Bob are  194  and  194  respectively
'''