import hashlib
import random
from math import gcd

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True          

def generate_prime(start=100, end=500):
    while True:
        num = random.randint(start, end)
        if is_prime(num):
            return num

def modular_inverse(e, phi_n):
    for d in range(1, phi_n):
        if (d * e) % phi_n == 1:
            return d

p = generate_prime()
q = generate_prime()
while q == p:
    q = generate_prime()

n = p * q
phi_n = (p - 1) * (q - 1)
e = random.randint(2, phi_n - 1)
while gcd(e, phi_n) != 1:
    e = random.randint(2, phi_n - 1)
    
d = modular_inverse(e, phi_n)

print("Public Key (e,n):", (e, n))
print("Private Key (d,n):", (d, n))

document = "This is a confidential agreement."
print("\n Original Document:", document)

doc_hash = hashlib.sha256(document.encode()).hexdigest()
print("Document Hash (SHA-256):", doc_hash)

hash_int = int(doc_hash, 16)
signature = pow(hash_int, d, n)
print("Digital Signature:", signature)

received_document = "The Original data has been altered."
received_signature = signature

received_hash = hashlib.sha256(received_document.encode()).hexdigest()
received_hash_int = int(received_hash, 16)

decrypted_hash = pow(received_signature, e, n)
print("\nVerifying Signature...")

if decrypted_hash == received_hash_int % n:
    print("Signature Verified and Valid: Document is authentic.")
else:
    print("Signature Invalid: Document may have been altered.")
