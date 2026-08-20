import hashlib

input_string = "Blockchain Developer"

byte_string = input_string.encode('utf-8')
hash_object = hashlib.sha256(input_string.encode())

message_digest = hash_object.hexdigest()

print("Input String:", input_string)
print("SHA-256 Message Digest:", message_digest)
