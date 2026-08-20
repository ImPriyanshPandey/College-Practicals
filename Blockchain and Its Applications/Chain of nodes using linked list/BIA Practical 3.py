import random
from math import gcd

def is_prime(n):
    if n<2:
        return False
    for i in range (2, int(n**0.5)+1):
        if n%i==0:
            return False
        return True

def generate_prime(start=100, end=500):
    while True:
        num=random.randint(start, end)
        if is_prime(num):
            return num

def modular_inverse(e, phi_n):
    for d in range (1, phi_n):
        if (d*e)%phi_n==1:
            return d

p = generate_prime()
q = generate_prime()

while q==p:
    q = generate_prime()

n=p*q

phi_n = (p-1)*(q-1)

e=random.randint(2, phi_n-1)
while gcd(e, phi_n)!=1:
    e = random.randint(2, phi_n-1)

d = modular_inverse(e, phi_n)

print("Public Key(e,n):", (e, n))
print("Private Key(d,n):", (d, n))

message = "HELLO"

print("\nOriginal Message:", message)

cipher_C=[]
for char in message:
    ascii_value =  ord(char)
    encrypted_value = pow(ascii_value, e, n)

    cipher_C.append(encrypted_value)

print("Encrypted Message:", cipher_C)

decrypted_chars=[]

for char in cipher_C:
    decrypted_number =pow(char, d, n)
    original_char = chr(decrypted_number)

    decrypted_chars.append(original_char)

decrypted_M = ' '.join(decrypted_chars)
print("Decrypted Message:", decrypted_M)
