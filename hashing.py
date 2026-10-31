import hashlib

message = "Swati Suman"
result = hashlib.sha256(message.encode())

print("Original Message:", message)
print("SHA-256 Hash:", result.hexdigest())
