import random
import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def multiplicative_inverse(e, phi):
	e = e%phi
	for x in range (1,phi):
		if((e*x)%phi==1):
			return x
	return 1

	
def is_prime(num):
    if num > 1:
        for i in range(2,num):
             if (num % i) == 0:
                 return 0
             else:
                 return 1
    else:
        return 0


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    
    n = p * q
    phi = (p-1) * (q-1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = multiplicative_inverse(e, phi)
    
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [(ord(char)**key) % n for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    return(''.join(plain))
    


    
print ("RSA Encrypter/ Decrypter")
primes = [i for i in range(1,10000) if is_prime(i)==1]
p = random.choice(primes)
q = random.choice(primes)
print ("Generating your public/private keypairs now . . .")
public, private = generate_keypair(p, q)
print ("Your public key is ", public ," and your private key is ", private)
message = input("Enter a message to encrypt with your private key: ")
encrypted_msg = encrypt(private, message)
print ("Your encrypted message is: ")
print (''.join(map(lambda x: str(x), encrypted_msg)))
print ("Decrypting message with public key ", public ," . . .")
print ("Your message is:")
print (decrypt(public, encrypted_msg))

'''
Joyson Gaurea 8390

RSA Encrypter/ Decrypter
Generating your public/private keypairs now . . .
Your public key is  (33031897, 40635075)  and your private key is  (15998713, 40635075)
Enter a message to encrypt with your private key: hi
Your encrypted message is:
1815421417287050
Decrypting message with public key  (33031897, 40635075)  . . .
Your message is:
hi
'''