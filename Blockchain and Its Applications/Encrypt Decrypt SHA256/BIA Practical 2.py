import hashlib

original_message = "Hello World"


hash_object = hashlib.sha256(original_message.encode())
message_digest = hash_object.hexdigest()

print("Original Message:", original_message)
print("SHA-256 Message Digest/Hash:", message_digest)


user_input = "Hello Universe"
user_hash = hashlib.sha256(user_input.encode()).hexdigest()

print("\nUser Input:", user_input)
print("\nVerifying message...")

if user_hash == message_digest:
    print("Message is authentic (hashes match); hence decryption successful: message verified")
else:
    print("Message has been changed (hashes do NOT match); hence verification failed!")
