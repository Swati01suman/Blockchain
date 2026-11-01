import hashlib

message = input("Enter a message: ")

first_hash = hashlib.sha256(message.encode()).digest()
second_hash = hashlib.sha256(first_hash).hexdigest()

print("\nOriginal Message:", message)
print("First SHA-256:", first_hash.hex())
print("Double SHA-256:", second_hash)
